from pyrogram import Client, filters
from Imshivaexe import Bunny
from config import HANDLER as hl
from Imshivaexe.Data.truth import TRUTH
import random

@Bunny.on_message(filters.command("truth",  hl) & filters.me)
async def truth(client, message):
    msg = random.choice(TRUTH)
    await message.edit(msg)
