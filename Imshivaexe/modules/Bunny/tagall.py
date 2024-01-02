from pyrogram import Client, filters
from pyrogram.types import Message
from Imshivaexe.powers import get_arg
from asyncio import sleep
from config import HANDLER as hl
from Imshivaexe import Bunny

spam_chats = []

@Bunny.on_message(filters.command("tagall", hl) & filters.me)
async def mentions(client: Client, message: Message):
    await message.delete()
    chat_id = message.chat.id
    direp = message.reply_to_message
    args = get_arg(message)
    if not direp and not args:
        return await message.reply(f"» ɢɪᴠᴇ  ᴀ ᴍᴇssᴀɢᴇ ᴏʀ ʀᴇᴘʟʏ ᴛᴏ ᴀɴʏ ᴍᴇssᴀɢᴇ..!!\n\n**๏ ᴇxᴀᴍᴘʟᴇ** » `{hl}tagall ʜʟᴡᴡ ᴇᴠᴇʀʏᴏɴᴇ` !!")
    spam_chats.append(chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.get_chat_members(chat_id):
        if not chat_id in spam_chats:
            break
        usrnum += 1
        usrtxt += f"[{usr.user.first_name}](tg://user?id={usr.user.id}), "
        if usrnum == 5:
            if args:
                txt = f"{args}\n{usrtxt}"
                await client.send_message(chat_id, txt)
            elif direp:
                await direp.reply(usrtxt)
            await sleep(2)
            usrnum = 0
            usrtxt = ""
    try:
        spam_chats.remove(chat_id)
    except:
        pass


@Bunny.on_message(filters.command("cancel", hl) & filters.me)
async def canceltagall(client: Client, message: Message):
    if not message.chat.id in spam_chats:
        return await message.edit("» ɪᴍ ɴᴏᴛ ᴛᴀɢɢɪɴɢ ᴀɴʏᴏɴᴇ ʜᴇʀᴇ sᴏ ɪ ᴄᴀɴ'ᴛ ᴄᴀɴᴄᴇʟ ᴇɪᴛʜᴇʀ..!!")
    else:
        try:
            spam_chats.remove(message.chat.id)
        except:
            pass
        return await message.edit("**__๏ sᴜᴄᴄᴇssғᴜʟʟʏ ᴄᴀɴᴄᴇʟ ᴛᴀɢɪɴɢ ᴍᴇᴍʙᴇʀs..!!⚡__**")
