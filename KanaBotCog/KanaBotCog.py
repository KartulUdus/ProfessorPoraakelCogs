import discord
import paramiko
from discord.ext import commands
from commander import sshgo
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
    async def tallinn(self, user : discord.Member):
       sshgo("tallinn")
       await self.bot.say(":white_check_mark: "+ user.mention +" tallinn restarted")

    @kana.command(pass_context=True)
    async def tartu(self, user : discord.Member):
        sshgo("tartu")
        await self.bot.say(":white_check_mark: "+ user.mention +" tartu restarted")

    @kana.command(pass_context=True)
    async def peetri(self, user : discord.Member):
        sshgo("peetri")
        await self.bot.say(":white_check_mark: "+ user.mention +" peetri restarted")

    @kana.command(pass_context=True)
    async def rakvere(self, user : discord.Member):
        sshgo('rakvere')
        await self.bot.say(":white_check_mark: "+ user.mention +" rakvere restarted")

    @kana.command(pass_context=True)
    async def haapsalu(self, user : discord.Member):
       sshgo("haapsalu")
       await self.bot.say(":white_check_mark: "+ user.mention +" haapsalu restarted")

    @kana.command(pass_context=True)
    async def kuressaare(self, user : discord.Member):
        sshgo("kuressaare")
        await self.bot.say(":white_check_mark: "+ user.mention +" kuressaare restarted")

    @kana.command(pass_context=True)
    async def webserver(self, user : discord.Member):
        sshgo("webserver")
        await self.bot.say(":white_check_mark: "+ user.mention +" frontend restarted")

    @kana.command(pass_context=True)
    async def nginx(self, user : discord.Member):
        sshgo("nginx")
        await self.bot.say(":white_check_mark: "+ user.mention +" nginx restarted")

    @kana.command(pass_context=True)
    async def dontdothis(self, user : discord.Member):
        sshgo("dontdothis")
        await self.bot.say(":white_check_mark: "+ user.mention +" :hamster: server restarted")

    @kana.command(pass_context=True)
    async def alarm(self, user : discord.Member):
        sshgo("alarm")
        await self.bot.say(":white_check_mark: "+ user.mention +" alarms restarted")


def setup(bot):
    bot.add_cog(kanaBot(bot))
