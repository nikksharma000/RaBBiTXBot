from pyrogram.types import Message
from config import HANDLER as hl
import requests
from Imshivaexe.powers import get_text
from pyrogram import Client, filters
from Imshivaexe import Bunny

@Bunny.on_message(filters.command("trump", hl) & filters.me)
async def tweet(client: Client, message: Message):
    text = get_text(message)
    if not text:
        await message.edit(f"`ɢɪᴠᴇ ᴍᴇ sᴏᴍᴛʜɪɴɢ ᴛᴏ ᴛᴡᴇᴇᴛ..!!`")
        return
    url = f"https://nekobot.xyz/api/imagegen?type=trumptweet&text={text}"
    r = requests.get(url=url).json()
    tweet = r["message"]
    await message.edit(f"`ᴛʀᴜᴍᴘ ɪs ᴛᴡᴇᴇᴛɪɴɢ...💥`")
    await client.send_photo(message.chat.id, tweet)
    await message.delete()
