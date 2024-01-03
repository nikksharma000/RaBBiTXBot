import sys
import logging
from os import environ, execle, remove
from pyrogram import Client, filters
from pyrogram.types import Message
from config import hl
from Imshivaexe import Bunny

GEEK = None

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)

@Bunny.on_message(filters.command("restart", hl) & filters.me)
async def restart_bot(client, message: Message):
    try:
        msg = await message.edit("`Restarting bot...`")
        LOGGER(__name__).info("BOT SERVER RESTARTING....")
    except BaseException as err:
        LOGGER(__name__).info(f"{err}")
        return
    await msg.edit_text("**RaBBiTX has been restarted Successfully..||**\n\n")
    if GEEK is not None:
        GEEK.restart()
    else:
        args = [sys.executable, "-m", "Imshivaexe"]
        execle(sys.executable, *args, environ)
