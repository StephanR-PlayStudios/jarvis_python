
class JarvisBranch:
    def __init__(self, branchId, gameId, name, gitBranch):
        self.id = branchId
        self.gameId = gameId
        self.name = name
        self.gitBranch = gitBranch

    def __str__(self):
        return f"[Environments] Name: {self.name}, branch: {self.gitBranch}"

