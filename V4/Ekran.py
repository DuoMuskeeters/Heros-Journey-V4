from Karakter import *
import json
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
        with open("Mehmet.json" , "r") as file:
            your_character= json.load(file, object_hook=lambda d: SimpleNamespace(**d))
        return your_character