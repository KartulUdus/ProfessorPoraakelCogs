import discord
import requests
from discord.ext import commands


class checkproxy:
    """Cog for proxy checking"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def checkproxy(self, ctx, proxy):
        """Checks the provided proxy."""

        p = proxy
        pr = {
                    'http': p,
                    'https': p
                }
        try:
            r = requests.get('https://pgorelease.nianticlabs.com/plfe/version', proxies=pr, timeout=5)
            if r.status_code == 200:
                await self.bot.say(':white_check_mark: 200 OK, proxy is not banned.')
            if r.status_code == 403:
                await self.bot.say(':x: 403 Forbidden, proxy is banned.')
        except requests.exceptions.timeout:
            await self.bot.say(':x: Timed out checking proxy.')
        except requests.exceptions.RequestException as e:
            await self.bot.say('Something is wrong with your proxy. Make sure to put the port as well as remove http or https from your input. Authentication is not supported right now.')

        if not ctx.message.channel.is_private:
            await self.bot.delete_message(ctx.message)


def setup(bot):
    bot.add_cog(checkproxy(bot))
