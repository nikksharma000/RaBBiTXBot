from pyrogram import Client, filters
from pyrogram.types import *
import requests
import os
from Imshivaexe import Bunny
from config import HANDLER as hl

@Bunny.on_message(filters.command("webss", hl) & filters.me)
async def webshot(client, message):
    try:
        user_link = message.command[1]
        await message.edit("`ᴛʀʏɪɴɢ ᴛᴏ ᴛᴀᴋᴇ ᴀ ꜱᴄʀᴇᴇɴꜱʜᴏᴛ...`")
        try:
            full_link = f"https://webshot.deam.io/{user_link}/?width=1920&height=1080?delay=2000?type=png"
            await client.send_photo(message.chat.id, full_link, caption=f"** Screenshot of the page ** `{user_link}`")
        except Exception as dontload:
            await message.edit(f"ɢᴇᴛᴛɪɴɢ ꜱᴄʀᴇᴇɴꜱʜᴏᴛ ꜰʀᴏᴍ ᴡᴇʙꜱɪᴛᴇ.....")
            full_link = f"https://mini.s-shot.ru/1920x1080/JPEG/1024/Z100/?{user_link}"
            await client.send_photo(message.chat.id, full_link, caption=f"** Screenshot of the page ** `{user_link}`")
        await message.delete()
    except Exception as error:
        await message.delete()
        await client.send_message(
            message.chat.id, f"**__» ᴛʜɪs ɪs ɴᴏᴛ ᴀ ᴠᴀʟɪᴅ ᴜʀʟ...__**"
        )
