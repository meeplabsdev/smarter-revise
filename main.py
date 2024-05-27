import os
import os.path
import fade
from termcolor import colored, cprint

from resetPassword import run as resetPassword
from smarterRevise import run as smarterRevise


def clear():
    os.system("clear" if os.name == "posix" else "cls")


def logo():
    clear()
    print(
        fade.purplepink(
            """                                   
  ██████  ███▄ ▄███▓ ▄▄▄       ██▀███  ▄▄▄█████▓▓█████  ██▀███      ██▀███  ▓█████ ██▒   █▓ ██▓  ██████ ▓█████ 
▒██    ▒ ▓██▒▀█▀ ██▒▒████▄    ▓██ ▒ ██▒▓  ██▒ ▓▒▓█   ▀ ▓██ ▒ ██▒   ▓██ ▒ ██▒▓█   ▀▓██░   █▒▓██▒▒██    ▒ ▓█   ▀ 
░ ▓██▄   ▓██    ▓██░▒██  ▀█▄  ▓██ ░▄█ ▒▒ ▓██░ ▒░▒███   ▓██ ░▄█ ▒   ▓██ ░▄█ ▒▒███   ▓██  █▒░▒██▒░ ▓██▄   ▒███   
  ▒   ██▒▒██    ▒██ ░██▄▄▄▄██ ▒██▀▀█▄  ░ ▓██▓ ░ ▒▓█  ▄ ▒██▀▀█▄     ▒██▀▀█▄  ▒▓█  ▄  ▒██ █░░░██░  ▒   ██▒▒▓█  ▄ 
▒██████▒▒▒██▒   ░██▒ ▓█   ▓██▒░██▓ ▒██▒  ▒██▒ ░ ░▒████▒░██▓ ▒██▒   ░██▓ ▒██▒░▒████▒  ▒▀█░  ░██░▒██████▒▒░▒████▒
▒ ▒▓▒ ▒ ░░ ▒░   ░  ░ ▒▒   ▓▒█░░ ▒▓ ░▒▓░  ▒ ░░   ░░ ▒░ ░░ ▒▓ ░▒▓░   ░ ▒▓ ░▒▓░░░ ▒░ ░  ░ ▐░  ░▓  ▒ ▒▓▒ ▒ ░░░ ▒░ ░
░ ░▒  ░ ░░  ░      ░  ▒   ▒▒ ░  ░▒ ░ ▒░    ░     ░ ░  ░  ░▒ ░ ▒░     ░▒ ░ ▒░ ░ ░  ░  ░ ░░   ▒ ░░ ░▒  ░ ░ ░ ░  ░
░  ░  ░  ░      ░     ░   ▒     ░░   ░   ░         ░     ░░   ░      ░░   ░    ░       ░░   ▒ ░░  ░  ░     ░   
      ░         ░         ░  ░   ░                 ░  ░   ░           ░        ░  ░     ░   ░        ░     ░  ░
                                                                                       ░      m e e p l a b s                 
"""
        )
    )


def main():
    try:
        logo()
        cprint("Ctrl-C to exit at any point\n", "green")
        cprint("[1] Question Bot", "blue")
        cprint("[2] Password Reset Spam", "blue")

        c = input(colored("> ", "blue"))
        print()

        num = int(c)

        if num not in [1, 2]:
            cprint("Invalid selection, exiting...", "red")
            raise KeyboardInterrupt

        if num == 1:
            smarterRevise()
        elif num == 2:
            resetPassword()
        raise KeyboardInterrupt

    except KeyboardInterrupt:
        exit()


if __name__ == "__main__":
    try:
        open("C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe")
    except:
        cprint("Brave not found! Install it to continue.", "red")
        exit()

    main()
