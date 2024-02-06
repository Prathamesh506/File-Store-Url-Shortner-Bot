# File Sharing Bot

Telegram bot for storing posts and documents, accessible via special links.

<div align="center">
  <img src="http://ForTheBadge.com/images/badges/made-with-python.svg" width ="200" alt="Made with Python">
  <img src="https://github.com/CodeXBotz/PyrogramGenStr/blob/main/resources/madebycodex-badge.svg" width="200" alt="Made by CodeXBotz">
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

```bash
git clone https://github.com/CodeXBotz/File-Sharing-Bot
cd File-Sharing-Bot
pip3 install -r requirements.txt
# <Create config.py appropriately>
python3 main.py
