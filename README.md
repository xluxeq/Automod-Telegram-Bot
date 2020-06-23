# Automod-Telegram-Bot
Sentiment/Mood-based auto public group moderation bot for Telegram.me.

I don't really have a place to host this if you want to set it up, I just wanted to throw it together since I noticed it didn't really exist.

It only works on public groups.

If a user says a negative word/sentence at the configurable setting (how many times it repeats in a row/and how negative it sounds) it will mute them for 12 hours.


Uses:

https://github.com/cjhutto/vaderSentiment

https://github.com/python-telegram-bot/python-telegram-bot


To run, install python 3 and run...

```python3 -m pip install -r requirements.txt```

Talk to @botfather on telegram and get a bot key. Input this bot key in place of: BOTKEYBOTKEYBOTKEYBOTKEY
in the python file at the top. Disable private/privacy mode on the bot and set to disabled. This will allow it to read all messages. The bot must also be admin in your group(s).

Then run the bash script on linux...

```./start```

Or on windows run the python file directly.


Command reference:

```
start - starts the bot
stop - stops the bot
repeat - how many times a user must be negative back to back to get muted
adjust - sensitivity level
```

