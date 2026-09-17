#!/usr/bin/env python3
"""
Supervisor script: runs app.py (Flask health-check server) and
Extractor (the Pyrogram bot) as subprocesses, and forwards
SIGTERM/SIGINT to both, so a platform's restart/redeploy/health-check
signal reaches the bot process cleanly instead of only killing the
parent shell.

This replaces the previous DYNO-based branching, which only ran the
bot (never the web server) on Heroku -- breaking any platform that
requires a bound port for health checks (Render, Heroku web dyno,
Koyeb, etc). Both processes now always run together, everywhere.
"""

import os
import signal
import subprocess
import sys
import time

from dotenv import load_dotenv

load_dotenv()  # no-op if a real environment (Render/Heroku/etc) already set vars

# Verify required credentials are present before spawning anything --
# config.py itself exits with a clear message if something's missing,
# so this import is the validation step.
import config  # noqa: F401

procs = []


def start():
    os.makedirs("sessions", exist_ok=True)
    procs.append(subprocess.Popen([sys.executable, "app.py"]))
    procs.append(subprocess.Popen([sys.executable, "-m", "Extractor"]))


def handle_signal(signum, frame):
    print(f"Supervisor received signal {signum}, forwarding to children...")
    for p in procs:
        if p.poll() is None:
            try:
                p.send_signal(signum)
            except Exception as e:
                print(f"Error signaling process {p.pid}: {e}")
    for p in procs:
        try:
            p.wait(timeout=15)
        except subprocess.TimeoutExpired:
            print(f"Process {p.pid} did not exit in time, killing.")
            p.kill()
    sys.exit(0)


signal.signal(signal.SIGTERM, handle_signal)
signal.signal(signal.SIGINT, handle_signal)

start()

# Monitor: if either process dies unexpectedly, bring the whole
# supervisor down so the host platform notices and restarts cleanly,
# rather than limping along with only one half of the app running.
try:
    while True:
        time.sleep(2)
        for p in procs:
            ret = p.poll()
            if ret is not None:
                print(f"Process {p.pid} exited with code {ret}, shutting down supervisor.")
                for other in procs:
                    if other is not p and other.poll() is None:
                        other.terminate()
                sys.exit(ret or 1)
except KeyboardInterrupt:
    handle_signal(signal.SIGINT, None)
