from pyrogram import Client, filters
from Imshivaexe import Bunny
from config import HANDLER as hl

@Bunny.on_message(filters.command("repo", hl) & filters.me)
async def repo(client, message):
    msg = f"""
    ** RaBBiTX UserBot **

    ๏ **__GitHub**__ » [click here](https://github.com/RaBBiTUserBot) 
    ๏ **__Support**__ » [click here](https://t.me/Robotxsupport) 
    ๏ **__Updates**__ » [click here](https://t.me/Robotxupdates)

    **By © @ITZ_RaBBiTX**
    """
    await message.edit(msg)
