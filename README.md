# File-Store-Url-Shortner-Bot

<div align="LEFT">
  <img src="https://c4.wallpaperflare.com/wallpaper/273/577/73/zero-two-darling-in-the-franxx-anime-girls-pink-hair-darling-in-the-franxx-wallpaper-preview.jpg" width="600" alt="vegacodes">
</div>

<br>

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

[![Deploy to Koyeb](https://www.koyeb.com/static/images/deploy/button.svg)](https://app.koyeb.com/deploy?type=git&repository=github.com/misterrnova/File-Store-Url-Shortner-Bot&branch=koyeb&name=filesharingbot)

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

* `API_HASH` Your API Hash from my.telegram.org
* `APP_ID` Your API ID from my.telegram.org
* `TG_BOT_TOKEN` Your bot token from @BotFather
* `OWNER_ID` Must enter Your Telegram Id
* `CHANNEL_ID` Your Channel ID eg:- -100xxxxxxxx
* `DATABASE_URL` Your mongo db url
* `DATABASE_NAME` Your mongo db session name
* `ADMINS` Optional: A space separated list of user_ids of Admins, they can only create links
* `START_MESSAGE` Optional: start message of bot, use HTML and fillings
* `FORCE_SUB_MESSAGE`Optional:Force sub message of bot, use HTML and Fillings
* `FORCE_SUB_CHANNEL` Optional: ForceSub Channel ID, leave 0 if you want disable force sub
* `PROTECT_CONTENT` Optional: True if you need to prevent files from forwarding

### Extra Variables

* `CUSTOM_CAPTION` put your Custom caption text if you want Setup Custom Caption, you can use HTML andfillings for formatting (only for documents)
* `DISABLE_CHANNEL_BUTTON` Put True to Disable Channel Share Button, Default if False
* `BOT_STATS_TEXT` put your custom text for stats command, use HTML and fillings
* `USER_REPLY_TEXT` put your text to show when user sends any message, use HTML


### Fillings
#### START_MESSAGE | FORCE_SUB_MESSAGE

* `{first}` - User first name
* `{last}` - User last name
* `{id}` - User ID
* `{mention}` - Mention the user
* `{username}` - Username

#### CUSTOM_CAPTION

* `{filename}` - file name of the Document
* `{previouscaption}` - Original Caption

#### CUSTOM_STATS

* `{uptime}` - Bot Uptime


### Credits

- Thanks To Dan For His Awsome [Libary](https://github.com/pyrogram/pyrogram)
- 
- Our Support Group Members

### Licence
[![GNU GPLv3 Image](https://www.gnu.org/graphics/gplv3-127x51.png)](http://www.gnu.org/licenses/gpl-3.0.en.html)  

[File-Store-Url-Shortner-Bot](https://github.com/misterrnova/File-Store-Url-Shortner-Bot/) is Free Software: You can use, study share and improve it at your
will. Specifically you can redistribute and/or modify it under the terms of the
[GNU General Public License](https://www.gnu.org/licenses/gpl.html) as
published by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version. 

##

   **Star this Repo if you Liked it ⭐⭐⭐**



