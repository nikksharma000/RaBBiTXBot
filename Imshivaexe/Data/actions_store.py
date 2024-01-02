from pyrogram import Client, enums, filters
from pyrogram.raw import functions
from pyrogram.types import Message

""" © @Imshivaexe """

commands = {
    "ftyping": enums.ChatAction.TYPING,
    "fvideo": enums.ChatAction.RECORD_VIDEO,
    "faudio": enums.ChatAction.RECORD_AUDIO,
    "fround": enums.ChatAction.RECORD_VIDEO_NOTE,
    "fphoto": enums.ChatAction.UPLOAD_PHOTO,
    "fsticker": enums.ChatAction.CHOOSE_STICKER,
    "fdocument": enums.ChatAction.UPLOAD_DOCUMENT,
    "flocation": enums.ChatAction.FIND_LOCATION,
    "fgame": enums.ChatAction.PLAYING,
    "fcontact": enums.ChatAction.CHOOSE_CONTACT,
    "fstop": enums.ChatAction.CANCEL,
    "fscreen": "screenshot",
 }

""" © @Imshivaexe """
