import random

# Base Character class
class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health  

    #modify the attack method to deal random damage within range
    def attack(self, opponent):
        damage = random.randint(1, 50)
        opponent.health -= damage
        print(f"{self.name} attacks {opponent.name} causing {damage} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

    def display_stats(self):
        print(f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}")

    def heal(self):
        self.health += 30
        if self.health > self.max_health:
            self.health = self.max_health
        print(f"{self.name} utilizes self-healing powers. Current health: {self.health}")

# Warrior class (inherits from Character)
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25)
    
    def special_ability(self, opponent):
        choice = input("\nWhich special ability would you like to use? Enter (1) Slingshot or (2) Visit Witch: ")
        if choice == "1":
            opponent.health -= 25
            self.health += 10
            print(f"{self.name} attacks with slingshot and buys time to heal. {opponent.name} health is now {opponent.health}. {self.name} health is: {self.health}")
        elif choice == "2":
            self.health += 25
            print(f"{self.name} visits the Witch. Health has increased to {self.health} while the spell they cast on {opponent.name} reduces {opponent.name}'s health to {opponent.health}")
        else:
            print("Sorry, that's not one of the options. Please try again.")

# Mage class (inherits from Character)
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35)

    def special_ability(self, opponent):
        choice = input("\nWhich special ability would you like to use? Enter (1) Hug a tree or (2) Conjure a storm: ")
        if choice == "1":
            self.health += 40
            opponent.health -= 5
            print(f"{self.name} hugs a tree, stealing some of {opponent.name}'s power. Current health is {self.health}.")
        elif choice == "2":
            self.health -= 5
            opponent.health -= 40
            print(f"{self.name} conjures a storm, reducing {opponent.name}'s health to {opponent.health} and own health to {self.health}")
        else:
            print("Sorry, that's not one of the options. Please try again.")
       
# Witch class (inherits from Character)
class Witch(Character):
    def __init__(self, name):
        super().__init__(name, health=200, attack_power=40)

    def special_ability(self, opponent):
        choice = input("Which special ability would you like to use? Enter (1) Invisible cloak or (2) Elixir: ")
        if choice == "1":
            self.health += 50
            opponent.health -= 15
            print(f"{self.name} puts on an invisible cloak and reduces {opponent.name}'s strength to {opponent.health}. Current health: {self.health}.")
        elif choice == "2":
            self.health += 18
            opponent.health -= 36
            print(f"{self.name} shares elixir with {opponent.name}. {self.name} current health: {self.health}. {opponent.name} current health: {opponent.health}.")
        else:
            print("Sorry, that's not one of the options. Please try again.")

# Changeling class (inherits from Character)
class Changeling(Character):
    def __init__(self, name):
        super().__init__(name, health=180, attack_power=35)

    def special_ability(self, opponent):
        choice = input("\nWhich special ability would you like to use? Enter (1) Enchant or (2) Power Nap: ")
        if choice == "1":
            opponent.health -= 20
            self.health += 20
            print(f"{self.name} enchants {opponent.name} to steal power. Current health of {opponent.name} is now {opponent.health}.")
        elif choice == "2":
            self.health += 35
            print(f"{self.name} disappears for a power nap. {opponent.name}'s energy decreases to {opponent.health} while searching for {self.name}. Current health: {self.health}.")
        else:
            print("Sorry, that's not one of the options. Please try again.")        

# EvilWizard class (inherits from Character)
class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=15)

    def regenerate(self):
        self.health += 5
        print(f"{self.name} regenerates 5 health! Current health: {self.health}")


def create_character():
    print("Choose your character class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Witch") 
    print("4. Changeling")  

    class_choice = input("Enter the number of your class choice: ")
    name = input("Enter your character's name: ")

    if class_choice == '1':
        return Warrior(name)
    elif class_choice == '2':
        return Mage(name)
    elif class_choice == '3':
        return Witch(name)
    elif class_choice == '4':
        return Changeling(name)
    else:
        print("Invalid choice. Defaulting to Warrior.")
        return Warrior(name)

def battle(player, wizard):
    while wizard.health > 0 and player.health > 0:
        print("\n--- Your Turn ---")
        print("1. Attack")
        print("2. Use Special Ability")
        print("3. Heal")
        print("4. View Stats")

        choice = input("Choose an action: ")

        if choice == '1':
            player.attack(wizard)
        elif choice == '2':
            player.special_ability(wizard) # implements special ability
        elif choice == '3':
            player.heal() # implements healing mechanic
        elif choice == '4':
            player.display_stats()
        else:
            print("Invalid choice. Try again.")

        if wizard.health > 0:
            wizard.regenerate()
            wizard.attack(player)

        if player.health <= 0:
            print(f"{player.name} has been defeated!")
            break

    if wizard.health <= 0:
        print(f"{wizard.name} has been defeated by {player.name}!")

def main():
    player = create_character()
    wizard = EvilWizard("The Dark Wizard")
    battle(player, wizard)

if __name__ == "__main__":
    main()
