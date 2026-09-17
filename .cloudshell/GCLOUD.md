# Deploy to Google Cloud Run

This bot ships with a `Dockerfile`, so it deploys to Cloud Run with no extra
build configuration.

## 1. Set your project

```sh
gcloud config set project YOUR_PROJECT_ID
```

## 2. Build and deploy

```sh
gcloud run deploy itsgolu-extractor \
  --source . \
  --region us-central1 \
  --allow-unauthenticated \
  --set-env-vars \
API_ID=your_api_id,\
API_HASH=your_api_hash,\
BOT_TOKEN=your_bot_token,\
BOT_USERNAME=your_bot_username,\
OWNER_ID=your_telegram_user_id,\
CHANNEL_ID=your_log_channel_id,\
CHANNEL_ID2=your_force_sub_channel_id,\
MONGO_URL=your_mongodb_connection_string,\
PREMIUM_LOGS=your_premium_logs_channel_id
```

Cloud Run will print a service URL when this finishes (e.g.
`https://itsgolu-extractor-xxxxx.a.run.app`). This bot doesn't need that URL
for core functionality (it's polling-based, not webhook-based) — it's only
there to satisfy the platform's health-check requirement.

## 3. Verify

```sh
gcloud run services describe itsgolu-extractor --region us-central1
```

Visit the printed service URL — it should return `Hello from Tech VJ`.

See `.env.example` in the repo root for what each variable means and how to
obtain it (my.telegram.org, BotFather, userinfobot, MongoDB Atlas, etc).
