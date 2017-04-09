import discord
import requests
from discord.ext import commands


class checkforced:
    """Cog for API force checking."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def checkforced(self):
        """Grabs latest forced API version."""

        pr = {
                 'http': '',
             }

        try:
            r = requests.get('https://pgorelease.nianticlabs.com/plfe/version', proxies=pr)
            if r.status_code == 200:
                await self.bot.say(r.content)
            if r.status_code == 403:
                await self.bot.say(':x: I was refused service by Niantic. My proxy must be banned :(')
        except requests.exceptions.RequestException as e:
            await self.bot.say(':x: I was unable to connect to Niantic.')


def setup(bot):
    bot.add_cog(checkforced(bot))
