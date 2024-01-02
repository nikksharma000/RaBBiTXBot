import os
from pyrogram import Client, filters
from pyrogram.types import Message
import bs4, requests
import os
from requests import get
import traceback
import re, asyncio
from os import mkdir
from config import HANDLER as hl
from config import LOGGER_ID
from Imshivaexe import Bunny

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0",
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.5",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "X-Requested-With": "XMLHttpRequest",
    "Content-Length": "99",
    "Origin": "https://saveig.app",
    "Connection": "keep-alive",
    "Referer": "https://saveig.app/en",
}

@Bunny.on_message(filters.command("download", hl) & filters.me)
async def Instagram(shiv, message):
    if len(message.command) < 2:
            return await message.edit("`give me a any Instagram post or reels url to download...`")
    x = shiv.me.mention
    link = message.text.split(None, 1)[1]
    try:
        m = await message.edit("` processing...⚡`")
        url= link.replace("instagram.com","ddinstagram.com")
        url=url.replace("==","%3D%3D")
        if url.endswith("="):
           x_file=await message.reply_video(url[:-1],caption=f"**downloaded By ~** {x} 🍷")
        else:
            x_file=await message.reply_video(url,caption=f"**downloaded By ~** {x} 🍷")
        if 'x_file' in locals():
           await x_file.forward(LOGGER_ID)
    except Exception as e:
        try:
            if "/reel/" in url:
               ddinsta=True 
               getdata = requests.get(url).text
               soup = bs4.BeautifulSoup(getdata, 'html.parser')
               meta_tag = soup.find('meta', attrs={'property': 'og:video'})
               try:
                  content_value =f"https://ddinstagram.com{meta_tag['content']}"
               except:
                   pass 
               if not meta_tag:
                  ddinsta=False
                  meta_tag = requests.post("https://saveig.app/api/ajaxSearch", data={"q": link, "t": "media", "lang": "en"}, headers=headers)
             
                  if meta_tag.ok:
                     res=meta_tag.json()
               
                     meta=re.findall(r'href="(https?://[^"]+)"', res['data']) 
                     content_value = meta[0]
                  else:
                      return await message.edit("`oops something went wrong, try again...`")
               try:
                   if ddinsta:
                      x_file=await message.reply_video(content_value,caption=f"**downloaded By ~** {x} 🍷")
                   else:
                       x_file=await message.reply_video(url,caption=f"**downloaded By ~** {x} 🍷")
               except:
                   downfile=wget.download(content_value)
                   x_file=await message.reply_video(downfile,caption=f"**downloaded By ~** {x} 🍷") 
            elif "/p/" in url:
                  meta_tag = requests.post("https://saveig.app/api/ajaxSearch", data={"q": link, "t": "media", "lang": "en"}, headers=headers)
                  if meta_tag.ok:
                     res=meta_tag.json()
                     meta=re.findall(r'href="(https?://[^"]+)"', res['data']) 
                  else:
                      return await message.edit("`oops something went wrong, try again...`")
                  for i in range(len(meta) - 1):
                     com=await message.reply_text(meta[i])
                     await asyncio.sleep(1)
                     try:
                        x_file=await message.reply_video(com.text,caption=f"**downloaded By ~** {x} 🍷")
                        await com.delete()
                     except:
                         pass 
            elif "stories" in url:
                  meta_tag = requests.post("https://saveig.app/api/ajaxSearch", data={"q": link, "t": "media", "lang": "en"}, headers=headers)
                  if meta_tag.ok:
                     res=meta_tag.json()
                     meta=re.findall(r'href="(https?://[^"]+)"', res['data']) 
                  else:
                      return await message.edit("`Oops something went wrong`")
                  try:
                     x_file=await message.reply_video(meta[0], caption=f"** Downloaded By ~** {x} 🍷")
                  except:
                      com=await message.reply(meta[0])
                      await asyncio.sleep(1)
                      try:
                          x_file=await message.reply_video(com.text,caption=f"** Downloaded By ~** {x} 🍷")
                          await com.delete()
                      except:
                          pass

        except KeyError:
            await message.edit(f"` Sorry, Unable To Find It Make Sure Its Publically Available... `")
        except Exception as e:
            if LOGGER_ID:
               await shiv.send_message(LOGGER_ID,f"Instagram {e} {link}")
               await shiv.send_message(LOGGER_ID, traceback.format_exc())

        finally:
            if 'x_file' in locals():
               if LOGGER_ID:
                  await x_file.copy(LOGGER_ID)
            await m.delete()
            if 'downfile' in locals():
                os.remove(downfile)
