import discord
from discord.ext import commands


class telegram:
    """Send filter information"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)

    async def scream(self):
        msg = discord.message
        await self.bot.say(msg)



def setup(bot):
    bot.add_cog(telegram(bot))
