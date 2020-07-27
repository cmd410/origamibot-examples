from origamibot import OrigamiBot

class BotModule:
    """Generic pluggable module"""
    def __init__(self, bot: OrigamiBot):
        self.bot = bot