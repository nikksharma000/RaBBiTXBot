from Imshivaexe.Data.replyraid import REPLYRAID
import random
from config import HANDLER as hl
import asyncio
from Imshivaexe.Database.replyraid import *
from pyrogram import Client, filters 
from Imshivaexe import Bunny

@Bunny.on_message(filters.command("replyraid", hl) & filters.me)
async def replyraid(client, message):
    try:
        if message.reply_to_message:
            id = message.reply_to_message.from_user.id
        else:
            x = message.text.split()[1]
            if str(x)[0] == "@":
                id = (await client.get_users(x)).id
            else:
                id = int(x)
    except:
        return await message.edit(f"`{hl}replyraid [ɪᴅ|ᴜsᴇʀɴᴀᴍᴇ|ʀᴇᴘʟʏ]`")
    if await is_rr(id):
        return await message.edit("`ᴀᴄᴄᴏʀᴅɪɴɢ ᴛᴏ ᴍʏ ᴅᴀᴛᴀʙᴀsᴇ ᴛʜɪs ᴜsᴇʀ ɪs ᴀʟʀᴇᴀᴅʏ ɪɴ ʀᴀɪᴅʟɪsᴛ..!!`")
    await add_rr(id)
    return await message.edit(f"`<code>{id}</code> sᴜᴄᴄᴇssғᴜʟʟʏ ᴀᴅᴅᴇᴅ ɪɴ ʀᴀɪᴅʟɪsᴛ..!!`")
 
@Bunny.on_message(filters.command("dreplyraid", hl) & filters.me)
async def dreplyraid(client, message):
    try:
        if message.reply_to_message:
            id = message.reply_to_message.from_user.id
        else:
            x = message.text.split()[1]
            if str(x)[0] == "@":
                id = (await _.get_users(x)).id
            else:
                id = int(x)
    except:
        return await message.edit(f"`{hl}dreplyraid [ɪᴅ|ᴜsᴇʀɴᴀᴍᴇ|ʀᴇᴘʟʏ]`")
    if not await is_rr(id):
        return await message.edit("`ᴀᴄᴄᴏʀᴅɪɴɢ ᴛᴏ ᴍʏ ᴅᴀᴛᴀʙᴀsᴇ ᴛʜɪs ᴜsᴇʀ ɪs ɴᴏᴛ ɪɴ ʀᴀɪᴅʟɪsᴛ..!!`")
    await del_rr(id)
    return await message.edit(f"`<code>{id}</code> sᴜᴄᴄᴇssғᴜʟʟʏ ʀᴇᴍᴏᴠᴇᴅ ғʀᴏᴍ ʀᴀɪᴅʟɪsᴛ..!!`")

@Bunny.on_message(group=2)
async def raids(client, message):
    if message.from_user:
        if await is_rr(message.from_user.id):
            await message.reply(random.choice(REPLYRAID))
