import asyncio
from io import BytesIO
from aiohttp import ClientSession
from pyrogram import Client, filters, enums
from pyrogram.types import Message, User
from config import HANDLER as hl
from Imshivaexe import Bunny
from Imshivaexe.powers import ReplyCheck

aiosession = ClientSession()

async def make_carbon(code):
    url = "https://carbonara.solopov.dev/api/cook"
    async with aiosession.post(url, json={"code": code}) as resp:
        image = BytesIO(await resp.read())
    image.name = "carbon.png"
    return image


@Bunny.on_message(filters.command("carbon", hl) & filters.me)
async def carbon_func(client: Client, message: Message):
    text = (
        message.text.split(None, 1)[1]
        if len(
            message.command,
        )
        != 1
        else None
    )
    if message.reply_to_message:
        text = message.reply_to_message.text or message.reply_to_message.caption
    if not text:
        return await message.delete()
    bunny = await message.edit("`ρяєραяιиg ¢αявσи...⚡`")
    carbon = await make_carbon(text)
    await bunny.edit("`υρℓσα∂ιиg...⚡`")
    await asyncio.gather(
        bunny.delete(),
        client.send_photo(
            message.chat.id,
            carbon,
            reply_to_message_id=ReplyCheck(message),
        ),
    )
    carbon.close()
