from discord.ext import commands
import logging
import json
import discord

try:
    from requests_futures.sessions import FuturesSession
    wehaveitall = True
except:
    wehaveitall = False

class json:
    """Gives JSON formatted """

    def __init__(self, bot):

        self.bot = bot

    @commands.command()
    async def json(self, text*):
        """Checks the current status of PTC login."""
        logging.info('Trying parse JSON.')

        try:
            await self.bot.say(text*)
        except BaseException as e:
            logging.error('Failed to GET lt and execution: %s', e)
            await self.bot.say(':x: something')
            return False



def setup(bot):
    bot.add_cog(json(bot))
