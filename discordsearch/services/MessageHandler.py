import discord

from discordsearch.services.AnsweringBot import AnsweringBot

class MessageHandler:

    """
    this class act as connection between answering bot and main engine
    """

    def handle( message ):

        content = str(message.content)
        print(message)
        sender_name = '' #str(message.name)

        answering_bot = AnsweringBot()
        return answering_bot.prepareResponse( content, sender_name )
