from Imshivaexe.Database.gban import *
from pyrogram import Client, filters
from config import HANDLER as hl
from Imshivaexe import Bunny
from Imshivaexe.powers import get_id_and_args

@Bunny.on_message(filters.command("gban", hl) & filters.me)
async def ungban(client, message):
    try:
        id, args = await get_id_and_args(client, message)
    except:
        return await message.edit("`this is not a valid User..`")
    if await is_gbanned(id):
        return await message.edit("`According to my database this User already gbanned..`")
    await gban(id)
    await message.edit(f"**successfully gbanned** `{id}` !!")
    
@Bunny.on_message(filters.command("ungban", hl) & filters.me)
async def ungban(client, message):
    try:
        id, args = await get_id_and_args(client, message)
    except:
        return await message.edit("`this is not a valid User..`")
    if not await is_gbanned(id):
        return await message.edit("`According to my database this User haven't been gbanned..`")
    await ungban(id)
    await message.edit(f"**successfully Ungbanned** `{id}` !!")

@Bunny.on_message(group=11)
async def watcher(client, message):
    if not message.from_user:
        return
    id = message.from_user.id
    if not await is_gbanned(id):
        return
    try:
        await client.ban_chat_member(message.chat.id, id)
        return await message.reply("`User have been banned due to gban..`")
    except:
        return
