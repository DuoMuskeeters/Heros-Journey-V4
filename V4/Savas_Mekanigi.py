from Karakter import *
from Ekran import *
from Tower import *
import random


#karakter = Karakter_tanimlama("Mehmet.json")
clear_console()


def dodge(rate1: float, rate2: float):
    if rate1 >= rate2:
        return (rate1-rate2)/rate1
    else:
        return 0.0

def warrior(attacker : Character):
    if isinstance(attacker, Warrior):
        warrior_q = input("Saldırı girişi yapın: ")
        if warrior_q.lower() == "q" :
            skill_damage = attacker.heavy_strike()
            if attacker.ATK == skill_damage:
                print("Yetersiz SP")
            return skill_damage 
        elif warrior_q.lower() == "w" :
            print("Vitality Boost becerisi kullanıldı.")
            attacker.vitality_boost()
            print(f"{attacker.name} karakterinin güncellenmiş HP değeri: {attacker.HP}")
            print(f"{attacker.name} karakterinin güncellenmiş SP değeri: {attacker.SP}")
            return 0
        else :
            return attacker.ATK
    else:
        return attacker.ATK

def Savas_Mekanigi(karakter: Character, mob: Mob):
    karakter = Warrior.from_character(karakter)
    players = [karakter, mob]
    turn=0 
    
    while True:
        attacker = players[turn]
        defender = players[1-turn]
        dodge_rate = dodge(defender.ATKRATE, attacker.ATKRATE)
        HP_reg = int(attacker.HP_reg * attacker.HP)/100
        SP_reg = int(attacker.SP_reg * attacker.SP)/100
        if dodge_rate >= random.random():
            print(f"{attacker.name} saldırısı {defender.name} tarafından dodgelandı. ")
        else:
            damage = warrior(attacker)
            if damage != 0 :
                defender.HP = max(0, defender.HP - damage)
                print(f"{attacker.name} {defender.name}a {damage} hasar verdi")
                print(f"{defender.name} canı {defender.HP} ")
                attacker.HP = min(attacker.max_hp, attacker.HP + HP_reg)
                attacker.SP = min(attacker.max_sp, attacker.SP + SP_reg) 
        if defender.HP == 0:
            print(f"{defender.name} {attacker.name} tarafından katledildi\n")
            break
        turn = 1 - turn  
        input()
    #Savas sonucu
    if karakter.HP == 0:
        return False
    if mob.HP == 0:
        return True
    
def fight(karakter : Character , mob : Mob):
    Sonuc= Savas_Mekanigi(karakter, mob)
    if not Sonuc :
        print("Öldün.")
    else:
        karakter.exp = karakter.exp + mob_exp_kazancı(mob.Level)


def zindana_giris(karakter : Character, zindan : tower):
    input("Zindana doğru yürüyorsun içerisi tehlikelerle dolu dikkatli ol")
    kat = zindan.zindan_tanimlama(karakter.Level)
    input(f"Şu anki seviyen {karakter.Level}, {kat}. kata doğru ilerliyorsun.\n")
    while True:
        karakter.level_up()
        karakter.update_Stat()
        exit = input("")
        if exit == 'z':
            break
        mob= random_mob(kat)
        print(f"Karşına {mob.name} çıktı.")
        fight(karakter, mob)
        input("Yürümeye devam ettin.")


def MOB_Mekanigi(karakter: Mob, mob: Mob):
    players = [karakter, mob]
    turn=0 
    
    while True:
        attacker = players[turn]
        defender = players[1-turn]
        dodge_rate = dodge(defender.ATKRATE, attacker.ATKRATE)
        HP_reg = int(attacker.HP_reg * attacker.HP)/100
        SP_reg = int(attacker.SP_reg * attacker.SP)/100
        if dodge_rate >= random.random():
            print(f"{attacker.name} saldırısı {defender.name} tarafından dodgelandı. ")
        else:        
                defender.HP = max(0, defender.HP - attacker.ATK)
                print(f"{attacker.name} {defender.name}a {attacker.ATK} hasar verdi")
                print(f"{defender.name} canı {defender.HP} ")
                attacker.HP = min(attacker.max_hp, attacker.HP + int(HP_reg))
                attacker.SP = min(attacker.max_sp, attacker.SP + int(SP_reg)) 
        if defender.HP == 0:
            print(f"{defender.name} {attacker.name} tarafından katledildi\n")
            break
        turn = 1 - turn  
        input()
    #Savas sonucu
    if karakter.HP == 0:
        return False
    if mob.HP == 0:
        return True