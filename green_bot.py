"""This is an example of setting up gevent to work with origamibot
"""

from gevent.monkey import patch_all
patch_all()  # Make standard library cooperative


from time import sleep  # Then, and only then import anything else
from main import bot

# The thing is
# Gevent does not change working with the bot at all
# The difference is that now bot will use gevent's greenlets
# For all messages and callbacks

if __name__ == '__main__':
    bot.start()
    print('Bot started polling...')
    while True:
        sleep(10)