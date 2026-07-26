import requests
from config import NewsApi
from speech.speak import speak
from brain.ai import translate_to_hindi
import feedparser

def get_news(command):
    if "sport" in command:
        url = "https://news.google.com/rss/headlines/section/topic/SPORTS?hl=hi&gl=IN&ceid=IN:hi"
    elif "business" in command:
        url = "https://news.google.com/rss/headlines/section/topic/BUSINESS?hl=hi&gl=IN&ceid=IN:hi"
    elif "TECHNOLOGY" in command or "technical" in command:
        url = "https://news.google.com/rss/headlines/section/topic/TECHNOLOGY?hl=hi&gl=IN&ceid=IN:hi"
    else:
        url = "https://news.google.com/rss?hl=hi&gl=IN&ceid=IN:hi"

    feed = feedparser.parse(url)
    for news in feed.entries[:5]:
        speak(news.title)


def get_news2():
    r = requests.get(f"https://newsapi.org/v2/top-headlines?category=general&apiKey={NewsApi}")
    if r.status_code == 200:
    # parse the JSON response
        data = r.json()
        # Extract the articles
        articles = data.get('articles',[])
        # Speak headlines
        for article in articles:
            translated = translate_to_hindi(article['title'])
            speak(translated)
    print("news shared")    