import asyncio
from pyrogram import Client, filters
from pyrogram.enums import ChatType, UserStatus
from pyrogram.types import Message
from config import HANDLER as hl
from config import LOGGER_ID
from Imshivaexe import Bunny

@Bunny.on_message(filters.me & filters.command("invite", hl))
async def invite(client: Client, message: Message):
    mg = await message.edit("`ᴀᴅᴅɪɴɢ ᴜsᴇʀs.. ᴘʟᴇᴀsᴇ ᴡᴀɪᴛ...`")
    user_s_to_add = message.text.split(" ", 1)[1]
    if not user_s_to_add:
        await mg.edit("__ɢɪᴠᴇ ᴍᴇ ᴜsᴇʀɴᴀᴍᴇ ᴛᴏ ᴀᴅᴅ ᴛʜᴀᴛ ᴍᴇᴍʙᴇʀs ʜᴇʀᴇ..!!__")
        return
    user_list = user_s_to_add.split(" ")
    try:
        await client.add_chat_members(message.chat.id, user_list, forward_limit=100)
    except BaseException as e:
        await mg.edit(f"__๏ ᴜɴᴀʙʟᴇ ᴛᴏ ᴀᴅᴅ ᴜsᴇʀs..!!__ \n\n**ᴇʀʀᴏʀ:** `{e}`")
        return
    await mg.edit(f"__๏ sᴜᴄᴇssғᴜʟʟʏ ᴀᴅᴅᴇᴅ {len(user_list)} ᴛᴏ ᴛʜɪs ɢʀᴏᴜᴘ..!!__")


@Bunny.on_message(filters.command(["inviteall"], hl) & filters.me)
async def invteall(client: Client, message: Message):
    bunny = await message.edit("`Processing...⚡`")
    text = message.text.split(" ", 1)
    queryy = text[1]
    chat = await client.get_chat(queryy)
    tgchat = message.chat
    await bunny.edit_text(f"__๏ ɪɴᴠɪᴛɪɴɢ ᴜsᴇʀs ғʀᴏᴍ {chat.username}...!!__")
    async for member in client.get_chat_members(chat.id):
        user = member.user
        sex = [
            UserStatus.ONLINE,
            UserStatus.OFFLINE,
            UserStatus.RECENTLY,
            UserStatus.LAST_WEEK,
        ]
        if user.status in sex:
            try:
                await client.add_chat_members(tgchat.id, user.id)
            except Exception as e:
                mg = await client.send_message(LOGGER_ID, f"**ᴇʀʀᴏʀ:** `{e}`")
                await asyncio.sleep(0.01)
                await mg.delete()


@Bunny.on_message(filters.command("invitelink", hl) & filters.me)
async def invitelink(client: Client, message: Message):
    bunny = await message.edit("`Processing...⚡`")
    if message.chat.type in [ChatType.GROUP, ChatType.SUPERGROUP]:
        message.chat.title
        try:
            link = await client.export_chat_invite_link(message.chat.id)
            await bunny.edit(f"**__๏ ɪɴᴠɪᴛᴇ ʟɪɴᴋ:__** {link}")
        except Exception:
            await bunny.edit("__๏ ᴅᴇɴɪᴇᴅ ᴘᴇʀᴍɪssɪᴏɴ__")
