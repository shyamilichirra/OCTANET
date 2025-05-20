class ATM:
    def __init__(self):
        # Initialize an empty dictionary to store account information
        self.accounts = {}

    def create_account(self, account_number, pin, balance):
        # Create a new account with the given account number, PIN, and balance
        self.accounts[account_number] = {
            "pin": pin,
            "balance": balance,
            "transactions": []
        }

    def authenticate(self, account_number, pin):
        # Authenticate the user by checking if the account number and PIN match
        if account_number in self.accounts and self.accounts[account_number]["pin"] == pin:
            return True
        return False

    def check_balance(self, account_number):
        # Return the current balance of the account
        return self.accounts[account_number]["balance"]

    def withdraw(self, account_number, amount):
        # Withdraw cash from the account if sufficient balance is available
        if self.accounts[account_number]["balance"] >= amount:
            self.accounts[account_number]["balance"] -= amount
            self.accounts[account_number]["transactions"].append(f"Withdrawal: -${amount}")
            return True
        return False

    def deposit(self, account_number, amount):
        # Deposit cash into the account
        self.accounts[account_number]["balance"] += amount
        self.accounts[account_number]["transactions"].append(f"Deposit: +${amount}")
        return True

    def change_pin(self, account_number, new_pin):
        # Change the PIN of the account
        self.accounts[account_number]["pin"] = new_pin
        return True

    def transaction_history(self, account_number):
        # Return the transaction history of the account
        return self.accounts[account_number]["transactions"]

def main():
    atm = ATM()
    atm.create_account("12345", "1234", 1000.0)

    while True:
        print("\nWelcome to the ATM Simulator!")
        print("1. Login")
        print("2. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            account_number = input("Enter your account number: ")
            pin = input("Enter your PIN: ")

            if atm.authenticate(account_number, pin):
                while True:
                    print("\nAccount Menu:")
                    print("1. Check Balance")
                    print("2. Withdraw Cash")
                    print("3. Deposit Cash")
                    print("4. Change PIN")
                    print("5. Transaction History")
                    print("6. Logout")
                    choice = input("Enter your choice: ")

                    if choice == "1":
                        print(f"Your balance is: ${atm.check_balance(account_number)}")
                    elif choice == "2":
                        amount = float(input("Enter the amount to withdraw: "))
                        if atm.withdraw(account_number, amount):
                            print("Withdrawal successful!")
                        else:
                            print("Insufficient balance!")
                    elif choice == "3":
                        amount = float(input("Enter the amount to deposit: "))
                        atm.deposit(account_number, amount)
                        print("Deposit successful!")
                    elif choice == "4":
                        new_pin = input("Enter your new PIN: ")
                        atm.change_pin(account_number, new_pin)
                        print("PIN changed successfully!")
                    elif choice == "5":
                        print("Transaction History:")
                        for transaction in atm.transaction_history(account_number):
                            print(transaction)
                    elif choice == "6":
                        break
                    else:
                        print("Invalid choice. Please try again.")
            else:
                print("Invalid account number or PIN.")
        elif choice == "2":
            print("Thank you for using the ATM Simulator!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main() 
