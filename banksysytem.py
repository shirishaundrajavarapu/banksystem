class Bank:
    def __init__(self):
        self.accounts = {}
        

    def create_account(self, account_number, name, initial_balance):
        if account_number not in self.accounts:
            self.accounts[account_number] = {
                "name": name,
                "balance": initial_balance
            }
            print(f"Account created successfully for {name} with account number {account_number}")
        else:
            print(f"Account with account number {account_number} already exists.")

    def view_account(self, account_number):
        account = self.accounts.get(account_number)
        if account:
            print(f"Account Number: {account_number}")
            print(f"Account Holder: {account['name']}")
            print(f"Balance: ${account['balance']:.2f}")
        else:
            print(f"Account with account number {account_number} does not exist.")

    def deposit(self, account_number, amount):
        account = self.accounts.get(account_number)
        if account:
            account['balance'] += amount
            print(f"Deposited ${amount:.2f} into account {account_number}.")
        else:
            print(f"Account with account number {account_number} does not exist.")

    def withdraw(self, account_number, amount):
        account = self.accounts.get(account_number)
        if account:
            if account['balance'] >= amount:
                account['balance'] -= amount
                print(f"Withdrew ${amount:.2f} from account {account_number}.")
            else:
                print("Insufficient balance.")
        else:
            print(f"Account with account number {account_number} does not exist.")

    def check_balance(self, account_number):
        account = self.accounts.get(account_number)
        if account:
            print(f"Balance in account {account_number}: ${account['balance']:.2f}")
        else:
            print(f"Account with account number {account_number} does not exist.")

    def view_all_accounts(self):
        print("\nAll Bank Accounts:")
        for account_number, account_info in self.accounts.items():
            print(f"Account Number: {account_number}")
            print(f"Account Holder: {account_info['name']}")
            print(f"Balance: ${account_info['balance']:.2f}")
            print("-" * 20)


if __name__ == "__main__":
    bank = Bank()

    while True:
        print("\nBanking System Options:")
        print("1. Create New Account")
        print("2. View Account Details")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. Check Balance")
        print("6. View All Accounts")
        print("7. Quit")

        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            account_number = input("Enter Account Number: ")
            name = input("Enter Account Holder's Name: ")
            initial_balance = float(input("Enter Initial Balance: "))
            bank.create_account(account_number, name, initial_balance)

        elif choice == '2':
            account_number = input("Enter Account Number: ")
            bank.view_account(account_number)

        elif choice == '3':
            account_number = input("Enter Account Number: ")
            amount = float(input("Enter Deposit Amount: "))
            bank.deposit(account_number, amount)

        elif choice == '4':
            account_number = input("Enter Account Number: ")
            amount = float(input("Enter Withdrawal Amount: "))
            bank.withdraw(account_number, amount)

        elif choice == '5':
            account_number = input("Enter Account Number: ")
            bank.check_balance(account_number)

        elif choice == '6':
            bank.view_all_accounts()

        elif choice == '7':
            print("Exiting the Banking System. Goodbye!")
            break

        else:
            print("Invalid choice. Please choose a valid option (1-7).")






























#             print("welcome to sbi bank")
# class atm():
#     def __init__(self):
#         self.totalamount=150000
#         self.menu()
#         # self.pin=9999
#         # self.card="sbi card"
#     def menu(self):
#         print('''Atm menu
#         1.check balance
#         2.withdraw
#         3.deposit
#         4.ministatement
#         5.quit''')
#         # atmcard=input("insert your card:")
#         # pin=int(input("enter your pin:"))
#         # if pin==9999:
#         #     print("success go to menu")
#         # else:
#         #     print("pin is incorrect")
#         # self.menu()
#         option=int(input("enter your option:"))
#         if option==1:
#             print(f"your balance is:{self.totalamount}")
#         elif option==2:
#             print("withdraw")
#         elif option==3:
#             print(self.deposit())
#         elif option==4:
#             print(self.ministatement())
#         elif option==5:
#             print(self.quit())
#     def check_balance(self):
#         print(f"your balance is:{self.totalamount}")
#         self.menu()
#     def withdraw(self):
#         input_balance=int(input("enter amount to withdraw:"))
#         if  input_balance < self.totalamount:
#           self.totalamount= self.totalamount-input_balance
#           print(f"remaining balance is:{self.totalamount}")
#           self.menu()
#     def deposit(self):
#         input_deposit=int(input("enter amount to deposit:"))
#         self.totalamount=self.totalamount+input_deposit
#         print(f"your total balance after deposit is:{self.totalamount}")
#         self.menu()
#     def ministatement(self):
#         # input_ministatement=int(input("enter input:"))
#         if self.totalamount == self.totalamount:
#             print(f"ministatement is...the total balance:{self.totalamount}")
#     def quit(self):
#         print("thank u for visiting")
# # object creation
# obj=atm()
# obj.menu()
# obj.check_balance()
# obj.withdraw()
# obj.deposit()
# obj.ministatement()
# obj.quit()