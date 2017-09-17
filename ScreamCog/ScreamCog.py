import discord
from discord.ext import commands


class telegram:
    """Send filter information"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)

    async def scream(self, ctx, text*):

        await self.bot.say(text)



def setup(bot):
    bot.add_cog(telegram(bot))
