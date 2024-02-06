# File-Store-Url-Shortner-Bot

Telegram bot for storing posts and documents, accessible via special links.

<div align="left">
  <img src="http://ForTheBadge.com/images/badges/made-with-python.svg" width ="200" alt="Made with Python">
</div>

## Features

- **Fully Customizable:** Tailor the bot to fit your needs perfectly.
- **Welcoming Messages:** Greet your users with personalized welcome and ForceSub messages.
- **Efficient Link Generation:** Easily create links for multiple posts or individual posts.
- **Heroku Deployment:** [Deploy on Heroku](https://heroku.com/deploy)

## Setup

- Add the bot to a Database Channel with all necessary permissions.
- Ensure the bot is added as an Admin to the ForceSub channel, granting "Invite Users via Link" permission if you enable ForceSub.

## Installation

### Deploy on Heroku

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

### Deploy on Railway

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/new/template/1jKLr4)

### Deploy on Koyeb

[![Deploy to Koyeb](https://www.koyeb.com/static/images/deploy/button.svg)](https://app.koyeb.com/deploy?type=git&repository=github.com/CodeXBotz/File-Sharing-Bot&branch=koyeb&name=filesharingbot)

### Deploy on Your VPS

#### Deploy in your VPS
````bash
git clone https://github.com/CodeXBotz/File-Sharing-Bot
cd File-Sharing-Bot
pip3 install -r requirements.txt
# <Create config.py appropriately>
python3 main.py
````

## Admin Commands

Manage your bot efficiently with these commands:

```
/start: Begin interaction with the bot or retrieve posts.
/batch: Generate a link for multiple posts simultaneously.
/genlink: Create a link for a single post.
/users: Access bot statistics and user insights.
/broadcast: Send broadcast messages to all bot users.
/stats: Check the bot's uptime and performance metrics.
```

### Variables

- `API_HASH`: Your API Hash from my.telegram.org
- `APP_ID`: Your API ID from my.telegram.org
- `TG_BOT_TOKEN`: Your bot token from @BotFather
- `OWNER_ID`: Your Telegram ID
- `CHANNEL_ID`: Your Channel ID (e.g., -100xxxxxxxx)
- `DATABASE_URL`: Your MongoDB URL
- `DATABASE_NAME`: Your MongoDB session name
- `ADMINS`: Optional list of user_ids of Admins (space-separated)
- `START_MESSAGE`: Optional start message of bot
- `FORCE_SUB_MESSAGE`: Optional ForceSub message of bot
- `FORCE_SUB_CHANNEL`: Optional ForceSub Channel ID (leave 0 to disable ForceSub)
- `PROTECT_CONTENT`: Optional: True if you need to prevent files from forwarding


