from random import randint

info =[]

def random9Digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start,range_end)

def openAccount():
    first_name = input("First Name \n").capitalize()
    last_name = input("Last name \n").capitalize()
    info.append(first_name)
    info.append(last_name)

    #generate userID
    userID = random9Digits(9)
    print(f'This is your account ID: {userID}\n')
    info.append(userID)

    username = input("Pick a username, this will be the method you will login.\n")
    userpasswd = input("Pick a password, it will be used to log in the account.\n")
    info.append(username)
    info.append(userpasswd)

def logAccount():
    username2 = input("Insert your username \n")
    userpasswd2 = input("Insert your password \n")
    info.append(username2)
    info.append(userpasswd2)




while True:
    ans = input("Welcome, do you already have an account? Y/N \n").lower()
    if ans == "n":
        print("No problem, please provide the information to open the account \n")
        openAccount()
        break
    elif ans == "y":
        print("Please insert your username and password \n")
        logAccount()
        break
    else:
        print("Please insert Y or N \n")
        continue


        
        


        
    
    
    
