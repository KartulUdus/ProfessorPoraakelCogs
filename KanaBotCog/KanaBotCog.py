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
    async def kana(self, ctx):
        if ctx.invoked_subcommand is None:
            await self.bot.say('Invalid :chicken:')

    @kana.command(pass_context=True)
    async def tallinn(self):
       sshgo("tallinn")
       await self.bot.say(":white_check_mark: "+ kana.author.mention +" tallinn restarted")

    @kana.command(pass_context=True)
    async def tartu(self):
        sshgo("tartu")
        await self.bot.say(":white_check_mark: "+ message.author.mention +" tartu restarted")

    @kana.command(pass_context=True)
    async def peetri(self, ctx):
        sshgo("peetri")
        await self.bot.say(":white_check_mark: {} peetri restarted".format(ctx.message.author.mention()))

    @kana.command(pass_context=True)
    async def rakvere(self,ctx):
        sshgo('rakvere')
        await self.bot.say(":white_check_mark: "+ discord.user.mention() +" rakvere restarted")

    @kana.command(pass_context=True)
    async def haapsalu(self, ctx):
       sshgo("haapsalu")
       await self.bot.say(":white_check_mark: "+ ctx.message.author.mention() +" haapsalu restarted")

    @kana.command(pass_context=True)
    async def kuressaare(self):
        sshgo("kuressaare")
        await self.bot.say(":white_check_mark: "+ self.author.mention +" kuressaare restarted")

    @kana.command(pass_context=True)
    async def webserver(self):
        sshgo("webserver")
        await self.bot.say(":white_check_mark: "+ user.mention +" frontend restarted")

    @kana.command(pass_context=True)
    async def nginx(self):
        sshgo("nginx")
        await self.bot.say(":white_check_mark: "+ user.mention +" nginx restarted")

    @kana.command(pass_context=True)
    async def dontdothis(self):
        sshgo("dontdothis")
        await self.bot.say(":white_check_mark: "+ user.mention +" :hamster: server restarted")

    @kana.command(pass_context=True)
    async def alarm(self):
        sshgo("alarm")
        await self.bot.say(":white_check_mark: "+ user.mention +" alarms restarted")


def setup(bot):
    bot.add_cog(kanaBot(bot))
