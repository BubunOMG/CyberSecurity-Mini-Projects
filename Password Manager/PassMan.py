import hashlib
import getpass

password_manager = {}

def create_account():
    username = input("Enter Your Desired Username:")
    password = getpass.getpass("Enter Your Desired Password:")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    password_manager[username] = hashed_password
    print("Account Created Successfully !!")
    
def login():
    username = input("Enter Your Username :")
    password = getpass.getpass("Enter Your Password : ")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    
    if username in password_manager and password_manager[username] == hashed_password:
        print("Login Successful !!")
    else:
        print("Invalid Username or Password !!")
      
def main():
    while True:
        choice = input("Enter 1 to create an account, 2 to login, or 0 to exit: ")
        if choice == "1":
            create_account()
        elif choice == "2":
            login()
        elif choice == "0":
            break
        else:
            print("Invalid Choice..")

if __name__ == "__main__":
    main()
