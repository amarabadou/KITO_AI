import hashlib
import os
import sys
from colorama import Fore

def verify_user():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"\n{Fore.MAGENTA}>>> KITO ")
    pwd = input(f"{Fore.WHITE}ENTER ACCESS CODE: ").strip()
    # THE ACCESS CODE IS  'CS1'
    if hashlib.md5(pwd.encode()).hexdigest() != "8ea4c9ac938645ff943aeb7a9c2bc060":
        return False
    return True