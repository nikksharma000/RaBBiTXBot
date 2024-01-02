from Imshivaexe.powers import extract_user
from pyrogram import Client, filters
from config import HANDLER as hl
from Imshivaexe import Bunny
from pyrogram.types import Message


@Bunny.on_message(filters.command(["setbio"], hl) & filters.me)
async def set_bio(client: Client, message: Message):
    bunny = await message.edit("`Processing . . .`")
    if len(message.command) == 1:
        return await bunny.edit("Provide text to set as bio..!!")
    elif len(message.command) > 1:
        bio = message.text.split(None, 1)[1]
        try:
            await client.update_profile(bio=bio)
            await bunny.edit(f"**Successfully Changed your BIO to..!!** `{bio}`")
        except Exception as e:
            await bunny.edit(f"**ERROR:** `{e}`")
    else:
        return await bunny.edit("Provide text to set as bio..!!")
