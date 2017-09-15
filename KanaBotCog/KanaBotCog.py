import discord
import paramiko
from discord.ext import commands
import configargparse
import os
import sys
client = discord.Client()


def get_args():
        # Get full dir and default config file path
        configfile = []
        if '-cf' not in sys.argv and '--config' not in sys.argv:
            configfile = [os.getenv('CONFIG', os.path.join(
                os.path.dirname(__file__), 'config.ini'))]
        parser = configargparse.ArgParser(
            default_config_files=configfile)

        # arrrgs, also available in config/config.ini

        parser.add_argument(
            '-cf',
            '--config', is_config_file=True,
            help='path to config file (config.ini by default)')

        parser.add_argument(
            '-sh',
            '--scanhost',
            help='host for scanserver'
        )

        parser.add_argument(
            '-su',
            '--scanuser',
            help='username for scanserver'
        )

        parser.add_argument(
            '-sp',
            '--scanpassword',
            help='password for scanserver'
        )

        parser.add_argument(
            '-fh',
            '--fronthost',
            help='host for frontend server'
        )

        parser.add_argument(
            '-fu',
            '--frontuser',
            help='host for frontend server'
        )

        parser.add_argument(
            '-fp',
            '--frontpassword',
            help='password for frontend server'
        )
        return parser.parse_args()

def sshgo(cmd):
        cmds = {
            'alarm': 'service alarms restart',
            'tallinn': 'service tallinnmap2 restart',
            'tartu': 'service tartumap restart',
            'peetri': 'service peetri restart',
            'haapsalu': 'service haapsalumap restart',
            'rakvere': 'service rakveremap restart',
            'kuressaare': 'service saaremaamap restart',
            'webserver': 'sh restartAll.sh',
            'nginx': 'sudo service nginx restart',
            'dontdothis': 'reboot',
            'test': 'mkdir thisshouldwork'
        }

        args = get_args()
        theCmd = cmds[cmd]
        be = True
        if cmd in ("nginx", "webserver"):
            be = False
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        if (be):
            ssh.connect(args.scanhost, username=args.scanuser,
                        password=args.scanpassword)
            ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(theCmd)
            return
        else:
            ssh.connect(args.fronthost, username=args.frontuser,
                        password=args.frontpassword)
            ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(theCmd)
            return

class kanaBot:
    """Allow kanaNagu to have basic control"""

    def __init__(self, bot):
        self.bot = bot


    @commands.group(pass_context=True)
    @commands.has_role("kananägu")
    async def kana(self, ctx, user : discord.Member):
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
       await self.bot.say(":white_check_mark: "+ str(discord.Member.mention) +" haapsalu restarted")

    @kana.command(pass_context=True)
    async def kuressaare(self, user : discord.Member):
        sshgo("kuressaare")
        await self.bot.say(":white_check_mark: "+ discord.Author.mention +" kuressaare restarted")

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
