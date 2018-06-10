import os
import time


class NonRootError(Exception):
    pass


def clear():
    os.system("clear")


def checkfwstatus():
    fwstatus = os.system("ufw status")
    print(fwstatus)


def firewall():
    os.system('apt install ufw')
    os.system('ufw enable')
    checkfwstatus()
    # make sure to make something that will just scan the file for ports to be open
    allow = 'y'
    while allow == 'y':
        allow = input("\n\t Yeh wanna let anything in? (y/n)")
        if allow == 'y':
            port = input("\n\t What port number?")
            os.system('ufw allow ' + port)
            checkfwstatus()
    deny = 'y'
    while deny == 'y':
        deny = input("\n\t Wanna keep anythin out? (y/n)")
        if deny == 'y':
            port = input("\n\t What port number?")
            os.system('ufw deny' + port)
            checkfwstatus()


def setupsystem():
    os.system("apt install -y ufw")


def addusers():
    allow = 'y'
    administrators = []
    regulars = []
    while allow == 'y':
        clear()
        print("(R)(TM)(C) Security Editor User Addition Software")
        print("=================================================")
        print("Accounts to Elevate")
        print(administrators)
        print("Accounts to Add")
        print(regulars)
        reps = int(input("\nHow many users do you want to add? (0-100) \n\n\n>"))
        while reps > 0:
            clear()
            print("(R)(TM)(C) Security Editor User Addition Software")
            print("=================================================")
            print("Accounts to Elevate")
            print(administrators)
            print("Accounts to Add")
            print(regulars)
            usertype = input("Sudoer? (y/n)\n\n>")
            clear()
            if usertype == "y":
                administrators.append(input("Type in username\n\n>"))
                regulars.append(administrators[-1])
            elif usertype == "n":
                regulars.append(input("Type in username:\n\n>"))
            reps -= 1

        allow = "n"
    for regusers in regulars:
        os.system("adduser --disabled-password --gecos \"\" " + regusers)
        os.system("echo \"" + regusers + ":Cyb3rP@triot! | chpasswd")


def delusers():
    print("not done yet")


def addprogram():
    addmore = 'y'
    programnames = ["mysql-server", "openssh-server", "apache2", "samba"]
    while addmore == 'y':
        clear()
        print("(R)(TM)(C) Security Editor Program Addition Software")
        print("====================================================")
        addmore = input("\n Add more programs? (y/n) \n\n\n> ")
        if addmore == 'y':
            prognum = input(
                "\n\t Which Program? "
                "\n\t\t 1. SQL "
                "\n\t\t 2. SSH "
                "\n\t\t 3. Apache2 "
                "\n\t\t 4. Samba "
                "\n\t\t 5. Other "
                "\n\t\t 0. exit")
            if prognum == 1:
                os.system("apt install " + programnames[0])
            elif prognum == 2:
                os.system("apt install " + programnames[1])
            elif prognum == 3:
                os.system("apt install " + programnames[2])
            elif prognum == 4:
                os.system("apt install " + programnames[3])
            elif prognum == 5:
                unown = input("put in package name of the program")
                os.system("apt install " + unown)
            else:
                return


def delprogram():
    delmore = 'y'
    programnames = ["mysql-server", "openssh-server", "apache2", "samba"]
    while delmore == 'y':
        clear()
        print("(R)(TM)(C) Ubuntu Security Editor Program Deletion Software")
        print("===========================================================")
        delmore = input("\n Remove more programs? (y/n) \n\n\n> ")
        if delmore == 'y':
            prognum = input("\n\t Which Program? "
                            "\n\t\t 1. SQL "
                            "\n\t\t 2. SSH "
                            "\n\t\t 3. Apache2 "
                            "\n\n\t 4. Samba "
                            "\n\t\t 5. Other "
                            "\n\t\t 0. Exit")
            if prognum == 1:
                os.system("apt autoremove --purge " + programnames[0])
            elif prognum == 2:
                os.system("apt autoremove --purge " + programnames[1])
            elif prognum == 3:
                os.system("apt autoremove --purge " + programnames[2])
            elif prognum == 4:
                os.system("apt autoremove --purge " + programnames[3])
            elif prognum == 5:
                unown = input("put in package name of the program")
                os.system("apt autoremove --purge " + unown)
            else:
                return


setupsystem()
clear()
while True:
    print("Welcome to the (R)(TM)(C) Ubuntu Security Editor")
    print("Version 0.50 (C)Copyright NCS Corp 2018")
    print("=======================================================")
    print("(R)(TM)(C) is not liable for any damages to your system")
    print("\n\n Options:\n\n")
    choice = int(input(
        "\t 1. Firewall Setup "
        "\n\t 2. Add User "
        "\n\t 3. DeleteUser "
        "\n\t 4. AddProgram "
        "\n\t 5. DelProgram "
        "\n\t 0. Exit "
        "\n\n > "))
    if 1 == choice:
        firewall()
        time.sleep(1)
        clear()
    elif choice == 2:
        addusers()
        time.sleep(3)
        clear()
    elif choice == 4:
        addprogram()
        time.sleep(1)
        clear()
    elif choice == 5:
        delprogram()
        time.sleep(1)
        clear()
    elif choice == 0:
        clear()
        print("Exiting...")
        time.sleep(1)
        clear()
        exit()
    else:
        print("Incorrect Answer Choice")
