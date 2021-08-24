import random


class Character:
    def __init__(self, name, attacks):
        self.name = name
        self.health = 0
        self.attacks = attacks
        self.current_move = []

    def increment_damage(self, damage):
        self.health += damage

    def select_move(self):
        self.current_move = random.choice(self.attacks)


class Battle:
    def __init__(self, P1, CPU):
        self.P1 = P1
        self.CPU = CPU
