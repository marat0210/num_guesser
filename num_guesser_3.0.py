"""This is version 3.0 of num_guesser program."""

"""New features in version 3.0:
1. Added user account function. User will have to create his own account if he wants to play.
"""

import random


def create_login():
    """Create user's login."""
    account = {}     #user's account is stored here.
    login = input("Create your own login: ")
    account.update({'login':login})
    print("Your login is saved: ")
     
    
def password():
    """Store User's password."""
    password = {}
    return password

p = password()


    


def letter_password():
    """Ask user to create a password that only contains letters."""
    letter_password = str(input("Type the letter password, its max " 
    "length is 8 characters and its min length is 5 characters."))

    letter = [str(l) for l in str(letter_password)]    #creating a list out of user input
    l = len(letter)     #finding the length of the list letter.
    
    while l >= 5 and l <= 8:
        p.update({'password':letter_password})
        print("Your password is saved now.")
        break
    #If the condition is false then we make another loop until the condition is true
    while l < 5 and l > 8:
        while True:
            print("Error. Try again!")
            letter_password = str(input("Create your password, using only letters,  ts max " 
            "length is 8 characters and its min length is 5 characters."))
            letter = [str(l) for l in str(letter_password)]    #creating a list out of user input
            l = len(letter)     #finding the length of the list letter.
            if l >= 5 and l <= 8:
                p.update({'password':letter_password})
                print("Your password is saved now.")
            break
        break

    



def mixed_password():
    """Create password that will contain digits and letters."""
    mixed_password = input("Create your password. Max length is 8, min length is 5:  ")
    mixed = [(m) for m in (mixed_password)]
    l = len(mixed)
    while l >= 5 and l <= 8:
        p.update({'password':mixed_password})
        print("Your password ia saved now.")
        break
    #If the condition is false then we make another loop until the condition is true
    while l < 5 and l > 8:
        print("Error. Try again.")
        while True:
            mixed_password = input("Create your password. Max length is 8, min length is 5:  ")
            mixed = [(m) for m in (mixed_password)]
            l = len(mixed)
            if l >= 5 and l <= 8:
                p.update({'password':mixed_password})
                print("Your password is saved now.")
            break
        break







def create_password():
    """Create user's password."""
    password()     #call password function that stores user's password
    
    password_choice = input("In what way you want your password to be?: "
    "\nleter password\nmixed password(digits and leters combined together): ")
    
    if password_choice == 'letter password':
        letter_password()
    elif password_choice  == 'mixed password':
        mixed_password()
    else:
        print("Make sure your input doesn't contain any mistakes.")
        while True:
            print("Try again...")
            create_password()
        

    




"""Making a game. User can play it if he logs in into his account."""
 def num_guesser():
    """Guess the number in a given range."""
    x = int(input("Type the starting number: "))
    y = int(input("Type the ending number: "))
    num = int(input("Type the number from between the range of x, y and I'll try to guess it: "))
    num_guesser = random.randint(x, y)
    while num >= x and num <= y:
        tryings = 1
        while num_guesser != num:
            num_guesser = random.randint(x, y)  
            tryings += 1
            if num_guesser == num:
                print("The number is " + str(num_guesser))
                print("The amount of attempts: " + str(tryings))
                break
    while num < x or num > y:
        print("Seems that you've made a mistake. Try again...")
        x = int(input("Type the starting number: "))
        y = int(input("Type the ending number: "))
        num = int(input("Type the number from between the range of x, y and I'll try to guess it: "))
        num_guesser = random.randint(x, y)
        tryings = 1
        while num_guesser != num:
            num_guesser = random.randint(x, y)  
            tryings += 1
            if num_guesser == num:
                print("The number is " + str(num_guesser))
                print("The amount of attempts: " + str(tryings))
                break
        



"""Creating log in system. User will have to log in into his account if he wants to play a game."""

def log_in():
    """Ask User to log in into his account."""
    choice = input("Do you want to log in into your account?: ")
    if choice == 'yes':
        user_password = input("Your password: ")   #asking user to type his password.
        a = p.get('password')           #making a string out of the dict value.
        while user_password == a:
            print("You've logged in!")
            num_guesser()
            break
        while user_password != a:
            print("Your password is incorrect.")
            while True:
                print("Try again.")
                user_password = input("Your password: ")
                a = p.get('password')
                if user_password == a:
                    print("You've logged in!")
                break
            break
    elif choice == 'no':
        while True:
            q = input("Press q to exit the program: ")
            if q == 'q':
                q.quit()
            else:
                q.quit()
            break
    else:
        print("Error. Make sure there are no typos in your input.")
        





create_login()
create_password()
log_in()



                
        
        
    
 
    

    



