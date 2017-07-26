import discord
from discord.ext import commands


class Alarms:
    """Send filter information"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def alarms(self, ctx):
        message = """
        *psst the current information sent in alarms is the following:*
        Pokemon:
                Alakazam
                Machamp
                Golem
                Chansey
                Kangaskhan
                Gyarados
                Lapras
                Snorlax
                Articuno
                Zapdos
                Moltres
                Dragonite
                Mewtwo
                Mew
                Typhlosion
                Feraligatr
                Flaaffy
                Ampharos
                Bellossom
                Politoed
                Sunflora
                Slowking
                Unown
                Steelix
                Scizor
                Heracross
                Corsola
                Delibird
                Kingdra
                Porygon2
                Smeargle
                Tyrogue
                Hitmontop
                Blissey
                Raikou
                Entei
                Suicune
                Larvitar
                Pupitar
                Tyranitar
                Lugia
                Ho-Oh
                Celebi

            Raids:
                  Machamp
                  Articuno
                  Zapdos
                  Moltres
                  Dragonite
                  Mewtwo
                  Mew
                  Blissey
                  Tyranitar
                  Lugia
                  Ho-Oh
                  Celebi
- :potato:
        """
        await self.bot.whisper(message)
        if not ctx.message.channel.is_private:
            await self.bot.delete_message(ctx.message)
    @commands.command(pass_context=True)
    async def telegram(self, ctx):
        message = """*Psst. you can get Free alarms with the following telegram invites*

https://t.me/joinchat/AAAAAD-jtIsx-kisr20vOg - South Tallinn
https://t.me/joinchat/AAAAAD8fmi8HXmV387w_zg - East Tallinn
https://t.me/joinchat/AAAAAEEUNNYVaOwoAlP_Pg - West Tallinn
https://t.me/joinchat/AAAAAEF17qV6JhjMcT1IIw - North Tallinn
https://t.me/joinchat/AAAAAEANW3hO-ZinRwzvBw - Center Tallinn
https://t.me/joinchat/AAAAAEGRXBQYld3ieKxiwg - Peetri-Jüri
https://t.me/joinchat/AAAAAEHASmqup0k4Jq_sVQ - Tartu
https://t.me/joinchat/AAAAAEKQh-3bsQghbR4hXg - Pärnu
https://t.me/joinchat/AAAAAD_LmpnjZDj15_TtrA - Haapsalu

If you wish to support Poraakel, these alarms are available on Discord for support tier lime and up:

https://patreon.com/poraakel

- :potato:

        """
        await self.bot.whisper(message)
        if not ctx.message.channel.is_private:
            await self.bot.delete_message(ctx.message)



def setup(bot):
    bot.add_cog(sprite(bot))
