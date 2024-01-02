from pyrogram import Client, filters
from pyrogram.types import Message
from Imshivaexe import startTime
from Imshivaexe import get_uptime
import time 
from config import HANDLER as hl
from Imshivaexe import grt
from Imshivaexe import Bunny

@Bunny.on_message(filters.command("ping",  hl) & filters.me)
async def ping(client, message):
    r = await client.get_me()
    st = time.time()
    end = time.time()
    user = r.mention
    upt = get_uptime(time.time())
    pong = str((end-st)*1000)[0:5]
    gtr = grt(int(time.time()-startTime))
    PING = f"""
__𝗣𝗢𝗡𝗚 🏓__

__**๏ ᴘɪɴɢ »**__ `{pong}`
__**๏ ᴜᴘᴛɪᴍᴇ »**__ `{upt}`
**__๏ ᴏᴡɴᴇʀ »__** {user}
"""
    return await message.edit(PING)
