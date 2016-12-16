import requests

class PySC2:

    def __init__(self, api_key, token=None):
        # config settings for calling the starcraft API
        self.api_key = api_key
        self.root_url = "https://us.api.battle.net"
        self.title = "sc2"
        self.locale="en_us"
        self.region=1
        self.token=token

    def _starcraftapi_request(self, url):
        # requests that require your API key use this field.
        apiurl = "{url}&apikey={apikey}".format(
            url=url,
            apikey=self.api_key
        )
        response = requests.get(apiurl)
        response.raise_for_status()
        return response

    def _starcraftapitoken_request(self, url):
        # This is used when a token is needed to access information rather than an API key
        apiurl = "{url}?access_token={token}".format(
            url=url,
            token=self.token
        )
        response = requests.get(apiurl)
        response.raise_for_status()
        return response

    def _data_request(self, endpoint):
        # requests that are based on metadata for Starcraft
        url = "{root}/{title}/data/{endpoint}?local={locale}".format(
                root=self.root_url,
                title=self.title,
                endpoint=endpoint,
                locale=self.locale
            )
        response = self._starcraftapi_request(url)
        return response.json()

    def get_achievements(self):
        # get all available achievements
        return self._data_request("achievements")

    def get_rewards(self):
        # get all available rewards
        return self._data_request("rewards")

    def _profile_request(self, id, name, endpoint=None):
        # requests that are based on iformation from a specific user. A user id and name are required.
        if endpoint is not None:
            url = "{root}/{title}/profile/{id}/{region}/{name}/{endpoint}?local={locale}".format(
                    root=self.root_url,
                    title=self.title,
                    id=id,
                    name=name,
                    region=self.region,
                    endpoint=endpoint,
                    locale=self.locale
                )
        else:
            url = "{root}/{title}/profile/{id}/{region}/{name}/?local={locale}".format(
                root=self.root_url,
                title=self.title,
                id=id,
                name=name,
                region=self.region,
                locale=self.locale
            )
        response = self._starcraftapi_request(url)
        return response.json()

    def get_profile(self, id, name):
        # retrive gamer profile
        return self._profile_request(id, name)

    def get_userLadder(self, id, name):
        # get the current users ladder information
        return self._profile_request(id, name, endpoint='ladders')

    def get_matches(self, id, name):
        # retrive current matches
        return self._profile_request(id, name, endpoint='matches')

    def _ladder_request(self, id):
        # request all players in a ladder
        url = "{root}/{title}/ladder/{id}?local={locale}".format(
            root=self.root_url,
            title=self.title,
            id=id,
            locale=self.locale
        )
        response = self._starcraftapi_request(url)
        return response.json()

    def get_ladder(self, id):
        # get ladder info for a specific ladder
        return self._ladder_request(id)

    def get_currentSeason(self):
        # get current season
        url = 'https://us.api.battle.net/data/sc2/season/current'
        response = self._starcraftapitoken_request(url)
        return response.json()

    def get_ladderData(self, season, qid=201, teamType=0, leagueID=6):
        '''
        default info shows Legacy of the void 1v1, arranged, grandmaster ladder
        for other ladders:

        Queue ID
        1 - Wings of Liberty 1v1
        2 - Wings of Liberty 2v2
        3 - Wings of Liberty 3v3
        4 - Wings of Liberty 4v4
        101 - Heart of the Swarm 1v1
        102 - Heart of the Swarm 2v2
        103 - Heart of the Swarm 3v3
        104 - Heart of the Swarm 4v4
        201 - Legacy of the Void 1v1
        202 - Legacy of the Void 2v2
        203 - Legacy of the Void 3v3
        204 - Legacy of the Void 4v4
        206 - Legacy of the Void Archon

        Team Type
        0 - Arranged
        1 - Random

        League ID
        0 - Bronze
        1 - Silver
        2 - Gold
        3 - Platinum
        4 - Diamond
        5 - Master
        6 - Grandmaster
        '''
        url = 'https://us.api.battle.net/data/sc2/league/{season}/{qid}/{teamType}/{leagueID}'.format(
            season=season,
            qid=qid,
            teamType=teamType,
            leagueID=leagueID
        )
        response = self._starcraftapitoken_request(url)
        return response.json()
