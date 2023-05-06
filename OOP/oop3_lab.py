class Enemy:

    def __init__(self, name='Enemy', health=0, hit_power=0):
        self.name = name
        self.health = health
        self.hit_power = hit_power

    def take_damage(self, damage):
        remaining_health = self.health - damage
        if remaining_health > 0:
            self.health = remaining_health
        else:
            self.health = 0
            print("Enemy is dead!")

    def attack(self):
        print(f"Enemy attack with power {self.hit_power}")

    def __str__(self):
        return f"Name {self.name}. Health: {self.health}. Hit power: {self.hit_power}"


class Troll(Enemy):

    def __init__(self, name):
        super().__init__(name, 100, 20)

    def take_damage(self, damage):
        super().take_damage(damage)
        if self.health == 0:
            self.health = 100

    def attack(self):
        print(f"Troll attack with power {self.hit_power}")


class Goblin(Enemy):

    def __init__(self, name, hit_power):
        super().__init__(name, 200, hit_power)

    def take_damage(self, damage):
        if self.health < 50:
            super().take_damage(damage / 2)
        else:
            super().take_damage(damage)

    def attack(self):
        if self.health < 20:
            return
        super().attack()



troll = Troll("Trolll")
goblin = Goblin("Gobllin", 33)

print(troll)
print(goblin)

print(goblin.attack())
goblin.take_damage(151)
print(goblin)
goblin.take_damage(49)
print(goblin)
goblin.take_damage(10)
print(goblin)