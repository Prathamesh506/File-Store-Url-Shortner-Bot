# File Sharing Bot

Telegram bot for storing posts and documents, accessible via special links.

![Made with Python](http://ForTheBadge.com/images/badges/made-with-python.svg)
![Made by CodeXBotz](https://github.com/CodeXBotz/PyrogramGenStr/blob/main/resources/madebycodex-badge.svg)

## Features

- Fully customizable.
- Customizable welcome & ForceSub messages.
- Supports more than one post in one link.
- Can be deployed on Heroku directly.

## Setup

- Add the bot to a Database Channel with all permissions.
- Add the bot to a ForceSub channel as an Admin with "Invite Users via Link" permission if you enable ForceSub.

## Installation

### Deploy on Heroku

Click the button below to deploy to Heroku.

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

Check out this [Tutorial Video](https://youtu.be/LCrkRTMkmzE) on YouTube for help.

### Deploy on Railway

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/new/template/1jKLr4)

### Deploy on Koyeb

Click the button below to deploy to Koyeb.

[![Deploy to Koyeb](https://www.koyeb.com/static/images/deploy/button.svg)](https://app.koyeb.com/deploy?type=git&repository=github.com/CodeXBotz/File-Sharing-Bot&branch=koyeb&name=filesharingbot)

### Deploy on your VPS

```bash
git clone https://github.com/CodeXBotz/File-Sharing-Bot
cd File-Sharing-Bot
pip3 install -r requirements.txt
# <Create config.py appropriately>
python3 main.py
