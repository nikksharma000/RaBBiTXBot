from Imshivaexe.Data.porn import PORN
import random
from config import HANDLER as hl, ALLOW_PORN
from pyrogram import Client, filters
from Imshivaexe import Bunny

@Bunny.on_message(filters.command(["pornspam", "ps"], hl) & filters.me)
async def pornspam(client, message):
  if not ALLOW_PORN:
    return await message.edit("`Porn spam is disabled now!!`")
  try:
    count = int(message.text.split()[1])
  except:
    return await message.edit(f"{hl}pornspam | {hl}ps [count]")
  for i in range(0, count):
    x = random.choice(PORN)
    if x[-3:] == "mp4":
        await client.send_animation(message.chat.id, x)
    else:
        await client.send_photo(message.chat.id, x)
