import sys
import os
from getpass import getpass
from time import sleep

from origamibot import OrigamiBot as Bot

from examples import simple, inline


token = os.environ.get(
    'BOT_TOKEN',
    (
        sys.argv[1]
        if len(sys.argv) > 1
        else getpass('Enter token: ')
    ))

bot = Bot(token)

bot.add_commands(simple.Commands(bot))


bot.add_inline(inline.InlineListener(bot))

if __name__ == '__main__':
    bot.start()
    print('Bot started polling...')
    while True:
        sleep(10)
