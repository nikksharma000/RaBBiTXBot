import asyncio
from pyrogram import *
from pyrogram import filters
from pyrogram.errors import YouBlockedUser
from pyrogram.types import *
from config import HANDLER as hl
from Imshivaexe.powers import extract_user
from Imshivaexe import Bunny

@Bunny.on_message(filters.command(["sg", "sa", "sangmata"], hl) & filters.me)
async def sg(client: Client, message: Message):
    args = await extract_user(message)
    lol = await message.edit("`Processing...⚡`")
    if args:
        try:
            user = await client.get_users(args)
        except Exception:
            return await lol.edit(f"`ᴘʟᴇᴀsᴇ sᴘᴇᴄɪғʏ ᴀ ᴠᴀʟɪᴅ ᴜsᴇʀ..!!`")
    bot = "@SangMata_beta_bot"
    try:
        await client.send_message(bot, f"{user.id}")
    except YouBlockedUser:
        await client.unblock_user(bot)
        await client.send_message(bot, f"{user.id}")
    await asyncio.sleep(1)

    async for stalk in client.search_messages(bot, query="Name", limit=1):
        if not stalk:
            await message.edit_text("ᴛʜɪs ᴘᴇʀsᴏɴ ʜᴀs ɴᴇᴠᴇʀ ᴄʜᴀɴɢᴇᴅ ʜɪs ɴᴀᴍᴇ..!!")
            return
        elif stalk:
            await message.edit(stalk.text)
            await stalk.delete()

    async for stalk in client.search_messages(bot, query="Username", limit=1):
        if not stalk:
            return
        elif stalk:
            await message.reply(stalk.text)
            await stalk.delete()
