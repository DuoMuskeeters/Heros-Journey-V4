from Karakter import *
import os

def clear_console():
    os.system("cls" if os.name == "nt" else "clear")


def check_in(kontrol):
    if kontrol == "0":
        check = input("Önceki Dosyalara Erişmek için S ye basın.") 
        if check.lower() == "s":
            dosya_adi = input("Karakterin adını girin.")
            with open(f"{dosya_adi}.json" , "r") as file:
                your_character= json.load(file, object_hook=lambda d: SimpleNamespace(**d))
            return your_character

        else:    
                your_character = create_character()
                return your_character
    else:
        with open(f"Mehmet.json" , "r") as file:
            your_character= json.load(file, object_hook=lambda d: SimpleNamespace(**d))
        return your_character
    

def level(level :int, n1 = 1.2, base_xp = 100):
    gereken_exp = base_xp * (n1**level)
    gereken_exp = round(gereken_exp /5) *5
    return gereken_exp

def mob_exp_kazancı(mob_level):
    mob_exp = level(mob_level,1.2,50)
    return mob_exp