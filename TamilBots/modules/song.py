from pyrogram import Client, filters
import asyncio
import os
from pytube import YouTube
from pyrogram.types import InlineKeyboardMarkup
from pyrogram.types import InlineKeyboardButton
from youtubesearchpython import VideosSearch
from TamilBots.TamilBots import ignore_blacklisted_users, get_arg
from TamilBots import app, LOGGER
from TamilBots.sql.chat_sql import add_chat_to_db


def yt_search(song):
    videosSearch = VideosSearch(song, limit=1)
    result = videosSearch.result()
    if not result:
        return False
    else:
        video_id = result["result"][0]["id"]
        url = f"https://youtu.be/{video_id}"
        return url


@app.on_message(filters.create(ignore_blacklisted_users) & filters.command("e"))
async def song(client, message):
    chat_id = message.chat.id
    user_id = message.from_user["id"]
    add_chat_to_db(str(chat_id))
    args = get_arg(message) + " " + "e"
    if args.startswith(" "):
        await message.reply("HATA! 👉🏼 /e Şarkı Adı")
        return ""
    status = await message.reply("👸🏻 DJ Nefise Şarkıyı Gönderiyor Biraz Bekle Tatlım 🌼")
    video_link = yt_search(args)
    if not video_link:
        await status.edit("🥺 Şarkıyı Bulamadım")
        return ""
    yt = YouTube(video_link)
    audio = yt.streams.filter(only_audio=True).first()
    try:
        download = audio.download(filename=f"{str(user_id)}")
    except Exception as ex:
        await status.edit("The song could not be downloaded 😶")
        LOGGER.error(ex)
        return ""
    rename = os.rename(download, f"{str(user_id)}.mp3")
    await app.send_chat_action(message.chat.id, "upload_audio")
    await app.send_audio(
        chat_id=message.chat.id,
        caption="Şarkı Hazır Bana Teşekkür Et 🙆🏻‍♀️",
        audio=f"{str(user_id)}.mp3",
        duration=int(yt.length),
        title=str(yt.title),
        performer="DJ NEFİSE",
        reply_to_message_id=message.message_id,        
    )
    await status.delete()
    os.remove(f"{str(user_id)}.mp3")
