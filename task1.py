Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import sys
... 
... class Game:
...     def __init__(self):
...         self.player = Player()
...         self.story = Story()
...     
...     def start(self):
...         print("Welcome to the Text-Based Adventure Game!")
...         self.player.create_character()
...         self.story.start_story(self.player)
...     
...     def play(self):
...         while True:
...             self.story.next_step(self.player)
... 
... class Player:
...     def __init__(self):
...         self.name = ""
...         self.health = 100
...         self.inventory = []
...     
...     def create_character(self):
...         self.name = input("Enter your character's name: ")
...         print(f"Welcome, {self.name}!")
... 
... class Story:
...     def __init__(self):
...         self.steps = {
...             0: self.step_0,
...             1: self.step_1,
...             2: self.step_2
...         }
...         self.current_step = 0
...     
...     def start_story(self, player):
...         self.steps[self.current_step](player)
...     
...     def next_step(self, player):
...         choice = input("What do you want to do next? (Enter step number): ")
...         if choice.isdigit():
...             choice = int(choice)
...             if choice in self.steps:
...                 self.steps[choice](player)
...             else:
...                 print("Invalid choice. Try again.")
...         else:
...             print("Please enter a valid number.")
    
    def step_0(self, player):
        print(f"{player.name} finds themselves at the entrance of a dark cave.")
        print("1: Enter the cave")
        print("2: Look around")
    
    def step_1(self, player):
        print(f"{player.name} bravely enters the cave. It's dark and you hear strange noises.")
        player.health -= 10
        print(f"Your health is now {player.health}.")
        print("1: Continue deeper")
        print("2: Exit the cave")
    
    def step_2(self, player):
        print(f"{player.name} finds a treasure chest!")
        player.inventory.append("Golden Sword")
        print(f"Inventory: {player.inventory}")
        print("1: Take the sword and leave the cave")
        print("2: Search for more treasure")

# Run the game
if __name__ == "__main__":
    game = Game()
    game.start()
    game.play()
