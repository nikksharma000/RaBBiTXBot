from Imshivaexe.powers import extract_user
from pyrogram import Client, filters
from config import HANDLER as hl
from Imshivaexe import Bunny
from pyrogram.types import Message

@Bunny.on_message(filters.command(["block"], hl) & filters.me)
async def block(client: Client, message: Message):
    user_id = await extract_user(message)
    bunny = await message.edit("`ρяσ¢єѕѕιиg...⚡`")
    if not user_id:
        return await message.edit(
            "ɢɪᴠᴇ ɪᴅ/ᴜsᴇʀɴᴀᴍᴇ ᴏʀ ʀᴇᴘʟʏ ᴛᴏ ᴜsᴇʀ ᴍᴇssᴀɢᴇ ᴛᴏ ʙʟᴏᴄᴋ..!!"
        )
    if user_id == client.me.id:
        return await bunny.edit("ɪ ᴄᴀɴ'ᴛ ʙʟᴏᴄᴋ ᴍʏsᴇʟғ ʟᴏʟ..!!")
    await client.block_user(user_id)
    geek = (await client.get_users(user_id)).mention
    await message.edit(f"__**๏ {geek} ʙʟᴏᴄᴋᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ**__")
