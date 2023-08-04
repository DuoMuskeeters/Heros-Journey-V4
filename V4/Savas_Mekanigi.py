from Karakter import *
from Tower import *
import random
import time


def dodge(rate1: float, rate2: float):
    if rate1 >= rate2:
        return (rate1 - rate2) / rate1
    else:
        return 0.0


def warrior(attacker: Canlı):
    if isinstance(attacker, Warrior):
        warrior_q = input("Saldırı girişi yapın: ")
        if warrior_q.lower() == "q":
            skill_damage = attacker.heavy_strike()
            if attacker.state.ATK == skill_damage:
                print("Yetersiz SP")
            return skill_damage
        elif warrior_q.lower() == "w":
            print("Vitality Boost becerisi kullanıldı.")
            attacker.vitality_boost()
            print(
                f"{attacker.state.name} karakterinin güncellenmiş HP değeri: {attacker.state.HP}"
            )
            print(
                f"{attacker.state.name} karakterinin güncellenmiş SP değeri: {attacker.state.SP}"
            )
            return 0
        elif warrior_q.lower() == "b":
            return False
    return attacker.state.ATK


def Savas_Mekanigi(karakter: Canlı, mob: Canlı):
    players = [karakter, mob]
    karakter = Warrior(karakter.state)
    turn = 0

    while True:
        attacker = players[turn]
        defender = players[1 - turn]
        dodge_rate = dodge(defender.state.ATKRATE, attacker.state.ATKRATE)
        HP_reg = int(attacker.state.HP_reg * attacker.state.HP) / 100
        SP_reg = int(attacker.state.SP_reg * attacker.state.SP) / 100
        if dodge_rate >= random.random():
            print(
                f"{attacker.state.name} saldırısı {defender.state.name} tarafından dodgelandı. "
            )
        else:
            damage = warrior(attacker)
            damage = int(damage * (1-defender.state.Armor))
            Blok = int(damage * (defender.state.Armor))
            if damage != 0:
                defender.state.HP = max(
                    0, int(defender.state.HP - damage)
                )
                print(
                    f"{attacker.state.name} {defender.state.name}a {damage}(Blok ({Blok})) hasar verdi"
                )
                print(f"{defender.state.name} canı {defender.state.HP} ")
                attacker.state.HP = min(
                    attacker.state.max_hp, int(attacker.state.HP + HP_reg)
                )
                attacker.state.SP = min(
                    attacker.state.max_sp, int(attacker.state.SP + SP_reg)
                )
        if defender.state.HP == 0:
            print(
                f"{defender.state.name} {attacker.state.name} tarafından katledildi\n"
            )
            break
        turn = 1 - turn
        input()


def fight(karakter: Canlı, mob: Canlı):
    karakter = Warrior(karakter.state)
    Savas_Mekanigi(karakter, mob)
    if karakter.state.HP == 0:
        print("Öldün.")
        return False
    else:
        return True


def zindana_giris(karakter: Character, zindan: tower):
    input("Zindana doğru yürüyorsun içerisi tehlikelerle dolu dikkatli ol")
    kat = zindan.zindan_tanimlama(karakter.state.Level)
    input(f"Şu anki seviyen {karakter.state.Level}, {kat}. kata doğru ilerliyorsun.\n")
    while True:
        karakter.level_up()
        karakter.update_Stat()
        exit = input("")
        if exit == "z":
            break
        mob = random_mob(kat)
        print(f"Karşına {mob.state.name} çıktı.")
        sonuc = fight(karakter, mob)
        if sonuc == False:
            print("Yeniden Doğuyorsun.")
            karakter.exp = karakter.exp * 0.75
            time.sleep(5)
            print("Yeniden doğdun.")
        elif sonuc == True:
            input("Yürümeye devam ettin.")
            karakter.exp = karakter.exp + mob_exp_kazancı(mob.state.Level)
