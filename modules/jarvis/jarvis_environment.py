class JarvisEnvironment:
    def __init__(self, id, gameId, name, production, configId, config_version, config_name, claimedByDisplayName):
        self.id = id
        self.gameId = gameId
        self.name = name
        self.production = production
        self.configId = configId
        self.config_version = config_version
        self.config_name = config_name
        self.claimedByDisplayName = claimedByDisplayName

    def __str__(self):
        return f"[Branches] Name: {self.name}, Production: {self.production}, Config: {self.config_name}, Claimed by: {self.claimedByDisplayName}"
