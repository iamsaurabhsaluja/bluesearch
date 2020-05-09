import discord

from discordsearch.services.AnsweringBot import AnsweringBot

class MessageHandler:

    """
    Method handle is called from InitiateEngine. It receives the messages
    and pass them to the method prepareResponse of bot - AnsweringBot
    this class act as connection between answering bot and main engine
    """

    def handle( message ):

        content = str(message.content)
        sender_id = str(message.author.id)

        answering_bot = AnsweringBot()
        return answering_bot.prepareResponse( content, sender_id )
