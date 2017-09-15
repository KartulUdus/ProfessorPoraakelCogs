import discord
import paramiko
from discord.ext import commands


class kanaNagu:
    """Allow kanaNagu to have basic control"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def kana(self):


        if discord.Role.name == 'kananägu':

            await self.bot.say("lol pleb, " + user.mention + " you have to be :chicken: to do that")
            await self.bot.delete_message(ctx.message)

def setup(bot):
    bot.add_cog(kanaNagu(bot))
