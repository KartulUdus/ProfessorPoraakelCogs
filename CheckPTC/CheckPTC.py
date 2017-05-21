from urllib.parse import parse_qs
from requests_futures.sessions import FuturesSession
import logging
import json

    wehaveitall = False

class checkptc:
    """checks if PTC is working properly."""

    loginurl = 'https://sso.pokemon.com/sso/login?service=https%3A%2F%2Fsso.pokemon.com%2Fsso%2Foauth2.0%2FcallbackAuthorize'
    oauth = 'https://sso.pokemon.com/sso/oauth2.0/accessToken'
    clientsecret = 'w8ScCUXJQc6kXKw8FiOhd8Fixzht18Dq3PEVkUCP5ZPxtgyWsbTvWHFLm2wNY0JR'

    def __init__(self, bot):

        self.bot = bot
        with open('CheckPTC.json', 'r') as f:
            config = json.load(f)

    @commands.command()
    async def checkptc(self):
        """Checks the current status of PTC login."""
        logging.info('Trying to login to PTC.')

        head = {'User-Agent': 'niantic'}
        session = FuturesSession()

        try:
            r1 = session.get(loginurl, headers=head, timeout=15)
        except BaseException as e:
            await self.bot.say(':x: Timed out or failed to connect. PTC is probably having issues.')
            logging.info('Failed to connect to PTC: %s', e)
            return False
        try:
            r1data = json.loads(r1.result().content.decode('utf-8'))
            data = {
                'lt': r1data['lt'],
                'execution': r1data['execution'],
                '_eventId': 'submit',
                'username': config['username'],
                'password': config['password'],
            }
        except BaseException as e:
            logging.error('Failed to GET lt and execution')
            await self.bot.say(':x: Failed initial auth GET, PTC might be having issues.')
            session.get('https://club.pokemon.com/us/pokemon-trainer-club/logout')
            return False
        try:
            r2 = session.post(loginurl, data=data, headers=head, timeout=15)
        except BaseException as e:
            logging.error('Failed to POST login data.')
            await self.bot.say(':x: Failed to login to PTC.')
            return False
        try:
            ticket = re.sub('.*ticket=', '', r2.result().history[0].headers['Location'])
            logging.info('PTC login successful.')
        except BaseException as e:
            logging.error('Failed to find ticket')
            await self.bot.say(':x: Couldn\'t find a valid ticket, PTC is probably having issues.')
            return False
        try:
            logging.info('Grabbing PoGo access token')
            accessdata = {
                'client_id': 'mobile-app_pokemon-go',
                'redirect_uri': 'https://www.nianticlabs.com/pokemongo/error',
                'client_secret': clientsecret,
                'grant_type': 'refresh_token',
                'code': ticket
            }
            r3 = session.post(oauth, data=accessdata, timeout=15)
            qs = parse_qs(r3.result().content.decode('utf-8'))
            accesstoken = qs.get('access_token', None)
            if accesstoken is not None:
                logging.info('PTC access token successfully retrieved.' + accesstoken[:25])
                await self.bot.say(':white_check_mark: Logged into PTC successfully. \n' +
                                   'Token: `' + accesstoken[:25] + '`')
                session.get('https://club.pokemon.com/us/pokemon-trainer-club/logout')
            else:
                logging.error('Logged in, but failed to get access token.')
                await self.bot.say(':x: Logged in, but unable to get an access token. PTC is probably having issues.')
                session.get('https://club.pokemon.com/us/pokemon-trainer-club/logout')
                return False
        except BaseException as e:
            logging.error('Logged in, but failed to get an access token.')
            await self.bot.say(':x: Logged in, but unable to get an access token. PTC is probably having issues.')
            session.get('https://club.pokemon.com/us/pokemon-trainer-club/logout')
            return False


def setup(bot):
    bot.add_cog(checkptc(bot))
