# from project.battle_field import BattleField
# from project.card.card_repository import CardRepository
# from project.card.magic_card import MagicCard
# from project.card.trap_card import TrapCard
# from project.player.advanced import Advanced
# from project.player.beginner import Beginner
# from project.player.player_repository import PlayerRepository
#
#
# class Controller:
#     def __init__(self):
#         self.player_repository = PlayerRepository()
#         self.card_repository = CardRepository()
#
#     def add_player(self, type: str, username: str):
#         if type == 'Beginner':
#             self.player_repository.add(Beginner(username))
#         elif type == 'Advanced':
#             self.player_repository.add(Advanced(username))
#         return f"Successfully added player of type {type} with username: {username}"
#
#     def add_card(self, type: str, name: str):
#         if type == 'Magic':
#             self.card_repository.add(MagicCard(name))
#         elif type == 'Trap':
#             self.card_repository.add(TrapCard(name))
#         return f"Successfully added card of type {type}Card with name: {name}"
#
#     def add_player_card(self, username: str, card_name: str):
#         needed_player = self.player_repository.find(username)
#         needed_card = self.card_repository.find(card_name)
#         needed_player.card_repository.add(needed_card)
#         return f"Successfully added card: {card_name} to user: {username}"
#
#     def fight(self, attack_name: str, enemy_name: str):
#         attacker = self.player_repository.find(attack_name)
#         enemy = self.player_repository.find(enemy_name)
#         battlefield = BattleField()
#         battlefield.fight(attacker, enemy)
#         return f"Attack user health {attacker.health} - Enemy user health {enemy.health}"
#
#     def report(self):
#         output = []
#         for player in self.player_repository.players:
#             output.append(f'Username: {player.username} - Health: {player.health} - Cards {player.card_repository.count}')
#             for card in player.card_repository.cards:
#                 output.append(f'### Card: {card.name} - Damage: {card.damage_points}')
#
#         return '\n'.join(output)

from project.battle_field import BattleField
from project.card.card_repository import CardRepository
from project.card.magic_card import MagicCard
from project.card.trap_card import TrapCard
from project.player.advanced import Advanced
from project.player.beginner import Beginner
from project.player.player_repository import PlayerRepository


class Controller:
    def __init__(self):
        self.player_repository = PlayerRepository()
        self.card_repository = CardRepository()

    def add_player(self, type: str, username: str):
        if type == "Beginner":
            self.player_repository.add(Beginner(username))
        else:
            self.player_repository.add(Advanced(username))
        return f"Successfully added player of type {type} with username: {username}"

    def add_card(self, type: str, name: str):
        if type == 'Magic':
            self.card_repository.add(MagicCard(name))
        else:
            self.card_repository.add(TrapCard(name))
        return f"Successfully added card of type {type}Card with name: {name}"

    def add_player_card(self, username: str, card_name: str):
        player = self.player_repository.find(username)
        card = self.card_repository.find(card_name)
        player.card_repository.add(card)
        return f"Successfully added card: {card_name} to user: {username}"

    def fight(self, attack_name: str, enemy_name: str):
        attacker = self.player_repository.find(attack_name)
        enemy = self.player_repository.find(enemy_name)
        battle_field = BattleField()
        battle_field.fight(attacker, enemy)
        return f"Attack user health {attacker.health} - Enemy user health {enemy.health}"

    def report(self):
        output = ""
        for player in self.player_repository.players:
            output += f'Username: {player.username} - Health: {player.health} - Cards {player.card_repository.count}\n'
            for card in player.card_repository.cards:
                output += f"### Card: {card.name} - Damage: {card.damage_points}\n"
        return output
