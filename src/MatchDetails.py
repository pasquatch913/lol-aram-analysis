from src.Participant import Participant

class MatchDetails:

    def __init__(self, details):
        self.gameId = details['gameId']
        self.gameDuration = details['gameDuration']
        temp_team1 = []
        temp_team2 = []

        for i in range(0,10):
            if details['participants'][i]['teamId'] == 100:
                temp_team1.append(Participant(details['participants'][i], details['participantIdentities'][i]))
            else:
                temp_team2.append(Participant(details['participants'][i], details['participantIdentities'][i]))
        self.teams = [
            {
                "id": details['teams'][0]['teamId'],
                "win": details['teams'][0]['win'],
                "teamOne": temp_team1,
                "teamTwo": temp_team2
            }
        ]
