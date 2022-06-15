from typing import List

class Account():
    account_number: str
    pin_number: str
    balance: int
    
    def __init__(self, account_number: str, pin_number: str, balance: int = 0):
        self.account_number = account_number
        self.pin_number = pin_number
        self.balance = balance

class Card():
    pin_number: str
    
    def __init__(self, pin_number: str):
        self.pin_number = pin_number

class Bank():
    accounts: List[Account]
    pin_numbers: List
    
    def __init__(self, accounts: List[Account], pin_numbers: List):
        self.accounts = accounts
        self.pin_numbers = pin_numbers
    
    def check_pin_number(self, pin_number: str):
        if pin_number in self.pin_numbers:
            return True
        else:
            return False
    
    def get_accounts(self, pin_number: str):
        if pin_number in self.pin_numbers:
            return [account for account in self.accounts if account.pin_number == pin_number]
        else:
            return None
            
class ATM():
    card: Card
    accounts: List[Account]
    selected_account: Account
    bank: Bank
    
    def __init__(self, bank: Bank = None):
        self.card = None
        self.accounts = None
        self.selected_account = None
        self.bank = bank
    
    def insert_card(self, card: Card):
        if self.bank.check_pin_number(card.pin_number):
            self.card = card
            self.accounts = self.bank.get_accounts(self.card.pin_number)
            print(f"Insert Card : {self.card.pin_number}")
            return True
        else:
            print(f"[Error] Invalid Card : {card.pin_number}")
            return False
    
    def show_accounts(self):
        if self.accounts is not None:
            print("---------------------------------")
            for i in range(len(self.accounts)):
                print(f"{i}. {self.accounts[i].account_number}")
            print("---------------------------------", end="\n\n")
        else:
            print("[Error] Invalid access")
            
    
    def select_account(self, selected_account: Account):
        if self.accounts is not None and selected_account in self.accounts:
            self.selected_account = selected_account
            print(f"Select Account : {self.selected_account.account_number}")
        else:
            print(f"[Error] Invalid Account : {selected_account.account_number}")
    
    def see_balance(self):
        if self.selected_account is not None:
            print(f"Current balance : {self.selected_account.balance}")
        else:
            print("[Error] Invalid access")
    
    def deposit(self, amount: int):
        try:
            if self.selected_account is not None:
                self.selected_account.balance += amount
            print("Deposit transaction success")
            print(f"Current balance : {self.selected_account.balance}")
        except:
            print("[Error] Deposit transaction fail")

    def withdraw(self, amount: int):
        try:
            if self.selected_account is not None:
                if self.selected_account.balance - amount >= 0:
                    self.selected_account.balance -= amount
                else:
                    print("[Error] Withdrawal is not possible")
                    raise
            print("Withdraw transaction success")
            print(f"Current balance : {self.selected_account.balance}")
        except:
            print("[Error] Withdraw transaction fail")