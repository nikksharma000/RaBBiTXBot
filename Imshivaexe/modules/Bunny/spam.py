from config import HANDLER as hl
import asyncio
from pyrogram import Client, filters
from Imshivaexe import Bunny

async def get_reply_and_args(message):
    reply = message.reply_to_message
    if not len(message.command) > 1:
        args = None
    else:
        args = message.text.split(None, 1)[1]
    if not reply:
        type = None 
    elif reply.photo:
        type = "photo"
    elif reply.video:
        type = "video"
    elif reply.animation:
        type = "animation"
    elif reply.document:
        type = "document"
    elif reply.audio:
        type = "audio"
    elif reply.voice:
        type = "voice"
    elif reply.sticker:
        type = "sticker"
    elif reply.text:
        type = "text"
    else:
        type = None
    if reply:
        if reply.caption:
            type += "-caption"
    return type, args

@Bunny.on_message(filters.command("spam", hl) & filters.me)
async def spam(client, message):
    reply = message.reply_to_message
    a, b = await get_reply_and_args(message)
    if not a and not b:
        return await message.edit(f"`{hl}spam [ʀᴇᴘʟʏ ᴏʀ ɢɪᴠᴇ sᴏᴍᴇ ᴛᴇxᴛ]`")
    if not b:
        return await message.edit(f"`{hl}spam [ᴄᴏᴜɴᴛ] [ᴛᴇxᴛ]`")
    if not a:
        try:
            count = int(b.split()[0])
        except:
            return await message.edit(f"`{hl}spam [ᴄᴏᴜɴᴛ] [ᴛᴇxᴛ]`")
        try:
            txt = b.split(None, 1)[1]
        except:
            return await message.edit(f"`{hl}spam [ᴄᴏᴜɴᴛ] [ᴛᴇxᴛ]`")
        for u in range(0, count):
            await client.send_message(message.chat.id, txt)
        return
    if a[-7:] == "caption":
        caption = True
        txt = reply.caption
    else:
        caption = False
    type = a.split("-")[0]
    try:
        count = int(b.split()[0])
    except:
        return await message.reply(f"`{hl}spam [ᴄᴏᴜɴᴛ] [ᴛᴇxᴛ]`")
    if not caption:
        try:
            txt = b.split(None, 1)[1]
            caption = True
        except:
            pass
    blank = ""
    if type == "photo":
        id = reply.photo.file_id
        for u in range(0, count):
            await client.send_photo(message.chat.id, id, caption=f"{txt if caption else blank}")
    elif type == "video":
        id = reply.video.file_id
        for u in range(0, count):
            await client.send_video(message.chat.id, id, caption=f"{txt if caption else blank}")
    elif type == "document":
        id = reply.document.file_id
        for u in range(0, count):
            await client.send_document(message.chat.id, id, caption=f"{txt if caption else blank}", force_document=True)
    elif type == "animation":
        id = reply.animation.file_id
        for u in range(0, count):
            await client.send_animation(message.chat.id, id, caption=f"{txt if caption else blank}")
    elif type == "voice":
        id = reply.voice.file_id
        for u in range(0, count):
            await client.send_voice(message.chat.id, id, caption=f"{txt if caption else blank}")
    elif type == "audio":
        id = reply.audio.file_id
        for u in range(0, count):
            await client.send_audio(message.chat.id, id, caption=f"{txt if caption else blank}")
    elif type == "text":
        id = reply.text
        for u in range(0, count):
            await client.send_message(message.chat.id, id)
    elif type == "sticker":
        id = reply.sticker.file_id
        for u in range(0, count):
            await client.send_sticker(message.chat.id, id)
