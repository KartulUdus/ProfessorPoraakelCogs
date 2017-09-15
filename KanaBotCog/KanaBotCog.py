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


    @commands.command(pass_context=True)
    async def kana(self):

    if discord.user.role.id
        await self.bot.say("lol pleb, you have " + str(discord.role)+ "to be :chicken: to do that")





def setup(bot):
    bot.add_cog(kanaBot(bot))
