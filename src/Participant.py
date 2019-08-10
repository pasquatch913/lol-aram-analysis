class Participant:

    def __init__(self, participant, account):
        self.participantId = participant['participantId']
        self.accountId = account['player']['accountId']
        self.championId = participant['championId']