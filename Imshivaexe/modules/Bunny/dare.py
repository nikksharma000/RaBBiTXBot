from pyrogram import Client, filters
from Imshivaexe import Bunny
from config import HANDLER as hl
from Imshivaexe.Data.dare import DARE
import random

@Bunny.on_message(filters.command("dare",  hl) & filters.me)
async def dare(client, message):
    msg = random.choice(DARE)
    await message.edit(msg)
