from pyrogram import Client, filters, enums
from gtts import gTTS
from Imshivaexe import Bunny
from config import HANDLER as hl

def convert(txt):
    tts = gTTS(txt)
    x = "shiva.mp3"
    tts.save(x)
    return x

@Bunny.on_message(filters.command("tts", hl) & filters.me)
async def texttospeech(client, message):
    reply = message.reply_to_message
    if not reply:
        if len(message.command) < 2:
            return await message.edit("`reply to any message or give some text...`")
    
    if reply:
        if not reply.text and not reply.caption:
            return await message.edit("`text not found...`")
        txt = reply.text if reply.text else reply.caption
        path = convert(txt)
    else:
        txt = message.text.split(None, 1)[1]
        path = convert(txt)
    try:
        await message.delete()
    except:
        pass
    try:
        await client.send_chat_action(message.chat.id, enums.ChatAction.RECORD_AUDIO)
        await message.reply_voice(path)
        await client.send_chat_action(message.chat.id, enums.ChatAction.CANCEL)
    except:
        await client.send_chat_action(message.chat.id, enums.ChatAction.RECORD_AUDIO)
        await message.reply_audio(path)
        await client.send_chat_action(message.chat.id, enums.ChatAction.CANCEL)
