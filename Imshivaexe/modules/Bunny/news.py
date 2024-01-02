from pyrogram import Client, filters
import requests
from config import HANDLER as hl
from config import NEWS_API
from Imshivaexe import Bunny

api_key = NEWS_API

@Bunny.on_message(filters.command("news", hl) & filters.me)
def get_news(client, message):
    try:
        response = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={api_key}")
        data = response.json()
        articles = data["articles"]
        news_headlines = "Top 5 News Headlines:\n\n"
        for article in articles[:5]:
            title = article["title"]
            news_headlines += f"📰 {title}\n\n"
        message.edit(news_headlines)
    except Exception as e:
        message.edit(f"An error occurred: `{e}`")
