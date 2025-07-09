import time

class BankAccount:
    account_counter = 1000 #default account number starts
    def __init__(self, name, password, balance=0):
        self.name = name
        self.password = password
        self.balance = balance
        self.account_number = BankAccount.account_counter
        BankAccount.account_counter += 1 #increment each new account number by 1

    def deposit(self, amount):
        self.balance += amount
        return f'You have deposited ${amount}. Your new balance is ${self.balance}.'

    def withdraw(self, amount):
        if self.balance < amount:
            return 'You do not have enough funds to withdraw.'
        else:
            self.balance -= amount
            return f'You have withdrawn ${amount}. Your new balance is ${self.balance}.'

    def show_balance(self):
        return f'Your balance is ${self.balance}.'

    def show_details(self):
        password_length = '*' * len(self.password)
        return f'''
        Name: {self.name}
        Account Number: {self.account_number}
        Password: {password_length}
        Balance: {self.balance}
        '''
    
accounts = {} #dictionary to store accounts once instantiated

bot = 'BankBot:'
print(f'{bot} Welcome to Mat\'s bank!')
time.sleep(1)

while True: #pre-login menu
    print(f'{bot} Please choose an option below: ')
    time.sleep(0.5)
    print('1. Create Account | 2. Log In | 3. Exit')
    user_input = input('You: ')
    time.sleep(1)

    if user_input == '1':
        name = input('Please input your full legal name: ')
        password = input('Please choose a secure password of at least 8 characters and that contains a number and 1 uppercase letter')
        #need to add loop to check password requirements are True
        new_account = BankAccount(name, password)
        accounts[new_account.account_number] = new_account
        print('Creating new account...')
        time.sleep(1)
        print('Account creation successful!')
        break
    if user_input == '2':
        pass
    if user_input == '3':
        break

    while True: #menu after successfully logging in
        print(f'{bot} Please choose an option below: ')
        time.sleep(0.5)
        print('1. Deposit | 2. Withdraw | 3. Show Balance | 4. Show Account Details | 5. Exit')

        user_input = input('You:')
        if user_input == '1':
            while True:
                try:
                    input_amount = int(input('Choose an amount to deposit: '))
                    BankAccount.deposit(input_amount)
                    break
                except ValueError:
                    print('Please insert a number only.')
        elif user_input == '2':
            while True:
                try:
                    input_amount = int(input('Choose an amount to withdraw: '))
                    BankAccount.withdraw(input_amount)
                    break
                except ValueError:
                    print('Please insert a number only.') 
        elif user_input == '3':
            print(BankAccount.show_balance())
        elif user_input == '4':
            print(BankAccount.show_details())
        elif user_input == '5':
            time.sleep(1)
            break #exists to pre-login menu
        else:
            print('Please choose one of the options provided.')
            time.sleep(1)