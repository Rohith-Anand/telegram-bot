import os
username = os.getenv('username')
activekey = os.getenv('activekey')
from Adafruit_IO import Client
aio = Client(username,activekey)
from telegram.ext import Updater, MessageHandler, Filters

def lighton(bot,update):
  aio.send('light',1)
  chat_id = bot.message.chat_id
  bot.message.reply_text('Light is turned ON')

def lightoff(bot,update):
  aio.send('light',0)
  chat_id = bot.message.chat_id
  bot.message.reply_text('Light is turned OFF')

def fanon(bot,update):
  aio.send('fan',1)
  chat_id = bot.message.chat_id
  bot.message.reply_text('Fan is turned ON')

def fanoff(bot,update):
  aio.send('fan',0)
  chat_id = bot.message.chat_id
  bot.message.reply_text('Fan is turned OFF')

def main(bot,update):
  a = bot.message.text
  if a=="turn on light":
    lighton(bot,update)
  elif a=="turn off light":
    lightoff(bot,update)
  elif a=="turn on fan":
    fanon(bot,update)
    
     
  elif a=="turn off fan":
    fanoff(bot,update)

bot_token = os.getenv('bot_token')
u = Updater(bot_token, use_context=True)
d = u.dispatcher
d.add_handler(MessageHandler(Filters.text,main))
u.start_polling()
u.idle()
