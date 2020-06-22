#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import ChatPermissions
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import logging, os, time
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)
# Input bot key below
KEY = "BOTKEYBOTKEYBOTKEYBOTKEY"



def start(bot, update):
    ID = update.effective_chat.id
    IDS = str(ID)
    UD = update.effective_user.id
    UDS = str(UD)
    stat = bot.get_chat_member(ID, UD)
    if stat.status == 'creator' or stat.status == 'administrator':
        directory = IDS
        parent_dir = "chats"
        path = os.path.join(parent_dir, directory)
        if os.path.exists(path):
            pass
        else:
            os.mkdir(path)
            writepath = "chats/" + IDS + "/REPEAT"
            with open(writepath, 'w') as f:
                f.write('3')
            writepath = "chats/" + IDS + "/ADJUST"
            with open(writepath, 'w') as f:
                f.write('1.000')
        writepath = "chats/" + IDS + "/ON"
        with open(writepath, 'w') as f:
            pass
        update.message.reply_text('Bot on...')
    else:
        pass

def stop(bot, update):
    ID = update.effective_chat.id
    IDS = str(ID)
    UD = update.effective_user.id
    UDS = str(UD)
    stat = bot.get_chat_member(ID, UD)
    if stat.status == 'creator' or stat.status == 'administrator':
        writepath = 'chats/' + IDS + "/ON"
        if os.path.exists(writepath):
            os.remove(writepath)
        update.message.reply_text('Bot off...')
    else:
        pass

def help(bot, update):
    """Send a message when the command /help is issued."""
    update.message.reply_text('This bot only works in supergroups. Commands are /start /stop /repeat [how many times a negative message] - above or at adjust, and /adjust [decimal between 0.00 and 1.00] - the closer to 1 the more negative a message must be to mute user. I reccomend testing both settings in a personal group first.')

def run(bot, update):
    ID = update.effective_chat.id
    IDS = str(ID)
    UD = update.effective_user.id
    UDS = str(UD)
    stat = bot.get_chat_member(ID, UD)
    if stat.status == 'creator' or stat.status == 'administrator':
        if "/repeat" in update.message.text:
            whitelist = set('0123456789')
            data = ''.join(filter(whitelist.__contains__, update.message.text))
            writepath = 'chats/' + IDS + "/REPEAT"
            with open(writepath, 'w') as owrite:
                owrite.write(data)
        if "/adjust" in update.message.text:
            whitelist = set('0123456789.')
            data = ''.join(filter(whitelist.__contains__, update.message.text))
            writepath = 'chats/' + IDS + "/ADJUST"
            with open(writepath, 'w') as owrite:
                owrite.write(data)
    else:
        writepath = 'chats/' + IDS + "/ON"
        if os.path.exists(writepath):
            analyzer = SentimentIntensityAnalyzer()
            vs = analyzer.polarity_scores(update.message.text)
            data = vs.get('neg')
            readpath = 'chats/' + IDS + "/ADJUST"
            file = open(readpath)
            for digit in file.readlines():
                adj = float(digit)
            readpath = 'chats/' + IDS + "/REPEAT"
            file = open(readpath)
            for digit in file.readlines():
                rep = int(digit)
            print(adj)
            print(rep)
            if data >= adj:
                f=open(writepath, "a+")
                UDSS = UDS + "\r\n"
                f.write(UDSS)
            f.close()
            list = []
            file = open(writepath)
            for line in file.readlines():
                list.append(line)
            print(list)
            if len(list) >= rep:
                repn = rep * -1
                result = False
                result = len(set(list[repn:])) == 1
                if result == True:
                    duration=43200
                    bot.restrictChatMember(chat_id=ID,user_id=UD,
                            until_date=time.time()+duration,
                            permissions = ChatPermissions(
                              can_send_messages = False,
                              can_send_media_messages = False,
                              can_send_other_messages = False,
                              can_add_web_page_previews = False,
                            ))
                    update.message.reply_text("Member trigger muted... Please contact a moderator.")
                else:
                    pass
            else:
                pass
def error(bot, update):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update)

def main():
    # Start the bot
    updater = Updater(KEY, use_context=False)
    dp = updater.dispatcher
    # Add commands
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("stop", stop))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(MessageHandler(Filters.text, run))
    # log all errors
    dp.add_error_handler(error)
    # Start the Bot
    updater.start_polling()
    # Run the bot until you press Ctrl-C
    updater.idle()

if __name__ == '__main__':
    main()
