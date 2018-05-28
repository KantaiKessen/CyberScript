import os


class NonRootError(Exception):
    pass


def checkfwstatus():
    fwstatus = os.system("ufw status")
    print(fwstatus)


def firewall():
    if not os.getuid != 0:
        raise NonRootError("You must run as root")
    else:
        os.system('apt install ufw')
        os.system('ufw enable')
        checkfwstatus()
        # make sure to make something that will just scan the file for ports to be open
        allow = 'y'
        while allow == 'y':
            allow = input("\n\t Add allowed ports to firewall (y/n)")
            if allow == 'y':
                port = input("\n\t What port number?")
                os.system('ufw allow ' + port)
                checkfwstatus()
        deny = 'y'
        while deny == 'y':
            deny = input("\n\t Add denied ports to firewall (y/n)")
            if deny == 'y':
                port = input("\n\t What port number?")
                os.system('ufw deny' + port)
                checkfwstatus()


print("\n\n In Compliance with the rules of Cyber Patriot, which Script Do You wish to Run?\n\n")
choice = int(input("\t 1. Firewall Setup \n\t 2. AddUser \n\t 3. DeleteUser\n\n\t Script Number: "))

if 1 == choice:
    firewall()
    os.system("clear")
else:
    print
    "Incorrect Answer Choice"
