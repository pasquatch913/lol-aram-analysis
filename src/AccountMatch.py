class AccountMatch:

    def __init__(self, gameId, championId, championIdMap):
        self.gameId = gameId
        self.championId = championId
        self.champion = championIdMap[str(championId)]
