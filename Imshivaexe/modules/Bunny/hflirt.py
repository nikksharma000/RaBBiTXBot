from pyrogram import Client, filters
from Imshivaexe import Bunny
from config import HANDLER as hl
from Imshivaexe.Data.hflirt import HINDI
import random

@Bunny.on_message(filters.command("hflirt",  hl) & filters.me)
async def eflirt(client, message):
    x = client.me.mention
    msg = random.choice(HINDI)
    msg += f"\n\n ✍🏻 {x}"
    await message.edit(msg)
