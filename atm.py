class ATM:
    def __init__(self):
        self.users = {}  
        self.current_user = None  
        self.transaction_history = []  

    def login(self, user_id, pin):
        if user_id in self.users and self.users[user_id].pin == pin:
            self.current_user = self.users[user_id]
            return True
        else:
            return False

    def withdraw(self, amount):
        if self.current_user:
            if amount > 0 and amount <= self.current_user.balance:
                self.current_user.balance -= amount
                self.transaction_history.append(f"Withdrew ${amount} from {self.current_user.user_id}")
                print(f"Withdrew ${amount}. New balance: ${self.current_user.balance}")
            else:
                print("Invalid withdrawal amount.")
        else:
            print("No user logged in.")

    def deposit(self, amount):
        if self.current_user:
            if amount > 0:
                self.current_user.balance += amount
                self.transaction_history.append(f"Deposited ${amount} into {self.current_user.user_id}")
                print(f"Deposited ${amount}. New balance: ${self.current_user.balance}")
            else:
                print("Invalid deposit amount.")
        else:
            print("No user logged in.")

    def transfer(self, recipient_id, amount):
        if self.current_user:
            if recipient_id in self.users and recipient_id != self.current_user.user_id:
                if amount > 0 and amount <= self.current_user.balance:
                    self.current_user.balance -= amount
                    self.users[recipient_id].balance += amount
                    self.transaction_history.append(f"Transferred ${amount} to {recipient_id}")
                    print(f"Transferred ${amount} to {recipient_id}. New balance: ${self.current_user.balance}")
                else:
                    print("Invalid transfer amount.")
            else:
                print("Recipient not found or cannot transfer to yourself.")
        else:
            print("No user logged in.")
    
    def display_transaction_history(self):
        if self.current_user:
            print(f"Transaction History for User: {self.current_user.user_id}")
            for transaction in self.transaction_history:
                print(transaction)

            total_deposits = sum(float(transaction.split('$')[1].split()[0]) for transaction in self.transaction_history if "Deposited" in transaction)
            total_withdrawals = sum(float(transaction.split('$')[1].split()[0]) for transaction in self.transaction_history if "Withdrew" in transaction)

            print(f"Total Deposits: ${total_deposits}")
            print(f"Total Withdrawals: ${total_withdrawals}")
            print(f"Net Total: ${total_deposits - total_withdrawals}")
        else:
            print("No user logged in.")




class User:
    def __init__(self, user_id, pin, balance):
        self.user_id = user_id
        self.pin = pin
        self.balance = balance

def main():
    atm = ATM()

    user1 = User("12345", "1234", 1000)
    user2 = User("54321", "4321", 500)
    atm.users[user1.user_id] = user1
    atm.users[user2.user_id] = user2

    while True:
        print("Welcome to the ATM system")
        user_id = input("Enter your User ID: ")
        pin = input("Enter your PIN: ")

        if atm.login(user_id, pin):
            while True:
                print("\nSelect an option:")
                print("1. Transaction History")
                print("2. Withdraw")
                print("3. Deposit")
                print("4. Transfer")
                print("5. Quit")

                choice = input("Enter your choice: ")

                if choice == "1":
                    atm.display_transaction_history()
                elif choice == "2":
                    amount = float(input("Enter the amount to withdraw: "))
                    atm.withdraw(amount)
                elif choice == "3":
                    amount = float(input("Enter the amount to deposit: "))
                    atm.deposit(amount)
                elif choice == "4":
                    recipient_id = input("Enter recipient's User ID: ")
                    amount = float(input("Enter the amount to transfer: "))
                    atm.transfer(recipient_id, amount)
                elif choice == "5":
                    atm.quit()
                    break
                else:
                    print("Invalid choice. Please try again.")
        else:
            print("Invalid User ID or PIN. Please try again.")

if __name__ == "__main__":
    main()
