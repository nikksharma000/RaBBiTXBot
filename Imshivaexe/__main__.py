from Imshivaexe import Bunny, Bot
import asyncio
import time
import importlib
from pyrogram import Client, idle
from Imshivaexe.modules import ALL_MODULES
from config import LOGGER_ID

async def start_user():
    await Bot.start()
    print("[•RBX•]: єνєяутнιиg ιѕ σк, ѕтαятιиg... уσυя υѕєявσт ρℓєαѕє ωαιт... ⚡")
    for all_module in ALL_MODULES:
        importlib.import_module("Imshivaexe.modules" + all_module)
        print(f"[•RBX•] ѕυ¢¢єѕѕfυℓℓу ιмρσятє∂ {all_module} ⚡")
    await Bunny.start()
    x = await Bunny.get_me()
    print(f"υѕєявσт ѕυ¢¢єѕѕfυℓℓყ ѕтαятє∂ αѕ {x.first_name} ⚡ ")
    try:
     await Bunny.join_chat("RoBotXSupport")
     await Bunny.join_chat("RoBotXUpdates")
    except:
      pass
    try:
     await Bunny.send_message(LOGGER_ID, "__**ѕтαятє∂ !!**__")
    except:
      pass
    await idle()
  
loop = asyncio.get_event_loop()
loop.run_until_complete(start_user())
