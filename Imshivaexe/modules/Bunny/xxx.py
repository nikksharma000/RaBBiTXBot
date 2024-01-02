import os
from pyrogram import Client, filters
from config import HANDLER as hl
from pyrogram.types import *
from Imshivaexe import Bunny

@Bunny.on_message(filters.command("save",  hl) & filters.private & filters.me)
async def self_media(client, message):
    replied = message.reply_to_message
    if not replied:
        return
    if not (replied.photo or replied.video):
        return
    fuck = await client.download_media(replied)
    await client.send_document("me", fuck)
    os.remove(fuck)
