import random

class Monster:
    def __init__(self, name, health, attack, weapon, armor):
        self.name = name
        self.health = health
        self.attack = attack
        self.weapon = weapon
        self.armor = armor

    @staticmethod
    def generate_monster(floor):
        monsters = [
            ("Goblin", 20, 5, "Rusty Dagger", "Tattered Leather"),
            ("Orc", 30, 8, "Crude Axe", "Hide Armor"),
            ("Troll", 50, 12, "Giant Club", "Thick Skin"),
            ("Skeleton", 25, 7, "Bone Sword", "Ribcage"),
            ("Zombie", 35, 6, "Rotten Hand", "Decayed Clothes"),
            ("Werewolf", 45, 10, "Sharp Claws", "Wolf Pelt"),
            ("Vampire", 55, 11, "Blood Drinker", "Noble's Cloak"),
            ("Dragon", 100, 15, "Dragon Fang", "Dragon Scales"),
            ("Demon", 80, 14, "Hellfire Blade", "Infernal Plate"),
            ("Lich", 70, 13, "Soul Stealer", "Necromancer Robes")
        ]
        name, base_health, base_attack, weapon, armor = monsters[min(floor - 1, len(monsters) - 1)]
        health = base_health + (floor * 10)
        attack = base_attack + floor
        return Monster(name, health, attack, weapon, armor)

