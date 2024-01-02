from pyrogram import Client, filters
from Imshivaexe.Database.pm import *
from Imshivaexe.powers import get_id
from config import HANDLER as hl
from config import PM_PIC
from Imshivaexe import Bunny

RBX = PM_PIC
pm_watcher = 5

TEXT = """
╭─────────────────๏
╰๏         ⚡ яαввιтχ ⚡
╭─────────────────๏
╰๏ ᴏᴡɴᴇʀ » {}
╭─────────────────๏
๏ ᴛʜɪs ɪs ʀᴀʙʙɪᴛx ᴘᴍ sᴇᴄᴜʀɪᴛʏ
╰─────────────────๏    
    ʜᴇʏᴀ !! 
    ɪғ ʏᴏᴜ sᴘᴀᴍ ʜᴇʀᴇ ᴡɪᴛʜᴏᴜᴛ ᴍʏ
    ᴏᴡɴᴇʀ's ᴀᴘᴘʀᴏᴠᴀʟ ʏᴏᴜ ᴡɪʟʟ ʙᴇ
    ʙʟᴏᴄᴋᴇᴅ. 
╭─────────────────๏
╰๏ ᴡᴀʀɴ ʟɪᴍɪᴛs » {}
╭─────────────────๏
╰๏ ʏᴏᴜʀ ᴡᴀʀɴs » {}
╭─────────────────๏
๏        🔥『 [яαввιтχ](https://t.me/Robotxupdates) 』🔥
╰─────────────────๏
"""

@Bunny.on_message(filters.command("pmpermit", hl) & filters.me)
async def pmpermit(client, message):
    x = await is_pm_on()
    try:
        tg = message.text.split()[1].lower()
    except:
        return await message.edit(f"`{hl}pmpermit [on | off]`")
    if not tg in ["on", "off"]:
        return await message.edit(f"`{hl}pmpermit [on | off]`")
    if tg == "on":
        if x:
            return await message.edit("`According to my database pmpermit already enabled..!!`")
        await toggle_pm()
        if await limit() == 0:
            await update_warns(3)
        return await message.edit("`Pmpermit successfully enabled..!!`")
    if not x:
        return await message.edit("`According to my database pmpermit is not enabled..!!`")
    await toggle_pm()
    return await message.edit("`Pmpermit successfully disabled..!!`")

@Bunny.on_message(filters.command(["approve", "disapprove", "a", "da", "allow", "disallow"], hl) & filters.me)
async def appr_dis(client, message):
    if str(message.chat.id)[0] == "-":
        try:
            id = await get_id(_, message)
        except:
            return await message.edit("`For approve user in group u want to give me I'd or reply that user..`")
    else:
        id = message.chat.id
    tg = message.text.split()[0][1]
    x = await is_approved(id)
    if tg == "d":
        if not x:
            return await message.edit("`According to my database this user is not approved..!!`")
        await disapprove(id)
        return await message.edit("`User successfully disapproved to pm..!!`")
    if x:
        return await message.edit("`According to my database user already approved..!!`")
    await approve(id) 
    await reset_warns(id)
    return await message.edit("`User successfully approved to pm..!!`")

@Bunny.on_message(filters.command("setwarns", hl) & filters.me)
async def setwarn(client, message):
    try:
        count = int(message.text.split()[1])
    except:
        return await message.edit(f"{hl}setwarns [value]")
    if count == 0:
        return await message.edit("`Give me value to set warns..!!`")
    await update_warns(count)
    await message.edit(f"`Dm warns successfully set to {count}..!!`")
    
@Bunny.on_message(filters.private, group=pm_watcher)
async def wtch(client, message):
    user_ = message.from_user
    if message.from_user.id == client.me.id:
        return
    if not await is_pm_on():
        return
    if user_.is_bot:
        return
    if await is_approved(message.from_user.id):
        return
    await add_warn(message.from_user.id)
    if await limit() <= await get_warns(message.from_user.id):
        await message.reply("Spammer detected and blocked successfully..!!")
        await reset_warns(message.from_user.id)
        return await client.block_user(message.from_user.id)
    await message.reply_photo(RBX, caption=TEXT.format((await client.get_me()).first_name, await limit(), await get_warns(message.from_user.id)))
