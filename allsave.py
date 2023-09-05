import telebot
import requests
from bs4 import BeautifulSoup

TOKEN = '5846077277:AAHpdlzdSaf4cMNh0IJcIS8jclTkaU8T8Vg'
bot = telebot.TeleBot("5846077277:AAHpdlzdSaf4cMNh0IJcIS8jclTkaU8T8Vg")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Merhaba! YouTube, TikTok, Instagram veya Pinterest'ten video indirmek için linki paylaşabilirsin.📋")

@bot.message_handler(func=lambda message: True)
def download_video(message):
    url = message.text.strip()

    if 'youtube.com/watch?v=' in url:
        youtube_download(url, message)
    elif 'tiktok.com/' in url:
        tiktok_download(url, message)
    elif 'instagram.com/' in url:
        instagram_download(url, message)
    elif 'pinterest.' in url:
        pinterest_download(url, message)
    else:
        bot.reply_to(message, "Desteklenmeyen bir link girdiniz.")

def youtube_download(url, message):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        video_element = soup.find('meta', attrs={'property': 'og:video'})
        video_url = video_element['content']
        bot.send_video(message.chat.id, video_url)
    except:
        bot.reply_to(message, "Video indirme işlemi başarısız oldu.")

def tiktok_download(url, message):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        video_element = soup.find('meta', attrs={'property': 'og:video'})
        video_url = video_element['content']
        bot.send_video(message.chat.id, video_url)
    except:
        bot.reply_to(message, "Video indirme işlemi başarısız oldu.")

def instagram_download(url, message):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        video_element = soup.find('meta', attrs={'property': 'og:video'})
        video_url = video_element['content']
        bot.send_video(message.chat.id, video_url)
    except:
        bot.reply_to(message, "Video indirme işlemi başarısız oldu.")

def pinterest_download(url, message):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        video_element = soup.find('meta', attrs={'property': 'og:video'})
        video_url = video_element['content']
        bot.send_video(message.chat.id, video_url)
    except:
        bot.reply_to(message, "Video indirme işlemi başarısız oldu.")

bot.polling()
