ID = []
PW = []
NAME = []

def SIGNUP():
    global ID, PW, NAME
    ID_L = (input("Please enter an ID for your new account "))

    if ID.count(ID_L) != 0:
        print("ID already exists")
        SIGNUP()
    else:
        Password_L = input("Please type of password for the account ")
        Name_L= input("Please state your real name, but don't ask why, just do it ")
        ID.append(ID_L)
        PW.append(Password_L)
        NAME.append(Name_L)
        
    print("Is this right?")
    print("ID:", ID_L, "    Password:", Password_L, "    Name:", Name_L)



def LOGIN():
    global ID, PW, NAME

    if ID == []:
        print("Don't even think about it >:(")
        print("Sending you back...")
        return
    
    ID_E = input("Enter your ID: ")
    if ID.count(ID_E) == 0:
        print("ID does not exist. Try again")
        LOGIN()
    else:
        while True:
            PW_E = input("Enter the password: ")
            if PW_E != PW[ID.index(ID_E)]:
                print("Please try again")
            else:
                break

        print("Welcome, ", NAME[ID.index(ID_E)]) 

def MAIN():
    while True:
        print("""1. Sign up
2. Log in""")
        choice = int(input("What do you want to do? "))

        if choice == 1:
            SIGNUP()
        else:
            LOGIN()

        A = input("Would you like to continue? (Y/N) ")
        if A.upper() == "Y":
            pass
        else:
            break
    

if __name__ == "__main__":
    MAIN()