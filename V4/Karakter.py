from types import SimpleNamespace
from Ekran import *
import json
import random


def Karakter_read(karakter):
    with open(karakter, "r") as file:
        karakter_data = json.load(file)
    return Character(**karakter_data)


class Character:
    def __init__(self, name: str, Level: int,exp :int,stat_point :int,HP: int, max_hp: int, max_sp: int, SP: int, ATK: int, ATKRATE: float, HP_reg: float, SP_reg: float, Strenght: int, Agility: int, Intelligence: int, Constitution: int):
        self.name = name
        self.Level = Level
        self.exp = exp
        self.stat_point = stat_point 
        self.HP = HP
        self.max_hp = max_hp
        self.max_sp = max_sp
        self.SP = SP
        self.ATK = ATK
        self.ATKRATE = ATKRATE
        self.HP_reg = HP_reg
        self.SP_reg = SP_reg
        self.Strenght = Strenght
        self.Agility = Agility
        self.Intelligence = Intelligence
        self.Constitution = Constitution

    def get_info(self):
        return SimpleNamespace(**self.__dict__)

    def __str__(self) -> str:
        return f"{self.name}(HP={self.HP}, SP={self.SP})"

    # def getinfo(self):
    #    return list(self.__dict__.values())
    def exp_boost(self, exp):
        self.exp = self.exp + exp
    def level_up(self):
        gereken_exp = level(self.Level)
        while True:
            if self.exp >= gereken_exp:
                self.Level = self.Level + 1
                self.exp = self.exp - gereken_exp
                self.stat_point = self.stat_point +5
            else:
                break
        self.calculate_power()
    # for the level up
    def update_Stat(self):

        if not self.stat_point :
            return 
        #TODO burası yarrak gibi
        print(f"{self.stat_point} stat puanların var.")
        print("1 Strenght 2 Agility 3 Intelligence 4 Constituon ")
        while self.stat_point > 0:
            choise = input("Lütfen stat puanlarınızı dağıtınız:")
            if choise == "1":
                self.Strenght += 1
            elif choise == "2":
                self.Agility += 1
            elif choise == "3":
                self.Intelligence += 1
            elif choise == "4":
                self.Constitution += 1
            else:
                print("Gecersiz giris")
                continue
            self.stat_point -= 1

    def calculate_power(self):
        self.HP = 100 + self.Constitution * 10
        self.HP_reg = 5 + self.Constitution * 0.1
        self.SP = 50 + self.Intelligence * 5
        self.SP_reg = 2.5 + self.Intelligence * 0.05
        self.ATK = 20 + self.Strenght * 2
        self.ATKRATE = 1 + self.Agility * 0.05
        # return yok


class Warrior(Character):

    # classmethod neden hepsine ihtiyaci var
    @classmethod
    def from_character(cls, chr: Character):
        return cls(chr.name, chr.Level,chr.exp,chr.stat_point, chr.HP, chr.max_hp, chr.max_sp, chr.SP, chr.ATK, chr.ATKRATE, chr.HP_reg, chr.SP_reg, chr.Strenght, chr.Agility, chr.Intelligence, chr.Constitution)

    def heavy_strike(self):
        if self.SP > 50 or self.SP == 50:
            strike_damage = self.ATK * 2
            self.SP = self.SP - 50
            return strike_damage

        return self.ATK

    def vitality_boost(self):
        hp = int(self.max_hp * 0.35 + self.HP)
        sp = int(self.max_sp * 0.35 + self.SP)
        self.HP = min(hp, self.max_hp)
        self.SP = min(sp, self.max_sp)

class Mob:
    def __init__(self, name: str, Level: int, HP: int, max_hp: int, max_sp: int, SP: int, ATK: int, ATKRATE: float, HP_reg: float, SP_reg: float, Strenght: int, Agility: int, Intelligence: int, Constitution: int):
        self.name = name
        self.Level = Level
        self.HP = HP
        self.max_hp = max_hp
        self.max_sp = max_sp
        self.SP = SP
        self.ATK = ATK
        self.ATKRATE = ATKRATE
        self.HP_reg = HP_reg
        self.SP_reg = SP_reg
        self.Strenght = Strenght
        self.Agility = Agility
        self.Intelligence = Intelligence
        self.Constitution = Constitution
    
    def get_info(self):
        return SimpleNamespace(**self.__dict__)

def create_character():
    name = input("Karakterin adını giriniz: ")
    current_level = 1
    exp = 0
    stat_point = 5
    Strength = 10
    Agility = 10
    Intelligence = 10
    Constitution = 10

    # stat_point = int(current_level - 0) * 5
    # print("1 Strenght 2 Agility 3 Intelligence 4 Constituon ")
    # while stat_point > 0:
    #     choise = int(input("Lütfen stat puanlarınızı dağıtınız:"))
    #     if choise == 1:
    #         Strength += 1
    #     elif choise == 2:
    #         Agility += 1
    #     elif choise == 3:
    #         Intelligence += 1
    #     elif choise == 4:
    #         Constitution += 1
    #     else:
    #         print("Gecersiz giris")
    #         continue
    #     stat_point -= 1

    HP = 100 + Constitution * 10
    max_hp = HP
    HP_reg = 5 + Constitution * 0.1
    SP = 50 + Intelligence * 5
    max_sp = SP
    SP_reg = 2.5 + Intelligence * 0.05
    ATK = 20 + Strength * 2
    ATKRATE = 1 + Agility * 0.05

    character = Character(name, current_level,exp,stat_point, HP, max_hp, max_sp, SP, ATK,
                          ATKRATE, HP_reg, SP_reg, Strength, Agility, Intelligence, Constitution)

    print("Karakter oluşturuldu:")
    print(f"Adı: {character.name}")
    print(f"Seviyesi: {character.Level}")
    print(f"HP: {character.HP}")
    print(f"SP: {character.SP}")
    print(f"ATK: {character.ATK}")
    print(f"ATKRATE: {character.ATKRATE}")
    print(f"HP Regeneration: {character.HP_reg}")
    print(f"SP Regeneration: {character.SP_reg}")

    character_data = character.get_info()
    return character_data

def level(level :int, n1 = 1.2, base_xp = 100):
    gereken_exp = base_xp * (n1**level)
    gereken_exp = round(gereken_exp /5) *5
    return gereken_exp

def mob_exp_kazancı(mob_level):
    mob_exp = level(mob_level,1.2,50)
    return mob_exp
    
def Karakter_write(character_data):
    json_data = json.dumps(character_data.__dict__, indent=4)
    file = f"{character_data.name}.json"
    with open(file, "w") as file:
        file.write(json_data)


def create_giant(level):
    current_level = int(level)
    Strength = 10
    Agility = 2
    Intelligence = 5
    Constitution = 20

    stat_point = int(current_level) * 5
    stat_turn = 2
    while stat_point > 0:
        if stat_turn == 0:
            Strength += 1
            stat_turn = stat_turn+2
        else:
            Constitution += 1
            stat_turn = stat_turn-1

        stat_point -= 1

    HP = 100 + Constitution * 10
    max_hp = HP
    HP_reg = 5 + Constitution * 0.1
    SP = 50 + Intelligence * 5
    max_sp = SP
    SP_reg = 2.5 + Intelligence * 0.05
    ATK = 20 + Strength * 2
    ATKRATE = 1 + Agility * 0.05

    giant = Mob(f"{current_level} Level Giant ", current_level, HP, max_hp, max_sp,
                      SP, ATK, ATKRATE, HP_reg, SP_reg, Strength, Agility, Intelligence, Constitution)
    #giant_data = giant.get_info()
    return giant


def create_bird(level):
    current_level = int(level)
    Strength = 5
    Agility = 20
    Intelligence = 5
    Constitution = 5

    stat_point = int(current_level) * 5
    stat_turn = 3
    while stat_point > 0:
        if stat_turn == 0:
            Constitution += 1
            stat_turn = stat_turn+3
        if stat_turn == 1:
            Strength += 1
            stat_turn = stat_turn-1
        else:
            Agility += 1
            stat_turn = stat_turn-1

        stat_point -= 1

    HP = 100 + Constitution * 10
    max_hp = HP
    HP_reg = 5 + Constitution * 0.1
    SP = 50 + Intelligence * 5
    max_sp = SP
    SP_reg = 2.5 + Intelligence * 0.05
    ATK = 20 + Strength * 2
    ATKRATE = 1 + Agility * 0.05

    bird = Mob(f"{current_level} Level Bird ", current_level, HP, max_hp, max_sp,
                     SP, ATK, ATKRATE, HP_reg, SP_reg, Strength, Agility, Intelligence, Constitution)

    #bird_data = bird.get_info()
    return bird


def random_mob(kat):
    random_number = random.random()
    begin = 1 + (3 * (kat-1))
    end = 3 * kat 
    random_level = random.randint(begin,end)
    if random_number <= 0.5:
        return create_giant(random_level)
    else:
        return create_bird(random_level)



'''

#stat point basarısız gırıs ıcın contınue koyduk 12-07-2023

'''
