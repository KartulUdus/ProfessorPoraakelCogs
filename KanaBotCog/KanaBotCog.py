import discord
import paramiko
from discord.ext import commands
import sshgo from commander
import configargparse
import os
import sys
client = discord.Client()



class kanaBot:
    """Allow kanaNagu to have basic control"""

    def __init__(self, bot):
        self.bot = bot


    @commands.group(pass_context=True)
    @commands.has_role("kananägu")
    async def kana(self, ctx):
        if ctx.invoked_subcommand is None:
            await self.bot.say('Invalid :chicken:')

    @kana.command(pass_context=True)
    async def tallinn(self):
       await self.bot.say("lol ple")

    @kana.command(pass_context=True)
    async def tartu(self):
        await self.bot.say("lol potato")

    @kana.command(pass_context=True)
    async def peetri(self):
       await self.bot.say("lol ple")

    @kana.command(pass_context=True)
    async def rakvere(self):
        await self.bot.say("lol potato")

    @kana.command(pass_context=True)
    async def haapsalu(self):
       await self.bot.say("lol ple")

    @kana.command(pass_context=True)
    async def kuressaare(self):
        await self.bot.say("lol potato")

    @kana.command(pass_context=True)
    async def webserver(self):
       await self.bot.say("lol ple")

    @kana.command(pass_context=True)
    async def nginx(self):
        await self.bot.say("lol potato")

    @kana.command(pass_context=True)
    async def dontdothis(self):
       await self.bot.say("lol ple")

    @kana.command(pass_context=True)
    async def test(self):
        sshgo("test")
        await self.bot.say("lol potato")

    @kana.command(pass_context=True)
    async def alarm(self):
        await self.bot.say("lol potato")






def setup(bot):
    bot.add_cog(kanaBot(bot))
