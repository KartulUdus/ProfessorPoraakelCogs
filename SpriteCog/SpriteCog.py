import discord
from discord.ext import commands


class sprite:
    """Send sprite information"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def sprite(self, ctx):
        message = """*Psst. You can grab the sprites at https://stuff.notfurprofit.org/static03.zip*

Simply extract the "static" folder into the root of RocketMap. Replace any files in conflict.

Mac OS Users: You must manually extract the icons folder and the png files into the static folder.

If you would like sprites that go up to gen4, you may use https://stuff.notfurprofit.org/static02.zip.

SpriteBot v2.3
        """
        await self.bot.whisper(message)
        if not ctx.message.channel.is_private:
            await self.bot.delete_message(ctx.message)
    @commands.command(pass_context=True)
    async def cries(self, ctx):
        message = """*Psst. You can grab Pokemon cries at https://stuff.notfurprofit.org/cries01.zip*

Simply extract the "static" folder into the root of RocketMap. Replace any files in conflict.

Mac OS Users: You must manually extract the cries folder from static/sounds into the static/sounds folder of RocketMap.

SpriteBot v2.3
        """
        await self.bot.whisper(message)
        if not ctx.message.channel.is_private:
            await self.bot.delete_message(ctx.message)



def setup(bot):
    bot.add_cog(sprite(bot))
