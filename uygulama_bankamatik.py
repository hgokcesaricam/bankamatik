# Bank ATM Application

# Account information will be stored (dict)
# menu, withdraw_money, check_balance, deposit_money functions will be defined.
# If the requested withdrawal amount is not in the account, it will ask if the overdraft should be used.

accounts = [
{
    "name" : "Gökçe Sarıçam",
    "account_no" : "12345", #str
    "balance" : 20000, #int
    "overdraft" : 5000,
    "username" : "gokcesaricam",
    "password" : "1234",
    "overdraft_limit" : 10000
}
]

def register():
    print("\n=== REGISTER ===")
    name = input("Full Name: ")
    username = input("Username: ")

    # Username check (Already taken?)
    for account in accounts:
        if account["username"] == username:
            print("This username is already taken! Please try another.")
            return register()

    password = input("Password: ")
    account_no = str(len(accounts) + 10000)  # Auto account number
    balance = float(input("Enter initial balance: "))
    overdraft_limit = float(input("Enter overdraft limit: "))

    new_account = {
        "name": name,
        "account_no": account_no,
        "balance": balance,
        "overdraft": overdraft_limit,
        "username": username,
        "password": password,
        "overdraft_limit": overdraft_limit
    }

    accounts.append(new_account)
    print("\n Registration completed! You can now log in.")

def main_menu(account):
    while True:
        print("\n=== MAIN MENU ===")
        print(f"Hello, {account['name']}!")
        print("1 : Check Balance")
        print("2 : Withdraw Money")
        print("3 : Deposit Money")
        print("4 : Exit")

        choice = input("Select an option (1-4): ")

        if choice == "1":
            check_balance(account)
        elif choice == "2":
            withdraw_money(account)
        elif choice == "3":
            deposit_money(account)
        elif choice == "4":
            print("Exiting...")
            break    
        else:
            print("Invalid selection! (1-4)")
        if not continue_menu():
            print("Exiting...")
            break

def continue_menu():
    while True:
        selection = input("\nReturn to main menu? (Y/N): ").strip().upper()
        if selection == "Y":
            return True
        elif selection == "N":
            return False
        else:
            print("Invalid input! Please enter 'Y' or 'N'.")

def deposit_money(account):
    amount = float(input("Enter the amount to deposit: "))
    account["balance"] += amount
    print(f"Deposit successful. New balance: {account['balance']}")

def check_balance(account):
    print(f"Balance: {account['balance']}")
    print(f"Overdraft: {account['overdraft']}")

def withdraw_money(account):
    amount = float(input("Enter the amount to withdraw: "))

    if account["balance"] >= amount:
        account["balance"] -= amount
        print("You can take your money.")
    else:
        total = account["balance"] + account["overdraft"]
        if total >= amount:
            use_overdraft = input("Use overdraft? (Y/N): ").strip().upper()
            if use_overdraft == "Y":
                used_amount = amount - account["balance"]
                account["balance"] = 0
                account["overdraft"] -= used_amount
                print("You can take your money.")
            elif use_overdraft == "N":
                print("Not allowed, insufficient balance.")
            else:
                print("Invalid input.")
        else:
            print("Insufficient balance.")


def login():
     while True:
        print("\n=== LOGIN SCREEN ===")
        print("1: Log In")
        print("2: Register")
        print("3: Exit")

        choice = input("Select an option (1-3): ")

        if choice == "1":
            username = input("Username: ")
            password = input("Password: ")

            for account in  accounts:
                if account["username"] == username and account["password"] == password:
                    print("Login successful!")
                    main_menu(account)
                    return
            
            print("Incorrect username or password! Please try again.")
        elif choice == "2":
            register()

        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid input! Please select between 1-3.")


login()




