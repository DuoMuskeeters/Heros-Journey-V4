import time

class Character:
    def __init__(self, name: str, HP: int, SP: int , ATK:int):
        self.name = name
        self.HP = HP 
        self.SP = SP
        self.ATK = ATK

class Warrior(Character):

    @classmethod
    def from_charachter(cls, chr: Character):
        return cls(chr.name, chr.HP, chr.SP, chr.ATK)
    

    def heavy_strike(self):
        if self.SP > 50 or self.SP == 50:
            strike_damage = self.ATK * 2    
            self.SP = self.SP - 50
            return strike_damage

        return self.ATK 

Ferhat= Character("Ferhat", 2000, 450, 150)
Ferhat = Warrior.from_charachter(Ferhat)
MOB= Character ("MOB", 3000, 400 , 50)


character = (Ferhat, MOB)
turn = 0


while True: 

    attacker = character[turn]     
    defender = character[1-turn]

    if isinstance(attacker, Warrior):
        warrior_q = input("Heavy strike becerisini kullanmak icin Q ya basin.")
        if warrior_q.lower() == "q" :
                verilen_hasar = attacker.heavy_strike()
                if attacker.ATK == verilen_hasar:
                    print("Yetersiz SP")
                defender.HP = max(0, defender.HP - verilen_hasar)
                print(f"{attacker.name} {defender.name}a {verilen_hasar} hasar verdi")
                print(f"{defender.name} canı {defender.HP} ")
                print(f"Ferhat kalan SP {Ferhat.SP}")
        else:   
                defender.HP = max(0, defender.HP - attacker.ATK)
                print(f"{attacker.name} {defender.name}a {attacker.ATK} hasar verdi")
                print(f"{defender.name} canı {defender.HP} ")
    else:
            defender.HP = max(0, defender.HP - attacker.ATK)
            print(f"{attacker.name} {defender.name}a {attacker.ATK} hasar verdi")
            print(f"{defender.name} canı {defender.HP} ")
    if defender.HP == 0:
        print(f"{defender.name} {attacker.name} tarafından katledildi")
        break
    input()    
    turn = 1-turn


#isinstance ekledik ilkerle 12-07-2023 
#verilen hasara esitleyip heavy strike sp sorununu cozduk 12-07-2023
#superinit yerine classmethod kullandik 12-07-2023