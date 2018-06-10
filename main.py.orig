import os


class NonRootError(Exception):
    pass


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


<<<<<<< HEAD
def users():
    allow = 'y'
    administrators = []
    regulars = []
    while allow == 'y':
        allow = input("\n\t Yeh wanna add anymore users? (except your own) (y/n)")
        if allow == 'y':
            usertype = input("admin or regular (a/r)")
            if usertype == "a":
                administrators.append(input("type in username"))
            elif usertype == "r":
                regulars.append(input("type in username"))




print("\n\n What scipt ye wanna run kiddo, I aint got all day.\n\n")
choice = int(input("\t 1. Firewall Setup \n\t 2. AddUser \n\t 3. DeleteUser\n\n\t Script Number: "))

if 1 == choice:
    firewall()
    os.system("clear")
if 2 == choice:
    users()
    os.system("clear")
else:
    print
    "Incorrect Answer Choice"
=======
def addprogram():
	addmore = 'y'
	programnames = ["mysql-server","openssh-server","apache2","samba"]
	while addmore == 'y':
		addmore = input("\n\t Add more programs y/n")
		if addmore == 'y':
			prognum = input("\n\t Which Program? \n\t\t 1. SQL \n\t\t 2. SSH \n\t\t 3. Apache2 \n\n\t 4. Samba \n\t\t 5. Other \n\t\t 0. exit")
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
					os.system("apt install "+unown)
				else:
					return
					
					
def delprogram():
	delmore = 'y'
	programnames = ["mysql-server","openssh-server","apache2","samba"]
	while delmore == 'y':
		delmore = input("\n\t Add more programs y/n")
		if delmore == 'y':
			prognum = input("\n\t Which Program? \n\t\t 1. SQL \n\t\t 2. SSH \n\t\t 3. Apache2 \n\n\t 4. Samba \n\t\t 5. Other \n\t\t 0. exit")
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
					os.system("apt autoremove --purge "+unown)
				else:
					return			
		
		
setupsystem()

print("\n\n What scipt ye wanna run kiddo, I aint got all day.\n\n")
while True:
	choice = int(input("\t 1. Firewall Setup \n\t 2. AddUser \n\t 3. DeleteUser \n\t 4. AddProgram \n\t 5. DelProgram \n\t 0. Exit \n\n\t Script Number: "))
	if 1 == choice:
		firewall()
		os.system("clear")
	elif choice == 4:
		addprogram()
		os.system("clear")
	elif choice == 5:
		delprogram()
		os.system("clear")
	elif choice == 0:
		exit()
	else:
		print
		"Incorrect Answer Choice"
>>>>>>> 047cb6fc51cfa0b768a93c07bc3be861f09c6bec
