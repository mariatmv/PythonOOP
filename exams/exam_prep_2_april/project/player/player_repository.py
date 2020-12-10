from project.player.player import Player


class PlayerRepository:
    count: int
    players: list

    def __init__(self):
        self.count = 0
        self.players = []

    def add(self, player: Player):
        # existing_player = [x for x in self.players if x.username == player.username]
        # if len(existing_player) > 0:
        try:
            existing_player = [x for x in self.players if x.username == player.username][0]
            raise ValueError(f"Player {player.username} already exists!")
        except IndexError:
            self.players.append(player)
            self.count += 1

    def remove(self, player: str):
        if player == '':
            raise ValueError("Player cannot be an empty string!")
        needed_player = [x for x in self.players if player == x.username][0]
        self.players.remove(needed_player)
        self.count -= 1

    def find(self, username: str):
        needed_player = [x for x in self.players if username == x.username][0]
        return needed_player
