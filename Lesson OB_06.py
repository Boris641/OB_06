import pygame
pygame.init()

class Hero:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack_power = 20

    def attack(self, other):
        print(f"{self.name} атакует {other.name} с силой {self.attack_power} урона.")
        other.health -= self.attack_power

    def is_alive(self):
        return self.health > 0

class Game:
    def __init__(self, player_name, computer_name):
        self.player = Hero(player_name)
        self.computer = Hero(computer_name)

    def start(self):
        turn = True  # True для хода игрока, False для хода компьютера
        while self.player.is_alive() and self.computer.is_alive():
            if turn:
                self.player.attack(self.computer)
                print(f"У {self.computer.name} осталось {self.computer.health} здоровья.\n")
            else:
                self.computer.attack(self.player)
                print(f"У {self.player.name} осталось {self.player.health} здоровья.\n")

            turn = not turn

        if self.player.is_alive():
            print(f"Победил {self.player.name}!")
        else:
            print(f"Победил {self.computer.name}!")

if __name__ == "__main__":
    game = Game("Игрок", "Компьютер")
    game.start()