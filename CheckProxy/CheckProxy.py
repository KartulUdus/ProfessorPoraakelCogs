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
                nstatus = ':white_check_mark: 200 OK, proxy is not banned.'
            if r.status_code == 403:
                nstatus = ':x: 403 Forbidden, proxy is banned.'
        except requests.exceptions.Timeout:
            nstatus = ':x: Timed out after 5 seconds.'
        except requests.exceptions.RequestException as e:
            nstatus = 'Something is wrong with your proxy. Make sure to put the port. Authentication is not supported right now.'

        try:
            r = requests.get('https://sso.pokemon.com/sso/login?locale=en&service=https://www.pokemon.com/us/pokemon-trainer-club/caslogin', proxies=pr, timeout=5)
            if r.status_code == 200:
                pstatus = ':white_check_mark: 200 OK, proxy is not banned.'
            if r.status_code == 409:
                pstatus = ':x: 409 Conflict, proxy is banned.'
        except requests.exceptions.Timeout:
            pstatus = ':x: Timed out after 5 seconds.'
        except requests.exceptions.RequestException:
            pstatus = 'Something is wrong with your proxy. Make sure to put the port. Authentication is not supported right now.'

        await self.bot.say("""Niantic:""" + nstatus + """
                           PTC:""" + pstatus)

        if not ctx.message.chnel.is_private:
            await self.bot.delete_message(ctx.message)


def setup(bot):
    bot.add_cog(checkproxy(bot))
