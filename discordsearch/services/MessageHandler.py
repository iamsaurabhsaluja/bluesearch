import discord

from AnsweringBot import AnsweringBot

class MessageHandler:

    """
    this class act as connection between answering bot and main engine
    """

    def handle( message ):
        answering_bot = AnsweringBot()
        return answering_bot.prepareResponse( message )
