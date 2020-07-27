from .base import BotModule
from origamibot.types import Message, User


class Commands(BotModule):
    """Very basic commands example

    This class will expose its public methods as commands
    which can be called by user with /[method_name]
    """
    def start(self, message: Message):
        """/start command
        """

        self.bot.reply_to(
            message,
            self._prepare_start_message(message),
            parse_mode='MarkdownV2'
        )

    def sum(self, message: Message, *args):
        """/sum [...] command

        Outputs a sum of given numbers
        """
        try:
            numbers = [float(i) for i in args]
            self.bot.reply_to(
                message,
                str(sum(numbers))
            )
        except ValueError:
            self.bot.reply_to(
                message,
                'Cannot sum these types!!!'
            )

    def _prepare_start_message(self, message: Message):
        """This methods is not exposed as bot command
        because its starts with underscore
        """
        user: User = message.from_user

        m = f'Hello, {user.first_name}\\!\n'
        m += 'This is an example bot made with '
        m += '[origamibot](https://github.com/cmd410/OrigamiBot)'

        return m
