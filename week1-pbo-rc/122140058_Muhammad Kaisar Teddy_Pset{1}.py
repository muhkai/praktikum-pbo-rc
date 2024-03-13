class Robot:
  
    def __init__(self, name, health_point, attack, defense):
        self.name = name
        self.health_point = health_point
        self.attack = attack
        self.defense = defense

    def launch_attack(self, enemy, ally_choise, enemy_choise):
        print(f'{self.name} attack {enemy.name} with {self.attack} damages')
        if ally_choise == 2 or enemy_choise == 2:
            pass
        else:
            enemy.health_point -= self.attack
            if enemy.health_point <= 0:
                print(f'{enemy.name} has been slain')

    def survive(self, enemy, ally_choise, enemy_choise): 
        print(f'{self.name} survive succed')
        self.health_point -= enemy.attack - self.defense
        if self.health_point <= 0:
            print(f'{self.name} has been slain')

    def life(self):
        return self.health_point > 0

class Game:

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.round = 0

    def play(self): 
        print('     Rules of Game\n')
        print("*The Attack option is used to attack the opponent with the current power attack*")
        print("*The Defense option functions to block the opponent's attack equal to the opponent's attack power minus the current defense power*")
        print("*The Give Up option is used for players to give up from the match*")
        print("*The HP Regen option functions to add health points by 10% of the current health points*")
        print("*The Upgrade Attack Power option functions to add Attack by 20% of the current Attack*")
        print("*The Recall option functions to add health points by 50% of the current health points*")

        while self.player1.life() and self.player2.life():

            self.round += 1
            print(f"\n     Round {self.round}")
            print(f'\n{self.player1.name} vs {self.player2.name}')
            print(f'Health point {self.player1.name} : {self.player1.health_point}; Attack power: {self.player1.attack}; Attack Resistance: {self.player1.defense}')
            print(f'Health point {self.player2.name}: {self.player2.health_point}; Attack power: {self.player2.attack}; Attack Resistance: {self.player2.defense}')

            print(f'\n1. Attack      2. Defense      3. Give Up      4. HP Regen      5. Upgrade Attack Power      6. Recall')
            ally_choise = int(input(f'{self.player1.name}, choose the option: '))
            print(f'\n1. Attack      2. Defense      3. Give Up      4. HP Regen      5. Upgrade Attack Power      6. Recall')
            enemy_choise = int(input(f'{self.player2.name}, choose the options: '))
            print('')
            
            if ally_choise == 3 and enemy_choise == 3:
                print(f'Tha match is draw, {self.player1.name} and {self.player2.name} are give up')
                break
            
            if ally_choise == 2 and enemy_choise == 2:
                print(f'Booth use defense')

            else:
                if ally_choise == 1:
                    self.player1.launch_attack(self.player2, ally_choise, enemy_choise)
                elif ally_choise == 2:
                    self.player1.survive(self.player2, ally_choise, enemy_choise)
                elif ally_choise == 3:
                    print(f'{self.player1.name} is give up')
                    print(f'{self.player2.name} is the winner!!')
                    break
                elif ally_choise == 4:
                    self.player1.health_point += (10/100) * self.player1.health_point
                    print(f'{self.player1.name} increase the HP')
                elif ally_choise == 5:
                    self.player1.attack += (20/100) * self.player1.attack
                    print(f'{self.player1.name} upgrade the attack power')
                elif ally_choise == 6:
                    self.player1.health_point += (1/2) * self.player1.health_point
                    print(f'{self.player1.name} increase the HP')
                else:
                    print('INVALID')

                if enemy_choise == 1:
                    self.player2.launch_attack(self.player1, ally_choise, enemy_choise)
                elif enemy_choise == 2:
                    self.player2.survive(self.player1, ally_choise, enemy_choise)
                elif enemy_choise == 3:
                    print(f'{self.player2.name} is give up')
                    print(f'{self.player1.name} is the winner!!')
                    break  
                elif enemy_choise == 4:
                    self.player2.health_point += (10/100) * self.player2.health_point
                    print(f'{self.player2.name} increase the HP')
                elif enemy_choise == 5:
                    self.player2.attack += (10/100) * self.player2.attack
                    print(f'{self.player2.name} upgrade the attack power')
                elif enemy_choise == 6:
                    self.player2.health_point += (1/2) * self.player2.health_point
                    print(f'{self.player2.name} increase the HP')
                else:
                    print('Invalid')


player1 = Robot('Liu Kang', 200, 40, 15)
player2 = Robot('Kunglao', 200, 35, 20)
game = Game(player1, player2)
game.play()
