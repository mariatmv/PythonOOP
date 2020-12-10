from project.player.player import Player


class BattleField:
    @staticmethod
    def fight(attacker: Player, enemy: Player):
        if attacker.is_dead or enemy.is_dead:
            raise ValueError("Player is dead!")
        if attacker.__class__.__name__ == "Beginner":
            BattleField.beginner_player_bonuses(attacker)
        if enemy.__class__.__name__ == 'Beginner':
            BattleField.beginner_player_bonuses(enemy)

        BattleField.bonus_health(attacker)
        BattleField.bonus_health(enemy)

        for card in attacker.card_repository.cards:
            enemy.take_damage(card.damage_points)
            if enemy.is_dead:
                return

        for card in enemy.card_repository.cards:
            attacker.take_damage(card.damage_points)
            if attacker.is_dead:
                return

    @classmethod
    def beginner_player_bonuses(cls, player: Player):
        player.health += 40

        for card in player.card_repository.cards:
            card.damage_points += 30

    @classmethod
    def bonus_health(cls, player: Player):
        sum = 0
        for card in player.card_repository.cards:
            sum += card.health_points
        player.health += sum
