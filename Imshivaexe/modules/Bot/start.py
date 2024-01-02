from pyrogram import Client, filters
from Imshivaexe import Bot
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.types import Message
from config import LOGGER_ID
from Imshivaexe import Bunny

START_BUTTONS = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton('๏ Support ๏', url='https://telegram.me/RoBotXsupport'),
            InlineKeyboardButton("๏ Updates ๏", url='https://t.me/Robotxupdates')
        ],
        [
            InlineKeyboardButton("๏ Repo ๏", url='https://github.com/Imshivaexe/RaBBiTUserBot')
        ]
    ]
)


START_TEXT = """
__**Heya!!**__ {}

**__๏ Im RaBBiTX UserBot Developer Assistant Here..!! __**

**__๏ If you want to know more about me then you can join my support group..!!__**

**My Developer ~** {}

**By © @ITZ_RaBBiTX**
"""

@Bot.on_message(filters.private & filters.command(["start"]))
async def start(client, message :Message):
    x = Bunny.me.mention
    await message.reply_text(
        text=START_TEXT.format(message.from_user.first_name, x),
        disable_web_page_preview=True,
        quote=True,
        reply_markup=START_BUTTONS
    )

@Bot.on_message(filters.incoming & filters.private,group=-1)
async def cid(shiva, message):
          await message.forward(LOGGER_ID)
