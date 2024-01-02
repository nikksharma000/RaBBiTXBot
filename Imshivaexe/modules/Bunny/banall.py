from pyrogram import Client, filters
from config import HANDLER as hl
from Imshivaexe import Bunny

@Bunny.on_message(filters.command("banall", hl) & filters.me)
async def banall(client, message):
    if not message.from_user:
        return
    ok = await message.edit("`Getting chat members...⚡`")
    mem = []
    async for x in client.get_chat_members(message.chat.id):
        mem.append(x.user.id)
    try:
        await ok.edit("`Banning chat members...⚡`")
    except:
        await message.reply("`Banning chat members...⚡`")
    a = 0
    b = 0
    for y in mem:
        try:
            await client.ban_chat_member(message.chat.id, y)
            a += 1
        except:
            b += 1
            pass
    try:
        await ok.edit(f"**Done ⚡ **\n\n{a} banned..!!\n \n{b} failed..!!")
    except:
        await message.reply(f"Done ⚡ !\n\n{a} banned..!!\n \n {b} failed..!!")
