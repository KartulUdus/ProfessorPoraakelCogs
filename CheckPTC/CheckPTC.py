# taken from pgoapi's auth_ptc.

from __future__ import absolute_import
from future.standard_library import install_aliases
install_aliases()

import re
import six
import json
import logging
import requests
import discord
import random

from urllib.parse import parse_qs
from discord.ext import commands

from requests.exceptions import ConnectionError

class checkptc():
    """checks if ptc is working using pgoapi's login code"""

    PTC_LOGIN_URL = 'https://sso.pokemon.com/sso/login?service=https%3A%2F%2Fsso.pokemon.com%2Fsso%2Foauth2.0%2FcallbackAuthorize'
    PTC_LOGIN_OAUTH = 'https://sso.pokemon.com/sso/oauth2.0/accessToken'
    PTC_LOGIN_CLIENT_SECRET = 'w8ScCUXJQc6kXKw8FiOhd8Fixzht18Dq3PEVkUCP5ZPxtgyWsbTvWHFLm2wNY0JR'

    def __init__(self, bot):

        self.bot = bot

        self._auth_provider = 'ptc'

        self._session = requests.session()
        self._session.verify = True

    def set_proxy(self, proxy_config):
        self._session.proxies = proxy_config
    @commands.command()
    async def checkptc(self):
        """Checks the current status of PTC login."""
        logging.info('Trying to login to PTC with tfoxmap5')

        head = {'User-Agent': 'niantic'}

        try:
            r = self._session.get(self.PTC_LOGIN_URL, headers=head, timeout=15)
        except ConnectionError as e:
            await self.bot.say(':x: Timed out or failed to connect completely. PTC is probably having issues.', e)

        try:
            jdata = json.loads(r.content.decode('utf-8'))
            data = {
                'lt': jdata['lt'],
                'execution': jdata['execution'],
                '_eventId': 'submit',
                'username': 'USER',
                'password': 'PASSWORD',
            }
        except ValueError as e:
            logging.error('PTC User Login Error - Field missing in response: %s', e)
            await self.bot.say(':x: Alright something is probably wrong on my end. Missing field in PTC response. If PTC is having problems, though, this could happen.')
            self._session.get('https://club.pokemon.com/us/pokemon-trainer-club/logout')
            return False
        except KeyError as e:
            logging.error('PTC User Login Error - Field missing in response.content: %s', e)
            await self.bot.say(':x: Alright something is probably wrong on my end. Missing field in PTC response. If PTC is having problems, though, this could happen.')
            self._session.get('https://club.pokemon.com/us/pokemon-trainer-club/logout')
            return False

        r1 = self._session.post(self.PTC_LOGIN_URL, data=data, headers=head, timeout=10)

        ticket = None
        try:
            ticket = re.sub('.*ticket=', '', r1.history[0].headers['Location'])
        except Exception as e:
            try:
                await self.bot.say(':x: PTC is probably down. Failed to get a token.')
                self._session.get('https://club.pokemon.com/us/pokemon-trainer-club/logout')
            except Exception as e:
                await self.bot.say(':x: PTC is probably down. Failed to get a token.')
                self._session.get('https://club.pokemon.com/us/pokemon-trainer-club/logout')
            return False

        self._refresh_token = ticket
        logging.info('PTC User Login successful.')

        logging.info('Trying to grab an access token.')
        data1 = {
            'client_id': 'mobile-app_pokemon-go',
            'redirect_uri': 'https://www.nianticlabs.com/pokemongo/error',
            'client_secret': self.PTC_LOGIN_CLIENT_SECRET,
            'grant_type': 'refresh_token',
            'code': self._refresh_token,
        }

        r2 = self._session.post(self.PTC_LOGIN_OAUTH, data=data1, timeout=10)

        qs = r2.content.decode('utf-8')
        token_data = parse_qs(qs)

        access_token = token_data.get('access_token', None)
        if access_token is not None:
            self._access_token = access_token[0]

            self._login = True

            logging.info('PTC Access Token successfully retrieved.')
            await self.bot.say(':white_check_mark: Logged into PTC successfully. \n' +
            'Token: `' + self._access_token[:25] + '`')
            logging.debug('PTC Access Token: %s...', self._access_token[:25])
            self._session.get('https://club.pokemon.com/us/pokemon-trainer-club/logout')
        else:
            self._access_token = None
            self._login = False
            await self.bot.say(':x: Logged in, but unable to get an access token. PTC is probably having issues.')
            logging.info("Could not retrieve a PTC Access Token")
            self._session.get('https://club.pokemon.com/us/pokemon-trainer-club/logout')

    def set_refresh_token(self, refresh_token):
        logging.info('PTC Refresh Token provided by user')
        self._refresh_token = refresh_token


def setup(bot):
    bot.add_cog(checkptc(bot))
