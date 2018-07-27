import discord
import paramiko
from discord.ext import commands
import configargparse
import os
import sys
client = discord.Client()

class kanaBot:
    def __init__(self, bot):
        self.bot = bot


    @commands.group(pass_context=True)
    async def kana(self, ctx):
        if ctx.invoked_subcommand is None:
            await self.bot.say('Invalid :robot_face:')

    @kana.command(pass_context=True)
    async def tallinn(self, ctx):

       await self.bot.say(":white_check_mark: "+ (ctx.message.raw_mentions).mention +" tallinn restarted")




def setup(bot):
    bot.add_cog(kanaBot(bot))
