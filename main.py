from telegram.ext import Updater,MessageHandler,CommandHandler,Filters
from googletrans import Translator

updater = Updater('5146245842:AAFegfAySk8bLl5maxEA2A2xVdxxvgXWwlc',use_context = True )

# \start komandasi uchun mas'ul funksiya
@tarjimonbot.message_handler(commands=["start"])
def salom(message):
    xabar = "Assalom alaykum, tarjimon botiga xush kelbisiz."
    xabar += "\nMatningizni yuboring."
    tarjimonbot.reply_to(message, xabar)
 
def echo(updater,context):
 usr_msg =updater.message.text
 translator = Translator()
 translation = translator.translate(usr_msg,dest='uz') 
 updater.message.reply_text(translation.text)
 
dp =updater.dispatcher.add_handler
dp(CommandHandler('start',start))
dp(MessageHandler(Filters.text,echo))

updater.start_polling()
updater.idle()
