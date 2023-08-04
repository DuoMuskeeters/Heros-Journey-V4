from types import SimpleNamespace
import json
import random
import os


class State:
    def __init__(
        self,
        name: str,
        Level: int,
        stat_point: int,
        HP: int,
        max_hp: int,
        max_sp: int,
        SP: int,
        ATK: int,
        ATKRATE: float,
        HP_reg: float,
        Armor: float,
        SP_reg: float,
        m_resist: float,
        Strength: int,
        Agility: int,
        Intelligence: int,
        Constitution: int,
    ):
        self.name = name
        self.Level = Level
        self.stat_point = stat_point
        self.HP = HP
        self.max_hp = max_hp
        self.max_sp = max_sp
        self.SP = SP
        self.ATK = ATK
        self.ATKRATE = ATKRATE
        self.HP_reg = HP_reg
        self.Armor = Armor
        self.SP_reg = SP_reg
        self.m_resist = m_resist
        self.Strength = Strength
        self.Agility = Agility
        self.Intelligence = Intelligence
        self.Constitution = Constitution

        def __dict__(self):
            return self.__dict__


class Canlı:
    def __init__(self, state: State):
        self.state = state


class Character(Canlı):
    def __init__(self, state: State, exp=0):
        self.state = state
        self.exp = exp

    def get_info(self):
        return SimpleNamespace(**self.__dict__)

    def karakter_read(self):
        with open(f"{self.state.name}.json", "r") as file:
            karakter_data = json.load(file)
        return Character(State(**karakter_data["state"]), karakter_data["exp"])

    def karakter_write(self):
        json_data = json.dumps(
            {"state": self.state.__dict__, "exp": self.exp}, indent=4
        )
        with open(f"{self.state.name}.json", "w") as file:
            file.write(json_data)

    def __str__(self) -> str:
        return f"{self.state.name}(HP={self.state.HP}, SP={self.state.SP})"

    def exp_boost(self, exp):
        self.exp = self.exp + exp

    def level_up(self):
        gereken_exp = level(self.state.Level)
        while True:
            if self.exp >= gereken_exp:
                self.state.Level = self.state.Level + 1
                self.exp = self.exp - gereken_exp
                self.state.stat_point = self.state.stat_point + 5
            else:
                break
        self.calculate_power()

    def update_Stat(self):
        if not self.state.stat_point:
            return
        # TODO burası yarrak gibi
        print(f"{self.state.stat_point} stat puanların var.")
        print("1 Strength 2 Agility 3 Intelligence 4 Constituon ")
        while self.state.stat_point > 0:
            choice = input("Lütfen stat puanlarınızı dağıtınız:")
            if choice == "1":
                self.state.Strength += 1
            elif choice == "2":
                self.state.Agility += 1
            elif choice == "3":
                self.state.Intelligence += 1
            elif choice == "4":
                self.state.Constitution += 1
            else:
                print("Gecersiz giris")
                continue
            self.state.stat_point -= 1

    def calculate_power(self):
        self.state.HP = 100 + self.state.Constitution * 10
        self.state.HP_reg = 5 + self.state.Constitution * 0.1
        self.state.SP = 50 + self.state.Intelligence * 5
        self.state.SP_reg = 2.5 + self.state.Intelligence * 0.05
        self.state.ATK = 20 + self.state.Strength * 2
        self.state.ATKRATE = 1 + self.state.Agility * 0.05
        # return yok


class Warrior(Character):
    def heavy_strike(self):
        if self.state.SP > 50 or self.state.SP == 50:
            strike_damage = self.state.ATK * 2
            self.state.SP = self.state.SP - 50
            return strike_damage

        return self.state.ATK

    def vitality_boost(self):
        hp = int(self.state.max_hp * 0.35 + self.state.HP)
        sp = int(self.state.max_sp * 0.35 + self.state.SP)
        self.state.HP = min(hp, self.state.max_hp)
        self.state.SP = min(sp, self.state.max_sp)


class Mob(Canlı):
    pass


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
    Armor = Constitution / (Constitution + 100)
    SP = 50 + Intelligence * 5
    max_sp = SP
    SP_reg = 2.5 + Intelligence * 0.05
    m_resist = Constitution / (Constitution + 100)
    ATK = 20 + Strength * 2
    ATKRATE = 1 + Agility * 0.05

    # buradaki karisikligi coz
    character_state = State(
        name,
        current_level,
        stat_point,
        HP,
        max_hp,
        max_sp,
        SP,
        ATK,
        ATKRATE,
        HP_reg,
        Armor,
        SP_reg,
        m_resist,
        Strength,
        Agility,
        Intelligence,
        Constitution,
    )
    character = Character(character_state, exp)

    print("Karakter oluşturuldu:")
    print(f"Adı: {character.state.name}")
    print(f"Seviyesi: {character.state.Level}")
    print(f"HP: {character.state.HP}")
    print(f"SP: {character.state.SP}")
    print(f"ATK: {character.state.ATK}")
    print(f"ATKRATE: {character.state.ATKRATE}")
    print(f"HP Regeneration: {character.state.HP_reg}")
    print(f"SP Regeneration: {character.state.SP_reg}")

    character.karakter_write()
    return character


# zorluk exponanasiyel arttigi icin bu algoritma 35-40 seviye arasina kadar ise yarar.
def level(level: int, n1=1.2, base_xp=100):
    n1 = n1 + (0.002) * int(level)
    gereken_exp = base_xp * (n1**level)
    gereken_exp = round(gereken_exp / 5) * 5
    return gereken_exp


def mob_exp_kazancı(mob_level, n1=1.2, base_exp=50):
    mob_exp = base_exp * (n1**mob_level)
    mob_exp = round(mob_exp / 5) * 5
    return mob_exp


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
            stat_turn = stat_turn + 2
        else:
            Constitution += 1
            stat_turn = stat_turn - 1

        stat_point -= 1

    HP = 100 + Constitution * 10
    max_hp = HP
    HP_reg = 5 + Constitution * 0.1
    Armor = Constitution / (Constitution + 100)
    SP = 50 + Intelligence * 5
    max_sp = SP
    SP_reg = 2.5 + Intelligence * 0.05
    m_resist = Constitution / (Constitution + 100)
    ATK = 20 + Strength * 2
    ATKRATE = 1 + Agility * 0.05


    giant_state = State(
        f"{current_level} Level Giant ",
        current_level,
        stat_point,
        HP,
        max_hp,
        max_sp,
        SP,
        ATK,
        ATKRATE,
        HP_reg,
        Armor,
        SP_reg,
        m_resist,
        Strength,
        Agility,
        Intelligence,
        Constitution,
    )
    giant = Mob(giant_state)
    # giant_data = giant.get_info()
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
            stat_turn = stat_turn + 3
        if stat_turn == 1:
            Strength += 1
            stat_turn = stat_turn - 1
        else:
            Agility += 1
            stat_turn = stat_turn - 1

        stat_point -= 1

    HP = 100 + Constitution * 10
    max_hp = HP
    HP_reg = 5 + Constitution * 0.1
    Armor = Constitution / (Constitution + 100)
    SP = 50 + Intelligence * 5
    max_sp = SP
    SP_reg = 2.5 + Intelligence * 0.05
    m_resist = Constitution / (Constitution + 100)
    ATK = 20 + Strength * 2
    ATKRATE = 1 + Agility * 0.05


    bird_state = State(
        f"{current_level} Level Bird ",
        current_level,
        stat_point,
        HP,
        max_hp,
        max_sp,
        SP,
        ATK,
        ATKRATE,
        HP_reg,
        Armor,
        SP_reg,
        m_resist,
        Strength,
        Agility,
        Intelligence,
        Constitution,
    )

    bird = Mob(bird_state)

    # bird_data = bird.get_info()
    return bird


def random_mob(kat):
    random_number = random.random()
    begin = 1 + (3 * (kat - 1))
    end = 3 * kat
    random_level = random.randint(begin, end)
    if random_number <= 0.5:
        return create_giant(random_level)
    else:
        return create_bird(random_level)


def clear_console():
    os.system("cls" if os.name == "nt" else "clear")


def check_in(kontrol):
    if kontrol == "0":
        check = input("Önceki Dosyalara Erişmek için S ye basın.")
        if check.lower() == "s":
            dosya_adi = input("Karakterin adını girin.")
            with open(f"{dosya_adi}.json", "r") as file:
                character_data = json.load(file)
            return Character(State(**character_data["state"]), character_data["exp"])
        else:
            your_character = create_character()
            return your_character
    else:
        with open(f"Messi2.json", "r") as file:
            character_data = json.load(file)
        return Character(State(**character_data["state"]), character_data["exp"])
