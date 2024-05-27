from termcolor import colored, cprint
from alive_progress import alive_bar
import os.path
import pwinput
import time
import fade
import os

import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def clear():
    os.system("clear" if os.name == "posix" else "cls")


def advance(driver, bar, numQuestions, course):
    driver.get("https://smartrevise.online/student/advance/index/" + course)

    complete = 0
    while complete < numQuestions:
        time.sleep(0.6)
        try:
            elem = WebDriverWait(driver, 300).until(
                EC.presence_of_element_located((By.ID, "kt_content"))
            )
        finally:
            try:
                qC = driver.execute_script(
                    """
    function doAnswer() {
        if (location.href.startsWith("https://smartrevise.online/student/advance/")) {
            setTimeout(() => {
                location.reload();
            }, 9000);
        }
        if (location.href.startsWith("https://smartrevise.online/student/advance/index/")) {
            document.querySelector("#SuppliedAnswer").value = "-";
            document.querySelector("#questionPortlet > form > div.kt-portlet__foot.pt-0 > div.row.justify-content-end > div > button").click();
            return 0;
        }
        if (location.href.startsWith("https://smartrevise.online/student/advance/MarkAnswer/")) {
            if (document.querySelector("#btnShowUnguided")) document.querySelector("#btnShowUnguided").click();
            let marksArray = document.querySelector("#formUnguided > div > label").innerText.split(" ");
            let marks = marksArray[marksArray.length - 1].replace("):", "");
            document.querySelector("#UnguidedMarks").value = marks;
            document.querySelector("#btnUnguidedFinish").click();
            return 1;
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


def terms(driver, bar, numQuestions, course):
    driver.get("https://smartrevise.online/student/reviseterminology/index/" + course)
    try:
        elem = WebDriverWait(driver, 300).until(
            EC.presence_of_element_located((By.ID, "kt_content"))
        )
    finally:
        driver.execute_script(
            """
document.querySelector("#chkSad").checked = true;
document.querySelector("#chkMeh").checked = true;
document.querySelector("#chkHappy").checked = true;
document.querySelector("#chkUnassessed").checked = true;
document.querySelector("#btnBuildDeck").click();                          
"""
        )

    complete = 0
    while complete < numQuestions:
        time.sleep(4)
        try:
            elem = WebDriverWait(driver, 300).until(
                EC.presence_of_element_located((By.ID, "kt_content"))
            )
        finally:
            try:
                answerBox = driver.find_element(by=By.ID, value="activeAnswer")
                answerBox.send_keys("-")
                qC = driver.execute_script(
                    """
    function doAnswer() {
        document.querySelector("#activeAnswer").value = "-";
        document.querySelector("#btnFlip").click();
        setTimeout(() => { document.querySelector("button[data-conf='3'").click(); }, 500);
        setTimeout(() => { document.querySelector("#btnNext").click(); }, 1500);
        return 1;
    }

    return (doAnswer() || 0);
    """
                )
                complete += qC or 0
                if qC == 1:
                    bar()
                else:
                    cprint("Unknown error", "red")
            except:
                pass

    time.sleep(2)


def login(driver):
    cprint("Email", "blue")
    email = input(colored("> ", "blue"))
    cprint("Password", "blue")
    password = pwinput.pwinput(prompt=colored("> ", "blue"))
    print()

    driver.get("https://smartrevise.online/Account/Login")
    driver.execute_script(
        f"""
document.querySelector("#Email").value = "{email}";
document.querySelector("#Password").value = "{password}";
document.querySelector("#btnLogin").click();
"""
    )
    if driver.current_url != "https://smartrevise.online/student/home/Index":
        cprint("Login failed, exiting...", "red")
        return -1

    course = driver.execute_script(
        """
courses = [];
document.querySelectorAll("#activeCoursesDeck > div > a").forEach(card => {
    courses.push(card.href.split("/").findLast(() => true));
});
return courses;
"""
    )[0]
    return course


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

        driver = uc.Chrome(options=options, service_log_path=os.devnull)
        course = login(driver)
        if course == -1:
            raise KeyboardInterrupt

        logo()
        cprint("Usage: <type<number>>, [type<number>], [type<number>], ...\n", "green")
        cprint("[T]erms", "blue")
        cprint("[A]dvance", "blue")

        choices = input(colored("> ", "blue")).split(",")
        print()

        for c in choices:
            c = c.strip().lower()
            if len(c) < 2:
                cprint("Invalid selection, exiting...", "red")
                raise KeyboardInterrupt

            type = c[0]
            num = int(c[1:])

            if type not in ["t", "a"]:
                cprint("Invalid selection, exiting...", "red")
                raise KeyboardInterrupt

            with alive_bar(num) as bar:
                if type == "t":
                    terms(driver, bar, num, course)
                elif type == "a":
                    advance(driver, bar, num, course)

        raise KeyboardInterrupt

    except KeyboardInterrupt:
        try:
            driver.close()
        except UnboundLocalError:
            print()


def run():
    try:
        open("C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe")
    except:
        cprint("Brave not found! Install it to continue.", "red")
        exit()

    options = uc.ChromeOptions()
    options.add_argument("--disable-brave-extension")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-notifications")
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.binary_location = (
        "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
    )

    main(options)
