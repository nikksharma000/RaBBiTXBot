from Imshivaexe.powers import extract_user
from pyrogram import Client, filters
from config import HANDLER as hl
from Imshivaexe import Bunny
from pyrogram.types import Message

@Bunny.on_message(filters.me & filters.command(["setpfp"], hl))
async def set_pfp(client: Client, message: Message):
    replied = message.reply_to_message
    if (
        replied
        and replied.media
        and (
            replied.photo
            or (replied.document and "image" in replied.document.mime_type)
        )
    ):
        await client.download_media(message=replied, file_name=profile_photo)
        await client.set_profile_photo(profile_photo)
        if os.path.exists(profile_photo):
            os.remove(profile_photo)
        await message.edit("**Your profile photo has been successfully changed..!!**")
    else:
        await message.edit(
            "`Reply to any photo to set as a profile photo..!!`"
        )
        
