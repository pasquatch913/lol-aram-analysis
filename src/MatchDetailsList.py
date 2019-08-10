import requests
import json
import time
import os
from src.MatchDetails import MatchDetails


class MatchDetailsList:
    def __init__(self, matches):
        temp_list = []
        for match in matches.matches[:5]:
            lol_matchdetails_url = 'https://na1.api.riotgames.com/lol/match/v4/matches/{}?api_key={}'.format(match.gameId, os.environ.get('RIOT_API_KEY'))
            r = requests.get(lol_matchdetails_url)
            match_details = json.loads(r.text)
            temp_list.append(MatchDetails(match_details))
            #     wait 2 seconds in between sending request for match details because rate limiting
            time.sleep(2)
        self.match_list = temp_list
