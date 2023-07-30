import os
import time
class Character:
    def __init__(self, name: str, HP: int, SP: int , ATK:int):
        self.name = name
        self.HP = HP 
        self.SP = SP
        self.ATK = ATK
        self.max_hp = HP
        self.max_sp = SP

    
    def __str__(self) -> str:
        return f"{self.name}(HP={self.HP}, SP={self.SP})" 

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
    def vitality_boost(self):
        hp = int(self.max_hp * 0.35 + self.HP)
        sp = int(self.max_sp * 0.35 + self.SP)
        self.HP = min(hp,self.max_hp)
        self.SP = min(sp,self.max_sp)
    

Ferhat= Character("Ferhat", 2000, 450, 150)
Ferhat = Warrior.from_charachter(Ferhat)
MOB= Character ("MOB", 3000, 400 , 50)


character = (Ferhat, MOB) 
turn = 0

def clear_console():
    os.system("cls" if os.name == "nt" else "clear")

while True: 
    clear_console() 
    print(f"{Ferhat} VS {MOB}" )

    attacker = character[turn]     
    defender = character[1-turn]

    if isinstance(attacker, Warrior):
        warrior_q = input("Saldırı girişi yapın: ")
        if warrior_q.lower() == "q" :
            verilen_hasar = attacker.heavy_strike()
            if attacker.ATK == verilen_hasar:
                print("Yetersiz SP")
            else :
                print("Heavy Strike becerisi kullanıldı.")
                defender.HP = max(0, defender.HP - verilen_hasar)
                print(f"{attacker.name} {defender.name}a {verilen_hasar} hasar verdi")
                print(f"{defender.name} canı {defender.HP} ")
        elif warrior_q.lower() == "w" :
            print("Vitality Boost becerisi kullanıldı.")
            attacker.vitality_boost()
            print(f"{attacker.name} karakterinin güncellenmiş HP değeri: {attacker.HP}")
            print(f"{attacker.name} karakterinin güncellenmiş SP değeri: {attacker.SP}")
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

    #ilkerle __str__ ekledik 12-07-2023
