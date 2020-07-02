from user import User
from credential import Info

def create_account(F_name,L_name,S_name,E_mail):
    new_user = User(F_name,L_name,S_name,E_mail)
    return new_user

def create_credential(instagram,E_mail):
    new_cred = Info(instagram,E_mail)
    return new_cred

def save_account(user):
    user.save_user()

//def save_credentials(credentials):
    credential.save_info()

def display_users():
    return User.display_users()

def display_creds():
    return Info.display_info()

def main():

    print(" ")
    print("Hey there, Welcome to password generator!!")
    print(" ")
    print("To get started type in a short code as below!!")
    print("")
    print("")
    print("-")
    print("""Here to guide you!!
    cc - Create new _account
    ex - Exit password locker
    dac - Display Accoounts
    gs - Generate passwords""")
    print(" ")
    short_code = input() .lower()
    if short_code =='cc':
        print(" ")
        print("-")
        print("CREATE A NEW ACCOUNT!")
        print(" ")
        print(" ")
        print("what is your first name?..")
        print(" ")
        F_name =input()
        print("What is your middle name?..")
        print(" ")
        M_name= input()
        print("What is your surname name?..")
        print(" ")
        S_name= input()
        print("What is your email address?..")
        print(" ")
        E_mail= input()
        print ("what is your instagram password?..")
        print(" ")
        instagram =input()
        print("What is your email password?..")
        print(" ")
        E_mail= input()
        save_account(create_account(F_name,M_name,S_name,E_mail))
        print('\n')
        save_credentials(create_credential(instagram,E_mail))
        print('\n')
        print("-")
        print(f"New Account  {F_name } { M_name} { instagram } has been created")
        print('\n')
    elif short_code =='dac':
            if display_users():
                print(" ")
                print("The user name")
                print(" ")
                print('\n')
                for user in display_users():
                    print(f"{user.F_name}{user.M_name}{user.S_name}")
                for credential in display_creds():
                    print (f"{instagram}")
                    print(" ")

            else:
                    print('\n')
                    print("-")
                    print(" ")
                    print("PLEASE CREATE AN ACCOUNT ")
                    print("You have not created an account yet :( ")
                    print(" ")
    elif  short_code == 'gs':
        print(" ")
        print(" ")
        print("TO GENERATE A PASSWORD ADD IN YOUR FIRST NAME AND INSTAGRAM BELOW!!")
        print(" ")
        list_of_inputs = [c for c in input()]

        list_of_inputs.reverse()

        print (list_of_inputs)

    elif short_code == "ex":
        print("-")
        print(" ")
        print("Thank You")
        print("Chao Now")
        print(" ")
        print("-")

    else:
        print("-")
        print(" ")
        print("Retry!!")
        print(" ")
        print("Please choose from the option provided")
        print(" ")

if __name__ == '__main__':

    main()
