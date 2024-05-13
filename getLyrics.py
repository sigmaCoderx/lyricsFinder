
# import bot library 
from telebot import TeleBot,types,util
from telebot.types import*
from telebot.util import user_link

from lyricsgenius import Genius

# get your own genius api key from lyrics genius
genuisKey = "x6UwAfX611_JKxAf1T2gJEOSd2efmt4c5d4EQm1ohy05DhbX2_yGS5RQYX7PiidUWiYzz0LHK15NNbcetXspZw"

bot = TeleBot("6934289676:AAE0COsWQoMTj4TR6hZGbVvhAZqDlUVZvjw",parse_mode="HTML")

# helps to create inline keyboards
markup = InlineKeyboardMarkup()
group = InlineKeyboardButton(text="Group",url="t.me/neuralg")
channel = InlineKeyboardButton(text="Channel",url="t.me/neuralp")
markup.add(group,channel)

# this handler works when the "/start" command sent to the bot
@bot.message_handler(commands=["start"])
def greet(msg):
    user = f"{user_link(msg.from_user)}"
    bot.reply_to(msg,f"""Hello {user} send song name or the lyrics,i can give you the lyrics""",reply_markup=markup)


@bot.message_handler(func=lambda m:True)
def getLyrics(query):
    genius = Genius(genuisKey)
    #lyrics = genius.search_lyrics(query)

    music = genius.search_song(query.text.strip())
    lyrics = music.lyrics
   
    #bot.reply_to(query,f"""```\n{lyrics}``` """,reply_markup=markup,parse_mode="MarkdownV2")
    """if len(lyrics) > 4096:
        for msg in range(0, len(lyrics), 4096):
            bot.send_message(query.chat.id, lyrics[msg:msg+4096],reply_markup=markup)
    else:"""
    bot.reply_to(query,lyrics,reply_markup=markup)


bot.infinity_polling()