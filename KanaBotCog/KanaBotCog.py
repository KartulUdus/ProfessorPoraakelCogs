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


def ssh(cmd):
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

    try:
        theCmd = cmds[cmd]
    except KeyError:
        return

    be = True
    if cmd in ("nginx", "webserver", "test"):
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
        await self.bot.say("lol potato")

    @kana.command(pass_context=True)
    async def alarm(self):
        await self.bot.say("lol potato")






def setup(bot):
    bot.add_cog(kanaBot(bot))
