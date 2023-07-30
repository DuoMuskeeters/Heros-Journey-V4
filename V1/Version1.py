import time

class Character:
    def __init__(self, name: str, HP: int, ATK:int) :
        self.name = name
        self.HP = HP 
        self.ATK = ATK

Ferhat = Character ("" , 2000, 100 )
MOB= Character ("MOB", 3000, 200 )

character = [Ferhat, MOB] 
turn = 0

while True: 

    attacker = character[turn]     
    defender = character[1-turn]

    defender.HP = max(0, defender.HP - attacker.ATK)
    print(f"{attacker.name} {defender.name}a {attacker.ATK} hasar verdi")
    print(f"{defender.name} canı {defender.HP} ")

    if defender.HP == 0:
        print(f"{defender.name} {attacker.name} tarafından katledildi")
        break
    turn = 1-turn
    #time.sleep(0.5)
    #input()
    