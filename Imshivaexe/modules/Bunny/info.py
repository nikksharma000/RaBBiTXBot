import os
from pyrogram import Client, filters
from Imshivaexe import Bunny
from config import HANDLER as hl

def user(user):
    text = "--**User Details:**--\n"
    text += f"\n**๏ First Name:** `{user.first_name}`"
    text += f"\n\n**๏ Last Name:** `{user.last_name},`" if user.last_name else ""
    text += f"\n\n**๏ User Id:** `{user.id}`"
    text += f"\n\n**๏ Username:** @{user.username}" if user.username else ""
    text += f"\n\n**๏ User Link:** {user.mention}" if user.username else ""
    text += f"\n\n**๏ DC ID:** `{user.dc_id}`" if user.dc_id else ""
    text += f"\n\n**๏ Is Deleted:** True" if user.is_deleted else ""
    text += f"\n\n**๏ Is Bot:** True" if user.is_bot else ""
    text += f"\n\n**๏ Is Verified:** True" if user.is_verified else ""
    text += f"\n\n**๏ Is Restricted:** True" if user.is_verified else ""
    text += f"\n\n**๏ Is Scam:** True" if user.is_scam else ""
    text += f"\n\n**๏ Is Fake:** True" if user.is_fake else ""
    text += f"\n\n**๏ Is Support:** True" if user.is_support else ""
    text += f"\n\n**๏ Language Code:** {user.language_code}" if user.language_code else ""
    text += f"\n\n**๏ Status:** {user.status}" if user.status else ""
    return text


def chat(chat):
    text = "--**Chat Details**--\n" 
    text += f"\n\n**๏ Title:** `{chat.title}`"
    text += f"\n\n**๏ Chat ID:** `{chat.id}`"
    text += f"\n\n**๏ Username:** @{chat.username}" if chat.username else ""
    text += f"\n\n**๏ Type:** `{chat.type}`"
    text += f"\n\n**๏ DC ID:** `{chat.dc_id}`"
    text += f"\n\n**๏ Is Verified:** True" if chat.is_verified else ""
    text += f"\n\n**๏ Is Restricted:** True" if chat.is_verified else ""
    text += f"\n\n**๏ Is Creator:** True" if chat.is_creator else ""
    text += f"\n\n**๏ Is Scam:** True" if chat.is_scam else ""
    text += f"\n\n**๏ Is Fake:** True" if chat.is_fake else ""
    return text


@Bunny.on_message(filters.command("info",  hl) & filters.me)
async def info(client, message):
    if (not message.reply_to_message) and ((not message.forward_from) or (not message.forward_from_chat)):
        info = user(message.from_user)
    elif message.reply_to_message and message.reply_to_message.forward_from:
        info = user(message.reply_to_message.forward_from)
    elif message.reply_to_message and message.reply_to_message.forward_from_chat:
        info = chat(message.reply_to_message.forward_from_chat)
    elif (message.reply_to_message and message.reply_to_message.from_user) and (not message.forward_from or not message.forward_from_chat):
        info = user(message.reply_to_message.from_user)
    else:
        return
    try:
        await message.edit(info)
    except Exception as error:
        await message.edit(error)
