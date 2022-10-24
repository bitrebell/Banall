from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
import responsre as R
from main import BOT_TOKEN
print("Bot is starting.......")

photo = "https://te.legra.ph/file/cf00ecd72b3ee934bd87e.jpg"
# photo2 = "https://te.legra.ph/file/036781df069b478254e37.jpg"

updater = Updater("BOT_TOKEN", None)


def start(update: Update, context: CallbackContext):
  update.message.reply_text(
    f"{photo} \n𝒉𝒊𝒊𝒊 𝒊 𝒂𝒎 𝒍𝒂𝒓𝒂... 𝒂𝒔𝒔𝒊𝒔𝒕𝒂𝒏𝒕 𝒐𝒓 @aadillllll . \n𝒓𝒆𝒎𝒆𝒎𝒃𝒆𝒓 𝒐𝒏𝒆 𝒕𝒉𝒊𝒏𝒈 𝒎𝒚 𝒎𝒂𝒔𝒕𝒆𝒓 𝒂𝒍𝒘𝒂𝒚𝒔 𝒃𝒆 𝒐𝒑.... 𝒔𝒐 𝒅𝒐𝒏'𝒕 𝒎𝒆𝒔𝒔 𝒖𝒑 𝒘𝒊𝒕𝒉 𝒉𝒊𝒎. 𝒃𝒖𝒕 𝒍𝒂𝒅𝒊𝒆𝒔 𝒚𝒐𝒖 𝒂𝒓𝒆 𝒘𝒆𝒍𝒄𝒐𝒎𝒆 𝒕𝒐 𝒉𝒆𝒓 𝒅𝒎  𝒐𝒓 𝒊𝒏𝒔𝒕𝒂. 𝒂𝒍𝒔𝒐 𝒚𝒐𝒖 𝒌𝒏𝒐𝒘 𝒂𝒃𝒐𝒖𝒕 𝒉𝒆𝒓. 𝒋𝒖𝒔𝒕 𝒕𝒚𝒑𝒆 /info 𝒂𝒏𝒅 𝒃𝒐𝒐𝒎 𝒚𝒐𝒖 𝒌𝒏𝒐𝒘 𝒂𝒍𝒍 𝒂𝒃𝒐𝒖𝒕 𝒉𝒆𝒓.ֆ 💛💭ۦ"
  )


def info(update: Update, context: CallbackContext):
  update.message.reply_text(
    """ https://te.legra.ph/file/036781df069b478254e37.jpg \n HERE are the some commands that you know  
	Available Commands :-
	/crush - To get the information about my master
	/insta - To get the instagram profile URL
	/gmail - To get gmail URL
	/github - To get the github URL""")


def crush_about(update: Update, context: CallbackContext):
  update.message.reply_text(
    "Hiiii my name is Aadil Shiekh. I have many thing to telll i know you here for my personal information. So, let's begin\n\
		my age is just 17 years.\nheight of 6 feet and the thing you don't know is my weight which is just 62 kg\
		I lived in New Delhi - JAMNAPAAR. \nI am a class 12th science(PCMB) student with a decent above average student profile. \nI best in Physics and Maths as well. But Chemistry is such a loosing face for me. \nBut if you want to be better text me.\nAnd then my professtional profile, I am a Developer with the master in Python CSS HTML and JAVA SCRIPT.\nI have Deploy Many of Telegram bots. And currently working with a secret projec let it be down.\nif you wanna to know more just dm me"
  )


def instagram_url(update: Update, context: CallbackContext):
  update.message.reply_text("INSTAGRAM Link =>\
	https://www.instagram.com/aadillllll._/")


def gmail_url(update: Update, context: CallbackContext):
  update.message.reply_text("GMAIL URL => \
		darkanger008@gmail.com")


def github_url(update: Update, context: CallbackContext):
  update.message.reply_text("GITHUB URL => https://github.com/Darkranger00/")


def gaali(update: Update, context: CallbackContext):
  update.message.reply_text("bsdk ka apna kaam kar")


def pyar(update: Update, context: CallbackContext):
  update.message.reply_text(
    "Tere gher wale tujhe uss ladki se jaada pyar or care karte hai\
  Kal hi aai ladki ke leye 21saal ki life ka end nhi kar sakta")


dict1 = {i: f"give a big hand to adil" for i in range(10)}


def repeat(update: Update, context: CallbackContext):
  update.message.reply_text(dict1)


def handle_message(update: Update, context: CallbackContext):
  text = str(update.message.text).lower()
  responses = R.sample_response(text)

  update.message.reply_text(responses)


#def unknown_text(update: Update, context: CallbackContext):
#	update.message.reply_text(
#		"Sorry I can't recognize you , you said '%s'" % update.message.text)


def mainn():
  updater.dispatcher.add_handler(CommandHandler('start', start))
  updater.dispatcher.add_handler(CommandHandler('insta', instagram_url))
  updater.dispatcher.add_handler(CommandHandler('info', info))
  updater.dispatcher.add_handler(CommandHandler('github', github_url))
  updater.dispatcher.add_handler(CommandHandler('crush', crush_about))
  updater.dispatcher.add_handler(CommandHandler('gmail', gmail_url))
  updater.dispatcher.add_handler(CommandHandler('repeat', repeat))
  updater.dispatcher.add_handler(CommandHandler('pyar', pyar))
  updater.dispatcher.add_handler(MessageHandler(Filters.text, handle_message))
  # Filters out unknown commands

  # Filters out unknown messages.
  # updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))

  updater.start_polling()
  updater.idle()


mainn()
