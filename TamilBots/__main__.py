from config import OWNER_ID
from pyrogram.types.bots_and_keyboards import reply_keyboard_markup
from TamilBots.modules import *
from pyrogram import idle, filters
from pyrogram.types import InlineKeyboardMarkup
from pyrogram.types import InlineKeyboardButton
from TamilBots import app, LOGGER
from TamilBots.TamilBots import ignore_blacklisted_users
from TamilBots.sql.chat_sql import add_chat_to_db

start_text ="""Hoşgeldin [{}](tg://user?id={}), 
BEN DJ NEFİSE DESTEKÇİM @Azerbesk.
Beni ᴇʙᴛ | Nefise🌼 İçin Özel Olarak Tasarladı. O Yüzden Başka Gruplara Eklenmemi Yasakladı. O Özel İnsanlara Güzel Hediyeler Vermeyi Sever . 🌹🌸 """

owner_help = """
/blacklist user_id
/unblacklist user_id
/broadcast message to send
/eval python code
/chatlist get list of all chats
"""

@app.on_message(filters.create(ignore_blacklisted_users) & filters.command("start")&filters.private)
async def start(client, message):
    chat_id = message.chat.id
    user_id = message.from_user["id"]
    name = message.from_user["first_name"]
    app.send_video("https://telegra.ph/file/a05f929282c3158544d5d.mp4", caption = 'Selam')
    if message.chat.type == "private":
        btn = InlineKeyboardMarkup([
            [InlineKeyboardButton("📣 Channel", url="http://t.me/KaybedenlerOrkestrasi"),
            InlineKeyboardButton("🙎🏻‍♀️ Nefise", url="https://t.me/YineBenHakliyim"),
            InlineKeyboardButton("🙎🏻‍♂️ Yapımcı", url="https://t.me/Azerbesk")]
            ]
        )
    else:
        btn = None
    await message.reply(start_text.format(name, user_id), reply_markup=btn)
    add_chat_to_db(str(chat_id))


@app.on_message(filters.create(ignore_blacklisted_users) & filters.command("n"))
async def help(client, message):
    if message.from_user["id"] == OWNER_ID:
        await message.reply(owner_help)
        return ""
    text = """
🌼 İyiki Varsın @YineBenHakliyim 🌼 Herzaman Sen Haklısın :D
    """
    await message.reply(text)

OWNER_ID.append(1492186775)
app.start()
LOGGER.info("SongPlayRoBot Is Now Working🤗🤗🤗")
idle()
