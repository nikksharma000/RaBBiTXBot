from pyrogram import Client, filters
from Imshivaexe import Bunny
from config import HANDLER as hl
from Imshivaexe.Data.eflirt import ENGLISH
import random

@Bunny.on_message(filters.command("eflirt",  hl) & filters.me)
async def eflirt(client, message):
    x = client.me.mention
    msg = random.choice(ENGLISH)
    msg += f"\n\n ✍🏻 {x}"
    await message.edit(msg)
