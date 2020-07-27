import shlex

from .base import BotModule
from origamibot.util import condition
from origamibot.types import (InlineQuery,
                              InlineQueryResultArticle,
                              InputTextMessageContent)


class InlineListener(BotModule):

    @condition(lambda s, q: q.query.startswith('sum ') or q.query == 'sum')
    def sum(self, q: InlineQuery):
        """sum command implemented in inline

        try: @your_bot_name sum [...numbers...]
        make sure you have inline mode enabled in @Botfather
        """
        params = q.query[3:]
        try:
            numbers = [
                float(i)
                for i in shlex.split(params)
            ]
            if not numbers:
                self._answer(q, 'Enter some numbers')
                return
            s = sum(numbers)
            self._answer(q, str(s))
        except ValueError:
            self._answer(q, 'Cannot sum these types')

    def _answer(self, q, text):
        self.bot.answer_inline_query(
                q.id,
                results=[
                    InlineQueryResultArticle(
                        id=q.query[:32],
                        title=text,
                        input_message_content=InputTextMessageContent(
                            message_text=text
                        )
                    )
                ]
            )
