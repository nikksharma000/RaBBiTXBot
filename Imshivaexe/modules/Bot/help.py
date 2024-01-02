from pyrogram.types import InlineKeyboardButton as IKB, InlineKeyboardMarkup as IKM
from config import HANDLER as hl
import time
from pyrogram import Client, filters
from Imshivaexe import Bot
from config import HELP_PIC
from Imshivaexe import Bunny
from pyrogram.types import InlineQueryResultPhoto as IQRP

PIC = HELP_PIC

HELP_TEXT = "**๏ ᴛʜɪs ɪs ᴛʜᴇ ʜᴇʟᴘ ᴍeɴᴜ ᴏғ ʀᴀʙʙɪᴛx ᴜsᴇʀʙᴏᴛ**\n\n**๏ __RaBBiTX UserBot loaded with 150+ Commands 🍷**__\n\n๏ **__By © @ITZ_RaBBiTX** 🥂\n\n**๏ page** ~ `1/2`"
HELP_TEXTT = "**๏ ᴛʜɪs ɪs ᴛʜᴇ ʜᴇʟᴘ ᴍeɴᴜ ᴏғ ʀᴀʙʙɪᴛx ᴜsᴇʀʙᴏᴛ**\n\n**๏ __RaBBiTX UserBot loaded with 150+ Commands 🍷**__\n\n๏ **__By © @ITZ_RaBBiTX** 🥂\n\n**๏ page** ~ `2/2`"

ADMINS_MSG = f"""
**Admins commands**

๏ `{hl}ban` » to ban anyone in gc...

๏ `{hl}unban` » to unban anyone in gc...

๏ `{hl}mute` » to mute anyone in gc...

๏ `{hl}unmute` » to unmute anyone in gc..!! 

๏ `{hl}kick` » to kick anyone in gc..!! 

๏ `{hl}pin` » to pin any message..!! 

๏ `{hl}unpin` » to unpin message..!! 

๏ `{hl}promote` » to promote anyone..!! 

๏ `{hl}demote` » to demote anyone..!!

๏ `{hl}setgpic` » to set pfp in gc..!!
"""

EXTRA_MSG = f"""
**Extra Commands** 

๏ `{hl}ping` » to check bot ping and uptime..!!

๏ `{hl}alive` » to check bot alive or not..!!

๏ `{hl}repo` » to get bot repo..!!

๏ `{hl}startvc` » to start vc in current chat..!!

๏ `{hl}id` » to get chat and replyed user's user_id..!!

๏ `{hl}sg` » yo get name history of replyed user..!!

๏ `{hl}gitinfo` <username> » to get git ACC information..!!
"""

INVITE_MSG = f"""
**Invite Commands**

๏ `{hl}invite` » to add members in gc by his/her username..!!

๏ `{hl}invitelink` » to get any group chat link..!!

๏ `{hl}inviteall` » to invite all members of other gc to ur gc..!!

"""

SPAM_MSG = f"""
**Spam Commands**

๏ `{hl}spam` » to spam messages by count..!!

๏ `{hl}banall` » to ban all members of current chats..!!

๏ `{hl}raid` » to abuse anyone..!!

๏ `{hl}replyraid` » to activate replyraid on anyone..!!

๏ `{hl}dreplyraid` » to deactivate replyraid..!!

๏ `{hl}ps` » to porn spam by count..!!
"""

ACC_MSG = f"""
**Profile Commands** 

๏ `{hl}setpfp` » to set your pfp..!!

๏ `{hl}block` » to block user by username or reply..!!

๏ `{hl}unblock` » to unblock user by username or reply..!!

๏ `{hl}setname` » to set name of your account..!!

๏ `{hl}setbio` » to set bio of your account..!!
"""

OTHER_MSG = f"""
**Other Commands**

๏ `{hl}trump` » to make trump tweet..!!

๏ `{hl}utweet` » to make tweet by username..!!

๏ {hl}f<action> » fake action > `{hl}ftyping`

๏ `{hl}create group/channel (name)` » to create..!!
"""

LOVE_MSG = f"""
**Love Commands**

๏ `{hl}lover` » check by yourself..!!

๏ `{hl}eflirt` » check by yourself..!!

๏ `{hl}hflirt` » check by yourself..!!

๏ `{hl}loveraid` » check by yourself..!!

"""

FUN_MSG = f"""
**Fun Commands**

๏ `{hl}lover` » 

๏ `{hl}stupid` » 

๏ `{hl}iloveu` » 

๏ `{hl}sex` » 

๏ `{hl}kiss` » 

๏ `{hl}slap` » 

๏ `{hl}dare` » 

๏ `{hl}truth` » 
"""

HELP_BUTTON = IKM(
              [
              [
              IKB("๏ Pmpermit ๏", callback_data='pmpermit'),
              IKB("๏ News ๏", callback_data='news')
              ],
              [
              IKB("๏ Important ๏", callback_data='important'),
              IKB("๏ Create ๏", callback_data='create')
              ],
              [
              IKB("๏ Q ๏", callback_data='q'),
              IKB("๏ Instagram ๏", callback_data='insta')
              ],
              [
              IKB("๏ info ๏", callback_data='info'),
              IKB("๏ convert ๏", callback_data='convert')
              ],
              [
              IKB(" Home 🏠", callback_data='join')
              ]
              ]
              )

                
HELP_MARKUP = IKM(
              [
              [
              IKB("๏ Admins ๏", callback_data="admins"),
              IKB("๏ Extra ๏", callback_data="extra")
              ],
              [
              IKB("๏ Invite ๏", callback_data="invite"),
              IKB("๏ Love ๏", callback_data="love")
              ],
              [
              IKB("๏ Spam ๏", callback_data="spam"),
              IKB("๏ Profile ๏", callback_data="pro")
              ],
              [
              IKB("๏ Other ๏", callback_data="other"),
              IKB("๏ Fun ๏", callback_data='fun')
              ],
              [
              IKB("2nd page 📃", callback_data="2page")
              ]
              ]
              )
sux = None

BACK = IKM(
       [
       [
       IKB("🔙", callback_data="back")
       ]
       ]
       )

BACK_BUTTON = IKM(
              [
              [
              IKB("➡️", callback_data="backup")
              ]
              ]
              )

@Bunny.on_message(filters.command("help", hl))
async def help(client, message):
    global sux
    if not sux:
        sux = Bot.me.username
    await message.edit("`processing...`")
    try:
        nice = await client.get_inline_bot_results(bot=sux, query="inline_help")
    except Exception as e:
        return await message.reply(e)
    try:
        await message.delete()
        await message.delete()
    except:
        pass
    try:
        await client.send_inline_bot_result(message.chat.id, nice.query_id, nice.results[0].id)
    except Exception as e:
        await message.reply(e)

ans = [IQRP(photo_url=HELP_PIC, thumb_url=PIC, title="Help", description="Help Menu", caption=HELP_TEXT, reply_markup=HELP_MARKUP)]

@Bot.on_inline_query()
async def inl(y, x):
    text = x.query.lower()
    try:
        if text == "inline_help":
            await y.answer_inline_query(x.id, results=ans, cache_time=0)     
    except Exception as e:
        print(e)

@Bot.on_callback_query(filters.regex("back"))
async def back(client, message):
    if message.from_user.id != Bunny.me.id:
        return await message.answer("This Is Not For You Baka..!!", show_alert=True)
    await message.answer()
    await message.edit_message_text(text=HELP_TEXT, reply_markup=HELP_MARKUP)
  
@Bot.on_callback_query(filters.regex("admins"))
async def admins(client, message):
    if message.from_user.id != Bunny.me.id:
        return await message.answer("This Is Not For You Baka..!!", show_alert=True)
    await message.answer()
    await message.edit_message_text(text=ADMINS_MSG, reply_markup=BACK)

@Bot.on_callback_query(filters.regex("extra"))
async def extra(client, message):
    if message.from_user.id != Bunny.me.id:
        return await message.answer("This Is Not For You Baka..!!", show_alert=True)
    await message.answer()
    await message.edit_message_text(text=EXTRA_MSG, reply_markup=BACK)

@Bot.on_callback_query(filters.regex("invite"))
async def invite(client, message):
    if message.from_user.id != Bunny.me.id:
        return await message.answer("This Is Not For You Baka..!!", show_alert=True)
    await message.answer()
    await message.edit_message_text(text=INVITE_MSG, reply_markup=BACK)

@Bot.on_callback_query(filters.regex("spam"))
async def spam(client, message):
    if message.from_user.id != Bunny.me.id:
        return await message.answer("This Is Not For You Baka..!!", show_alert=True)
    await message.answer()
    await message.edit_message_text(text=SPAM_MSG, reply_markup=BACK)

@Bot.on_callback_query(filters.regex("love"))
async def love(client, message):
    if message.from_user.id != Bunny.me.id:
        return await message.answer("This Is Not For You Baka..!!", show_alert=True)
    await message.answer()
    await message.edit_message_text(text=LOVE_MSG, reply_markup=BACK)

@Bot.on_callback_query(filters.regex("pro"))
async def profile(client, message):
    if message.from_user.id != Bunny.me.id:
        return await message.answer("This Is Not For You Baka..!!", show_alert=True)
    await message.answer()
    await message.edit_message_text(text=ACC_MSG, reply_markup=BACK)

@Bot.on_callback_query(filters.regex("fun"))
async def profile(client, message):
    if message.from_user.id != Bunny.me.id:
        return await message.answer("This Is Not For You Baka..!!", show_alert=True)
    await message.answer()
    await message.edit_message_text(text=FUN_MSG, reply_markup=BACK)

@Bot.on_callback_query(filters.regex("other"))
async def profile(client, message):
    if message.from_user.id != Bunny.me.id:
        return await message.answer("This Is Not For You Baka..!!", show_alert=True)
    await message.answer()
    await message.edit_message_text(text=OTHER_MSG, reply_markup=BACK)

@Bot.on_callback_query(filters.regex("2page"))
async def pange(client, message):
    if message.from_user.id != Bunny.me.id:
        return await message.answer("This Is Not For You Baka..!!", show_alert=True)
    await message.answer()
    await message.edit_message_text(text=HELP_TEXTT, reply_markup=HELP_BUTTON)

@Bot.on_callback_query(filters.regex("backup"))
async def pange(client, message):
    if message.from_user.id != Bunny.me.id:
        return await message.answer("This Is Not For You Baka..!!", show_alert=True)
    await message.answer()
    await message.edit_message_text(text=HELP_TEXTT, reply_markup=HELP_BUTTON)

@Bot.on_callback_query(filters.regex("fun"))
async def pange(client, message):
    if message.from_user.id != Bunny.me.id:
        return await message.answer("This Is Not For You Baka..!!", show_alert=True)
    await message.answer()
    await message.edit_message_text(text=FUN_MSG, reply_markup=BACK)
