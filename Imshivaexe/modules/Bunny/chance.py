from pyrogram import Client, filters
import random
from config import HANDLER as hl
from Imshivaexe import Bunny

@Bunny.on_message(filters.command("chance",  hl) & filters.me)
async def chance(client, message):
    text = message.text.split(hl + "chance ", maxsplit=1)[1]
    await message.edit(f"{text}\n\n**__๏ ᴄʜᴀɴᴄᴇ »__** {random.randint(1, 100)}%")
