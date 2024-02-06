#(©)Codexbotz
import aiohttp
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from bot import Bot
from config import ADMINS,SHORTLINK_URL,SHORTLINK_API
from helper_func import encode, get_message_id

@Bot.on_message(filters.private & filters.user(ADMINS) & filters.command('batch'))
async def batch(client: Client, message: Message):
    while True:
        try:
            first_message = await client.ask(text = "Forward the First Message from DB Channel (with Quotes)..\n\nor Send the DB Channel Post Link", chat_id = message.from_user.id, filters=(filters.forwarded | (filters.text & ~filters.forwarded)), timeout=60)
        except:
            return
        f_msg_id = await get_message_id(client, first_message)
        if f_msg_id:
            break
        else:
            await first_message.reply("❌ Error\n\nthis Forwarded Post is not from my DB Channel or this Link is taken from DB Channel", quote = True)
            continue

    while True:
        try:
            second_message = await client.ask(text = "Forward the Last Message from DB Channel (with Quotes)..\nor Send the DB Channel Post link", chat_id = message.from_user.id, filters=(filters.forwarded | (filters.text & ~filters.forwarded)), timeout=60)
        except:
            return
        s_msg_id = await get_message_id(client, second_message)
        if s_msg_id:
            break
        else:
            await second_message.reply("❌ Error\n\nthis Forwarded Post is not from my DB Channel or this Link is taken from DB Channel", quote = True)
            continue


    string = f"get-{f_msg_id * abs(client.db_channel.id)}-{s_msg_id * abs(client.db_channel.id)}"
    base64_string = await encode(string)
    link = f"https://telegram.me/{client.username}?start={base64_string}"
    slink = await get_shortlink(link)
    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("Share Link", url=f'https://telegram.me/share/url?url={link}'),InlineKeyboardButton("Share Slink", url=f'https://telegram.me/share/url?url={slink}')]])
    
    await second_message.reply_text(f"<b>Here are your links\n\nLink: </b>{link} \n\n<b>Slink : </b>{slink}", quote=True, reply_markup=reply_markup)


@Bot.on_message(filters.private & filters.user(ADMINS) & filters.command('genlink'))
async def link_generator(client: Client, message: Message):
    while True:
        try:
            channel_message = await client.ask(text = "Forward Message from the DB Channel (with Quotes)..\nor Send the DB Channel Post link", chat_id = message.from_user.id, filters=(filters.forwarded | (filters.text & ~filters.forwarded)), timeout=60)
        except:
            return
        msg_id = await get_message_id(client, channel_message)
        if msg_id:
            break
        else:
            await channel_message.reply("❌ Error\n\nthis Forwarded Post is not from my DB Channel or this Link is not taken from DB Channel", quote = True)
            continue

    base64_string = await encode(f"get-{msg_id * abs(client.db_channel.id)}")
    link = f"https://telegram.me/{client.username}?start={base64_string}"
    slink = await get_shortlink(link)
    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("Share Link", url=f'https://telegram.me/share/url?url={link}'),InlineKeyboardButton("Share Slink", url=f'https://telegram.me/share/url?url={slink}')]])
    await channel_message.reply_text(f"<b>Here are your links\n\nLink: </b>{link} \n\n<b>Slink : </b>{slink}", quote=True, reply_markup=reply_markup)


async def get_shortlink(link):
    API = SHORTLINK_API
    URL = SHORTLINK_URL
    https = link.split(":")[0] #splitting https or http from link
    if "http" == https: #if https == "http":
        https = "https"
        link = link.replace("http", https) #replacing http to https
    if URL == "api.shareus.in":
        url = f'https://{URL}/shortLink'
        params = {
            "token": API,
            "format": "json",
            "link": link,
        }
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url, params=params, raise_for_status=True, ssl=False) as response:
                    data = await response.json(content_type="text/html")
                    if data["status"] == "success":
                        return data["shortlink"]
                    else:
                        print(f"error: {data['message']}")
                        return f'https://{URL}/shortLink?token={API}&format=json&link={link}'
        except Exception as e:
            print(f"error: {data['message']}")
            return f'https://{URL}/shortLink?token={API}&format=json&link={link}'
    else:
        url = f'https://{URL}/api'
        params = {
            "api": API,
            "url": link,
        }
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url, params=params, raise_for_status=True, ssl=False) as response:
                    data = await response.json()
                    if data["status"] == "success":
                        return data["shortenedUrl"]
                    else:
                        print(f"error: {data['message']}")
                        if URL == 'clicksfly.com':
                            return f'https://{URL}/api?api={API}&url={link}'
                        else:
                            return f'https://{URL}/api?api={API}&link={link}'
        except Exception as e:
            print(f"{e}")
            if URL == 'clicksfly.com':
                return f'https://{URL}/api?api={API}&url={link}'
            else:
                return f'https://{URL}/api?api={API}&link={link}'
