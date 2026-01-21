accounts = []

def create_account():
    account_number = input("Enter account number: ")
    name = input("Enter account holder name: ")
    balance = float(input("Enter initial deposit: "))

    account = {
        "account_number": account_number,
        "name": name,
        "balance": balance
    }

    accounts.append(account)
    print("Account created successfully!")

def deposit():
    account_number = input("Enter account number: ")
    amount = float(input("Enter deposit amount: "))

    for account in accounts:
        if account["account_number"] == account_number:
            account["balance"] += amount
            print("Deposit successful!")
            return

    print("Account not found!")

def withdraw():
    account_number = input("Enter account number: ")
    amount = float(input("Enter withdrawal amount: "))

    for account in accounts:
        if account["account_number"] == account_number:
            if amount <= account["balance"]:
                account["balance"] -= amount
                print("Withdrawal successful!")
            else:
                print("Insufficient balance!")
            return

    print("Account not found!")

def check_balance():
    account_number = input("Enter account number: ")

    for account in accounts:
        if account["account_number"] == account_number:
            print(f"Account Balance: ₦{account['balance']}")
            return

    print("Account not found!")

def main():
    while True:
        print("\n--- Simple Banking System ---")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            create_account()
        elif choice == "2":
            deposit()
        elif choice == "3":
            withdraw()
        elif choice == "4":
            check_balance()
        elif choice == "5":
            print("Thank you for using the banking system.")
            break
        else:
            print("Invalid option!")

main()
