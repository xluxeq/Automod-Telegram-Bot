# Automod-Telegram-Bot
Sentiment/Mood-based auto public group moderation bot for Telegram.me.

I don't really have a place to host this if you want to set it up, I just wanted to throw it together since I noticed it didn't really exist.

It only works on public groups.

If a user says a negative word/sentence at the configurable setting (how many times it repeats in a row/and how negative it sounds) it will mute them for 12 hours.

If it's online you can find it here: @AutoMoodBot

Please host it yourself because I won't have a host soon.

Uses:

https://github.com/cjhutto/vaderSentiment

https://github.com/python-telegram-bot/python-telegram-bot


To run, install python 3 and run...

```python3 -m pip install -r requirements.txt```

Then run the bash script on linux...

```./start```

Or on windows run the python file directly.
