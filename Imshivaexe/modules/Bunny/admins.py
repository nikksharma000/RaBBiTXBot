import asyncio
from pyrogram import Client, filters
from pyrogram.errors import ChatAdminRequired
from pyrogram.types import ChatPermissions, ChatPrivileges, Message
from config import *
from Imshivaexe.powers import extract_user, extract_user_and_reason, list_admins
from config import HANDLER as hl
from Imshivaexe.Data.owners import DEVS
from Imshivaexe import Bunny

unmute_permissions = ChatPermissions(
    can_send_messages=True,
    can_send_media_messages=True,
    can_send_polls=True,
    can_change_info=False,
    can_invite_users=True,
    can_pin_messages=False,
)

@Bunny.on_message(filters.command(["kick", "shutup"], hl) & filters.me)
async def kick_user(client: Client, message: Message):
    user_id, reason = await extract_user_and_reason(message)
    bunny = await message.edit("`ρяσ¢єѕѕιиg...⚡`")
    bot = (await client.get_chat_member(message.chat.id, client.me.id)).privileges
    if not bot.can_restrict_members:
        return await bunny.edit("ɪ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ʀɪɢʜᴛs ᴛᴏ ᴋɪᴄᴋ ᴀɴʏᴏɴᴇ..!!")
    if not user_id:
        return await bunny.edit("ʏᴏᴜ'ʀᴇ ɢᴏɪɴɢ ᴛᴏ ɴᴇᴇᴅ ᴛᴏ sᴘᴇᴄɪғʏ ᴀ ᴜsᴇʀ..!!")
    if user_id == client.me.id:
        return await bunny.edit("ʏᴇᴀʜʜʜ, ɪ'ᴍ ɴᴏᴛ ɢᴏɪɴɢ ᴛᴏ ᴋɪᴄᴋ ᴍʏsᴇʟғ..!!")
    if user_id == DEVS:
        return await bunny.edit("ɪ ᴄᴀɴ'ᴛ ᴋɪᴄᴋ ʜɪᴍ ᴄᴏᴢ ʜᴇ ɪs ᴋɪɴɢ ᴏғ ᴛᴇʟᴇɢʀᴀᴍ..!!")
    if user_id in (await list_admins(client, message.chat.id)):
        return await bunny.edit("ɪᴍ ɴᴏᴛ ɢᴏɴɴᴀ ᴋɪᴄᴋ ᴀɴ ᴀᴅᴍɪɴ..!! ᴛʜᴏᴜɢʜ ɪ ʀᴇᴄᴋᴏɴ ɪᴛ'ᴅ ʙᴇ ᴘʀᴇᴛᴛʏ ғᴜɴɴʏ..!!")
    mention = (await client.get_users(user_id)).mention
    msg = f"""
**__๏ ᴋɪᴄᴋᴇᴅ ᴜsᴇʀ »__** {mention}
**__๏ ᴋɪᴄᴋᴇᴅ ʙʏ »__** {message.from_user.mention if message.from_user else 'Anon'}"""
    if message.command[0][0] == "d":
        await message.reply_to_message.delete()
    if reason:
        msg += f"\n**__๏ ʀᴇᴀsᴏɴ »__** `{reason}`"
    try:
        await message.chat.ban_member(user_id)
        await bunny.edit(msg)
        await asyncio.sleep(1)
        await message.chat.unban_member(user_id)
    except ChatAdminRequired:
        return await bunny.edit("ɪ'ᴍ ɴᴏᴛ ᴀᴅᴍɪɴ ʜᴇʀᴇ..!!")

@Bunny.on_message(filters.group & filters.command("ban", hl) & filters.me)
async def member_ban(client: Client, message: Message):
    user_id, reason = await extract_user_and_reason(message, sender_chat=True)
    bunny = await message.edit("`ρяσ¢єѕѕιиg...⚡`")
    bot = (await client.get_chat_member(message.chat.id, client.me.id)).privileges
    if not bot.can_restrict_members:
        return await bunny.edit("ɪ ᴅᴏɴᴛ ʜᴀᴠᴇ ᴇɴᴏᴜɢʜ ʀɪɢʜᴛs ᴛᴏ ʙᴀɴ ᴀɴʏᴏɴᴇ..!!")
    if not user_id:
        return await bunny.edit("ʏᴏᴜ'ʀᴇ ɢᴏɪɴɢ ᴛᴏ ɴᴇᴇᴅ ᴛᴏ sᴘᴇᴄɪғʏ ᴀ ᴜsᴇʀ...!!")
    if user_id == client.me.id:
        return await bunny.edit("ʏᴏᴜ ᴋɴᴏᴡ ᴡʜᴀᴛ ɪᴍ ɴᴏᴛ ɢᴏɪɴɢ ᴛᴏ ᴅᴏ? ʙᴀɴ ᴍʏsᴇʟғ..!!")
    if user_id in DEVS:
        return await bunny.edit("ɪ ᴄᴀɴ'ᴛ ʙᴀɴ ʜɪᴍ ᴄᴏᴢ ʜᴇ ɪs ᴋɪɴɢ ᴏғ ᴛᴇʟᴇɢʀᴀᴍ..!!__")
    if user_id in (await list_admins(client, message.chat.id)):
        return await bunny.edit("ᴡʜʏ ᴡᴏᴜʟᴅ I ʙᴀɴ ᴀɴ ᴀᴅᴍɪɴ? ᴛʜᴀᴛ sᴏᴜɴᴅs ʟɪᴋᴇ ᴀ ᴘʀᴇᴛᴛʏ ᴅᴜᴍʙ ɪᴅᴇᴀ..!!")
    try:
        mention = (await client.get_users(user_id)).mention
    except IndexError:
        mention = (
            message.reply_to_message.sender_chat.title
            if message.reply_to_message
            else "Anon"
        )
    msg = (
        f"**__๏ ʙᴀɴɴᴇᴅ ᴜsᴇʀ »__** {mention}\n"
        f"**__๏ ʙᴀɴɴᴇᴅ ʙʏ »__** {message.from_user.mention if message.from_user else 'Anon'}\n"
    )
    if message.command[0][0] == "d":
        await message.reply_to_message.delete()
    if reason:
        msg += f"**__๏ ʀᴇᴀsᴏɴ »__** {reason}"
    await message.chat.ban_member(user_id)
    await bunny.edit(msg)

@Bunny.on_message(filters.group & filters.command("unban", hl) & filters.me)
async def member_unban(client: Client, message: Message):
    reply = message.reply_to_message
    bunny = await message.edit("`ρяσ¢єѕѕιиg...⚡`")
    bot = (await client.get_chat_member(message.chat.id, client.me.id)).privileges
    if not bot.can_restrict_members:
        return await bunny.edit("ɪ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴇɴᴏᴜɢʜ ʀɪɢʜᴛs ᴛᴏ ᴜɴʙᴀɴ ᴀɴʏᴏɴᴇ..!!")
    if reply and reply.sender_chat and reply.sender_chat != message.chat.id:
        return await bunny.edit("ɪ ᴄᴀɴ'ᴛ ᴜɴʙᴀɴ ᴀ ᴄʜᴀɴɴᴇʟ..!!")

    if len(message.command) == 2:
        user = message.text.split(None, 1)[1]
    elif len(message.command) == 1 and reply:
        user = message.reply_to_message.from_user.id
    else:
        return await bunny.edit(
            "ʏᴏᴜ'ʀᴇ ɢᴏɪɴɢ ᴛᴏ ɴᴇᴇᴅ ᴛᴏ sᴘᴇᴄɪғʏ ᴀ ᴜsᴇʀ..!!"
        )
    await message.chat.unban_member(user)
    umention = (await client.get_users(user)).mention
    await bunny.edit(f"**__๏ ᴜɴʙᴀɴɴᴇᴅ »__** {umention}")

@Bunny.on_message(filters.command(["pin", "unpin"], hl) & filters.me)
async def pin_message(client: Client, message):
    if not message.reply_to_message:
        return await message.edit("ʏᴏᴜ ɴᴇᴇᴅ ᴛᴏ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ ᴛᴏ ᴘɪɴ ɪᴛ..!!")
    bunny = await message.edit("`ρяσ¢єѕѕιиg...⚡`")
    bot = (await client.get_chat_member(message.chat.id, client.me.id)).privileges
    if not bot.can_pin_messages:
        return await bunny.edit("ɪ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴇɴᴏᴜɢʜ ʀɪɢʜᴛs ᴛᴏ ᴘɪɴ ᴍᴇssᴀɢᴇs..!!")
    r = message.reply_to_message
    if message.command[0][0] == "u":
        await r.unpin()
        return await bunny.edit(
            f"๏ ᴜɴᴘɪɴɴᴇᴅ [ᴛʜɪs]({r.link}) ᴍᴇssᴀɢᴇ..!!",
            disable_web_page_preview=True,
        )
    await r.pin(disable_notification=True)
    await bunny.edit(
        f"๏ ᴘɪɴɴᴇᴅ [ᴛʜɪs]({r.link}) ᴍᴇssᴀɢᴇ..!!",
        disable_web_page_preview=True,
    )

@Bunny.on_message(filters.command("mute", hl) & filters.me)
async def mute(client: Client, message: Message):
    user_id, reason = await extract_user_and_reason(message)
    bunny = await message.edit("`ρяσ¢єѕѕιиg...⚡`")
    bot = (await client.get_chat_member(message.chat.id, client.me.id)).privileges
    if not bot.can_restrict_members:
        return await bunny.edit("ɪ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴇɴᴏᴜɢʜ ʀɪɢʜᴛs ᴛᴏ ᴍᴜᴛᴇ ᴀɴʏᴏɴᴇ..!!")
    if not user_id:
        return await bunny.edit("ʏᴏᴜ'ʀᴇ ɢᴏɪɴɢ ᴛᴏ ɴᴇᴇᴅ ᴛᴏ sᴘᴇᴄɪғʏ ᴀ ᴜsᴇʀ..!!")
    if user_id == client.me.id:
        return await bunny.edit("ʏᴏᴜ ᴋɴᴏᴡ ᴡʜᴀᴛ ɪᴍ ɴᴏᴛ ɢᴏɪɴɢ ᴛᴏ ᴅᴏ? ᴍᴜᴛᴇ ᴍʏsᴇʟғ..!!")
    if user_id in DEVS:
        return await bunny.edit("ɪ ᴄᴀɴ'ᴛ ᴍᴜᴛᴇ ʜɪᴍ ᴄᴏᴢ ʜᴇ ɪs ᴋɪɴɢ ᴏғ ᴛᴇʟᴇɢʀᴀᴍ..!!")
    if user_id in (await list_admins(client, message.chat.id)):
        return await bunny.edit("ᴇʜʜʜ, ɪᴅ ʀᴀᴛʜᴇʀ ɴᴏᴛ ɢᴇᴛ ɪɴᴠᴏʟᴠᴇᴅ ɪɴ ᴍᴜᴛɪɴɢ ᴀɴ ᴀᴅᴍɪɴ. ɪ'ᴡɪʟʟ sᴛɪᴄᴋ ᴛᴏ ᴍᴜᴛɪɴɢ ɴᴏʀᴍᴀʟ ᴜsᴇʀs, ᴛʜᴀɴᴋs..!!")
    mention = (await client.get_users(user_id)).mention
    msg = (
        f"**__๏ ᴍᴜᴛᴇᴅ ᴜsᴇʀ »__** {mention}\n"
        f"**__๏ ᴍᴜᴛᴇᴅ ʙʏ »__** {message.from_user.mention if message.from_user else 'Anon'}\n"
    )
    if reason:
        msg += f"**__๏ ʀᴇᴀsᴏɴ  »__** {reason}"
    await message.chat.restrict_member(user_id, permissions=ChatPermissions())
    await bunny.edit(msg)


@Bunny.on_message(
    filters.group & filters.command(["setchatphoto", "setgpic"], hl) & filters.me
)
async def set_chat_photo(client: Client, message: Message):
    zuzu = (await client.get_chat_member(message.chat.id, client.me.id)).privileges
    can_change_admin = zuzu.can_change_info
    can_change_member = message.chat.permissions.can_change_info
    if not (can_change_admin or can_change_member):
        await message.edit_text("ʏᴏᴜ ᴅᴏɴᴛ ʜᴀᴠᴇ ᴇɴᴏᴜɢʜ ʀɪɢʜᴛs ᴛᴏ ᴄʜᴀɴɢᴇ ɢʀᴏᴜᴘ ᴘғᴘ..!!")
    if message.reply_to_message:
        if message.reply_to_message.photo:
            await client.set_chat_photo(
                message.chat.id, photo=message.reply_to_message.photo.file_id
            )
            return
    else:
        await message.edit_text("ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴘʜᴏᴛᴏ ᴛᴏ sᴇᴛ ɪᴛ ᴀs ɢʀᴏᴜᴘ ᴘғᴘ..!!")

@Bunny.on_message(filters.group & filters.command("unmute", hl) & filters.me)
async def unmute(client: Client, message: Message):
    user_id = await extract_user(message)
    bunny = await message.edit("`ρяσ¢єѕѕιиg...⚡`")
    bot = (await client.get_chat_member(message.chat.id, client.me.id)).privileges
    if not bot.can_restrict_members:
        return await bunny.edit("ɪ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴇɴᴏᴜɢʜ ʀɪɢʜᴛs ᴛᴏ ᴜɴᴍᴜᴛᴇ ᴀɴʏᴏɴᴇ..!!")
    if not user_id:
        return await bunny.edit("ʏᴏᴜ'ʀᴇ ɢᴏɪɴɢ ᴛᴏ ɴᴇᴇᴅ ᴛᴏ sᴘᴇᴄɪғʏ ᴀ ᴜsᴇʀ..!!")
    await message.chat.restrict_member(user_id, permissions=unmute_permissions)
    umention = (await client.get_users(user_id)).mention
    await bunny.edit(f"**__๏ ᴜɴᴍᴜᴛᴇᴅ __** {umention}")



@Bunny.on_message(filters.group & filters.command(["promote", "fullpromote"], hl) & filters.me)
async def promotte(client: Client, message: Message):
    user_id = await extract_user(message)
    umention = (await client.get_users(user_id)).mention
    bunny = await message.edit("`ρяσ¢єѕѕιиg...⚡`")
    if not user_id:
        return await bunny.edit("ʏᴏᴜ'ᴇ ɢᴏɪɴɢ ᴛᴏ ɴᴇᴇᴅ ᴛᴏ sᴘᴇᴄɪғʏ ᴀ ᴜsᴇʀ..!!")
    bot = (await client.get_chat_member(message.chat.id, client.me.id)).privileges
    if not bot.can_promote_members:
        return await bunny.edit("ɪ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴇɴᴏᴜɢʜ ʀɪɢʜᴛs ᴛᴏ ᴘʀᴏᴍᴏᴛᴇ ᴀɴʏᴏɴᴇ..!!")
    if message.command[0][0] == "f":
        await message.chat.promote_member(
            user_id,
            privileges=ChatPrivileges(
                can_manage_chat=True,
                can_delete_messages=True,
                can_manage_video_chats=True,
                can_restrict_members=True,
                can_change_info=True,
                can_invite_users=True,
                can_pin_messages=True,
                can_promote_members=True,
            ),
        )
        return await bunny.edit(f"**__๏ ғᴜʟʟʏ ᴘʀᴏᴍᴏᴛᴇᴅ »__** {umention}")
    if message.command[0][0] == "p":
        await message.chat.promote_member(
            user_id,     
            privileges=ChatPrivileges(
                can_manage_chat=True,
                can_delete_messages=True,
                can_manage_video_chats=True,
                can_restrict_members=True,
                can_change_info=True,
                can_invite_users=True,
                can_pin_messages=True,
                can_promote_members=False,
            ),
        )
        return await bunny.edit(f"**__๏ ᴘʀᴏᴍᴏᴛᴇᴅ »__** {umention}")

@Bunny.on_message(filters.group & filters.command("demote", hl) & filters.me)
async def demote(client: Client, message: Message):
    user_id = await extract_user(message)
    bunny = await message.edit("`ρяσ¢єѕѕιиg...⚡`")
    if not user_id:
        return await bunny.edit("ʏᴏᴜ ɢᴏɪɴɢ ᴛᴏ ɴᴇᴇᴅ ᴛᴏ sᴘᴇᴄɪғʏ ᴀ ᴜsᴇʀ..!!")
    if user_id == client.me.id:
        return await bunny.edit("ɪ ᴀᴍ ɴᴏᴛ ɢᴏɪɴɢ ᴛᴏ ᴅᴇᴍᴏᴛᴇ ᴍʏsᴇʟғ..!!")
    await message.chat.promote_member(
        user_id,
        privileges=ChatPrivileges(
            can_manage_chat=False,
            can_delete_messages=False,
            can_manage_video_chats=False,
            can_restrict_members=False,
            can_change_info=False,
            can_invite_users=False,
            can_pin_messages=False,
            can_promote_members=False,
        ),
    )
    umention = (await client.get_users(user_id)).mention
    await bunny.edit(f"**__๏ ᴅᴇᴍᴏᴛᴇᴅ »**__ {umention}")
