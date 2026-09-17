# 🎓 ITsGOLU Extractor

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python&logoColor=white)
![Pyrofork](https://img.shields.io/badge/Pyrofork-Pyrogram_Fork-orange)
![MongoDB](https://img.shields.io/badge/MongoDB-Motor%20Async-green?logo=mongodb)
![License](https://img.shields.io/badge/License-See%20LICENSE-lightgrey)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)



> 🚀 **This bot can be deployed on Render, Heroku, Koyeb, Railway, Google Cloud Run, Google Colab, VPS, and Termux.** See [Deployment](#-deployment).

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Commands Reference](#-commands-reference)
- [Environment Variables](#-environment-variables)
- [Deployment](#-deployment)
- [BotFather Setup](#-botfather-setup)
- [MongoDB Atlas Setup](#-mongodb-atlas-setup)
- [Security Notes](#️-security-notes)
- [Repository Structure](#-repository-structure)
- [Troubleshooting](#-troubleshooting)

---



## 💬 Commands Reference

### Platform Extractors

| Command | Platform | Notes |
|---|---|---|
| `/pw` | Physics Wallah | Prompts for phone number, OTP, then course ID |
| `/cp` | Classplus | Interactive login flow |
| `/maakichut` | Career Will | Interactive login flow |
| `/kd` | KD Campus (`kdlive`) | Interactive login flow |
| `/adda` | Adda247 | Interactive login flow |
| `/utkarsh` | Utkarsh Classes | Interactive login flow |
| `/my` | MyPathshala | Interactive login flow |
| `/ak` | AK-based platform | Interactive login flow |
| `/iq` | IQ-based platform | Interactive login flow |
| `/rgvikramjeet` | RG Vikramjeet platform | Interactive login flow |

### AppX (multiple API versions)

| Command | Purpose |
|---|---|
| `/appx` | AppX extraction (v4 API) |
| `/appxm` | AppX extraction (v3 API) |
| `/apiv1` | AppX extraction (v1 API) |
| `/appxotp` | AppX OTP-based login/extraction |

### Utilities

| Command | Purpose |
|---|---|
| `/enc` | Reply to a `.txt` file to AES-encrypt the URLs inside it |
| `/dec` | Reply to a bot-encrypted file to decrypt it |
| `/enchelp` | Shows help for the encryption module |
| `/html2txt` | Converts HTML content to plain text |
| `/txt2html` | Converts plain text to HTML |
| `/getapi` | Extracts an API key/token from a given input |
| `/cancel` | Cancels an in-progress extraction/conversation |

### Premium System

| Command | Access | Purpose |
|---|---|---|
| `/myplan` | Everyone | Check your own premium status |
| `/chk_premium` | Everyone | Check premium status (by reply/argument, depending on context) |
| `/add_premium` | Owner | Grant premium access to a user |
| `/remove_premium` | Owner | Revoke a user's premium access |
| `/premium_users` | Owner | List all current premium users |

### Owner / Admin

| Command | Purpose |
|---|---|
| `/start` | Starts the bot; shows the welcome menu |
| `/stats` | Bot usage statistics (owner only) |
| `/broadcast` | Sends a message to every known user (owner only) |
| `/forward` | Forwards a message to the configured log channel (owner only) |
| `/announce` | Posts an announcement (owner only) |
| `/eval` / `/x` | Runs arbitrary Python code (owner only — ⚠️ see [Security Notes](#️-security-notes)) |
| `/sh` | Runs an arbitrary shell command (owner only — ⚠️ see [Security Notes](#️-security-notes)) |

---

## 🔑 Environment Variables

| Variable | Required | Default | Purpose |
|---|---|---|---|
| `API_ID` | ✅ Yes | — | From [my.telegram.org](https://my.telegram.org) |
| `API_HASH` | ✅ Yes | — | From [my.telegram.org](https://my.telegram.org) |
| `BOT_TOKEN` | ✅ Yes | — | From @BotFather |
| `BOT_USERNAME` | ✅ Yes | — | Your bot's username, without `@` |
| `OWNER_ID` | ✅ Yes | — | Your numeric Telegram user ID (get from @userinfobot) |
| `SUDO_USERS` | ❌ No | *(defaults to `OWNER_ID`)* | Space-separated list of additional admin user IDs |
| `CHANNEL_ID` | ✅ Yes | — | Log channel ID — the bot must be admin there |
| `CHANNEL_ID2` | ✅ Yes | — | Force-subscribe channel ID — the bot must be admin there |
| `MONGO_URL` | ✅ Yes | — | MongoDB connection string (e.g. from MongoDB Atlas) |
| `PREMIUM_LOGS` | ✅ Yes | — | Channel/chat ID used for premium-related logs |
| `THUMB_URL` | ❌ No | *(a default image)* | Default thumbnail image URL |

All required variables must be set as **plain values** (not left empty) — the bot validates each one at startup and exits with a clear error message naming the missing variable, rather than crashing with a raw Python error.

---

## 🚀 Deployment

This bot is **polling-based** (Pyrogram's `idle()`, not a Telegram webhook), so it doesn't strictly need a public URL to function. The included Flask server exists only to satisfy platforms (like Render's free tier) that require the process to bind a port. It supports **Render, Heroku, Koyeb, Railway, Google Cloud Run, Google Colab, VPS, and Termux**.

### One-Click Deploy

| Platform | Deploy |
|---|---|
| Render | [![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy?repo=https://github.com/Alex638796/ITsGOLU_EXTRACTOR) |
| Heroku | [![Deploy to Heroku](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/Alex638796/ITsGOLU_EXTRACTOR) |
| Koyeb | [![Deploy to Koyeb](https://www.koyeb.com/static/images/deploy/button.svg)](https://app.koyeb.com/deploy?type=git&repository=github.com/Alex638796/ITsGOLU_EXTRACTOR&branch=main&name=itsgolu-extractor) |
| Google Colab | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Alex638796/ITsGOLU_EXTRACTOR/blob/main/colab_deploy.ipynb) |
| Google Cloud | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.svg)](https://ssh.cloud.google.com/cloudshell/editor?cloudshell_git_repo=https://github.com/Alex638796/ITsGOLU_EXTRACTOR&cloudshell_tutorial=.cloudshell/GCLOUD.md) |

> ⚠️ None of these badges fully automate deployment — each opens that platform's setup screen where you still need to fill in environment variables manually (see the table above). They save the "find and configure a new app" step, not the "enter your credentials" step.

> ℹ️ **Railway**: this bot can also be deployed on Railway — it auto-detects the Python app via Nixpacks and picks up `requirements.txt` + `Procfile` with no extra configuration needed. There's no one-click badge here because Railway deploy buttons require a pre-registered Railway template (a manual one-time setup on Railway's side, separate from this repo). To deploy: create a new Railway project → "Deploy from GitHub repo" → select this repo → set the environment variables from the table above.

### Render / Heroku / Koyeb / Google Cloud Run

All four use the included `Dockerfile` (Render and Koyeb/Cloud Run directly; Heroku via `heroku.yml`, which points at the same Dockerfile). After clicking a badge, fill in the environment variables from the table above. For manual Cloud Run deployment via `gcloud` CLI, see `.cloudshell/GCLOUD.md`.

### Google Colab (temporary/testing)

Click the Colab badge above to open `colab_deploy.ipynb`. Fill in the mandatory fields (`API_ID`, `API_HASH`, `BOT_TOKEN`, `BOT_USERNAME`, `OWNER_ID`, `CHANNEL_ID`, `CHANNEL_ID2`, `MONGO_URL`, `PREMIUM_LOGS`) — optional fields (`SUDO_USERS`, `THUMB_URL`) come pre-filled or can be left blank — and run the single cell. It clones the repo, installs dependencies, and runs `python3 run.py`. The cell blocks and streams logs live; press ■ to stop.

> ⚠️ Colab sessions are temporary (disconnect on tab close, inactivity, or after Colab's free-tier time limit — up to ~12 hours). Use this for quick testing only; for always-on hosting, use Render/Heroku/Koyeb/Railway above.

### VPS

```bash
git clone https://github.com/Alex638796/ITsGOLU_EXTRACTOR.git
cd ITsGOLU_EXTRACTOR
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
# edit .env with your values
python3 run.py
```

Or via Docker, using the included `Dockerfile`:

```bash
git clone https://github.com/Alex638796/ITsGOLU_EXTRACTOR.git
cd ITsGOLU_EXTRACTOR
sudo apt install docker.io -y
sudo docker build -t itsgolu-extractor .
sudo docker run -it --rm --env-file .env itsgolu-extractor
```

No public URL is required — this bot works over polling on any VPS with outbound internet access.

### Termux (Android)

```bash
pkg update && pkg upgrade -y
pkg install python git -y
git clone https://github.com/Alex638796/ITsGOLU_EXTRACTOR.git
cd ITsGOLU_EXTRACTOR
pip install -r requirements.txt
cp .env.example .env
# edit .env with your values
python3 run.py
```

> If any package fails to build on Termux, run `pkg install libffi openssl` first, then retry `pip install -r requirements.txt`. A remote MongoDB instance (e.g. MongoDB Atlas's free tier) is recommended over trying to run MongoDB on-device.

---

## 🤖 BotFather Setup

1. Open Telegram, message **@BotFather**.
2. Send `/newbot`, choose a name and username.
3. Copy the **Bot Token** → `BOT_TOKEN`, and the username (without `@`) → `BOT_USERNAME`.
4. Get your numeric Telegram ID (e.g. via @userinfobot) → `OWNER_ID`.
5. Get `API_ID` and `API_HASH` from [my.telegram.org](https://my.telegram.org).

## 🍃 MongoDB Atlas Setup

1. Create a free cluster at [mongodb.com/cloud/atlas](https://www.mongodb.com/cloud/atlas).
2. Database Access → create a user with read/write permissions.
3. Network Access → add `0.0.0.0/0` (allow from anywhere, required for most hosts).
4. Connect → Drivers → copy the connection string → `MONGO_URL` (insert your DB user password).

---

## ⚠️ Security Notes

- **`/eval`, `/x`, and `/sh` execute arbitrary Python code and shell commands** on the host running the bot, restricted to `OWNER_ID`/`SUDO_USERS` only. Keep your bot token, owner ID, and `SUDO_USERS` list private — anyone who can message the bot as one of those IDs has full code execution on your server/container.
- Never commit real values for `API_ID`, `API_HASH`, `BOT_TOKEN`, or `MONGO_URL` to source control, even as comments or "example" defaults — treat every one of these as a secret.
- `MONGO_URL` contains your database password — rotate it if it's ever exposed (committed to a public repo, pasted in a chat, etc).

---

## 🗂 Repository Structure

```
ITsGOLU_EXTRACTOR/
├── run.py                     # Supervisor: runs app.py + Extractor together, forwards shutdown signals
├── app.py                      # Flask health-check server
├── config.py                   # Environment variable loading + validation
├── secure.py
├── requirements.txt
├── Dockerfile                  # Used by Render, Koyeb, Railway, Google Cloud Run, VPS-via-Docker
├── Procfile                     # Heroku process definition
├── heroku.yml                   # Heroku container deploy config
├── app.json                    # Heroku one-click deploy manifest
├── render.yaml                  # Render service definition
├── colab_deploy.ipynb           # Google Colab one-click deploy notebook
├── .cloudshell/                 # Google Cloud Shell walkthrough
│   ├── tutorial.yaml
│   └── GCLOUD.md
├── .env.example
├── appxapis.json                # AppX API endpoint definitions
└── Extractor/
    ├── __init__.py               # Bot client initialization
    ├── __main__.py                # Entry point (Pyrogram idle loop, graceful shutdown)
    └── modules/
        ├── start.py, stats.py, plans.py, broadcast.py, eval.py, check.py
        ├── enc.py                 # URL encryption/decryption utility
        ├── findapi.py              # API key extraction
        ├── appex_v1.py / appex_v2.py / appex_v3.py / appex_v4.py / getappxotp.py / freeappx.py
        ├── pw.py, classplus.py, careerwill.py, adda.py, utk.py, kdlive.py, mypathshala.py, freecp.py, freepw.py
        └── ak.py, iq.py, mix.py, exampur.py, khan.py, vision.py, rg_vikramjeet.py
```

---

## 🧯 Troubleshooting

**Bot exits immediately on startup with a `❌ ... is missing` message**
- One of the required environment variables isn't set. The message names exactly which one — set it and restart.

**Bot doesn't respond after deploy**
- Check host logs for the "» ʙᴏᴛ ᴅᴇᴘʟᴏʏ sᴜᴄᴄᴇssғᴜʟʟʏ" startup line — if missing, verify `BOT_TOKEN`, `API_ID`, and `API_HASH` are correct.
- Confirm the Flask health-check route (`/`) returns `200 OK`.

**Force-subscribe / login prompts fail**
- Confirm the bot is admin in both `CHANNEL_ID` (log channel) and `CHANNEL_ID2` (force-sub channel).

**A platform-specific extraction command doesn't respond to prompts**
- Reply directly to the bot's prompt messages rather than sending a new unrelated message — the interactive login flow (`app.ask()`) waits for a reply in the same chat.
- Use `/cancel` to reset a stuck conversation before retrying.

**MongoDB connection errors**
- Confirm Network Access allows `0.0.0.0/0` and the password in `MONGO_URL` doesn't contain unescaped special characters (URL-encode if needed).

**Render/Heroku free tier sleeping**
- Free tier instances may spin down after inactivity; since this bot needs to run continuously, a paid always-on tier is recommended for production use.
