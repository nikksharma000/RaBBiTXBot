from pyrogram import Client, enums, filters
from pyrogram.raw import functions
from pyrogram.types import Message
from Imshivaexe import Bunny
from config import HANDLER as hl
from Imshivaexe.Data.actions_store import commands
from Imshivaexe.powers import ReplyCheck
from asyncio import sleep

@Bunny.on_message(filters.command(list(commands), hl) & filters.me)
async def actions(client: Client, message: Message):
    geek = message.command[0]
    try:
        sec = int(message.command[1])
        if sec > 60:
            sec = 60
    except:
        sec = None
    await message.delete()
    action = commands[geek]
    try:
        if action != "screenshot":
            if sec and action != enums.ChatAction.CANCEL:
                await client.send_chat_action(chat_id=message.chat.id, action=action)
                await sleep(sec)
            else:
                return await client.send_chat_action(
                    chat_id=message.chat.id, action=action
                )
        else:
            for _ in range(sec if sec else 1):
                await client.send(
                    functions.messages.SendScreenshotNotification(
                        peer=await client.resolve_peer(message.chat.id),
                        reply_to_msg_id=0,
                        random_id=client.rnd_id(),
                    )
                )
                await sleep(0.3)
    except Exception as e:
        return await client.send_message(
            message.chat.id,
            f"**__๏ ᴇʀʀᴏʀ »__** `{e}`",
            reply_to_message_id=ReplyCheck(message),
        )
