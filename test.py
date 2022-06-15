from ATM_system import ATM, Bank, Card, Account

accounts = [
    Account('100000', '1021', 500000),
    Account('100007', '1021', 400000),
    Account('100008', '1021', 300000),
    Account('100009', '1022', 50000),
    Account('100010', '1022', 500000),
    Account('100011', '1022', 5000000),
    Account('100002', '1023', 0),
    Account('100003', '1024', 45000),
    Account('100004', '1025', 95000),
    Account('100005', '1026', 700000),
    Account('100006', '1027', 1000000),
]
pin_numbers = list(set([account.pin_number for account in accounts]))
bank = Bank(accounts=accounts, pin_numbers=pin_numbers)
atm = ATM(bank=bank)

if __name__ == "__main__":
    print("*********************************")
    print("*                               *")
    print("*     Welcome to ATM system     *")
    print("*                               *")
    print("*********************************")
    
    
    while atm.card is None:
        pin_number = input("-> Please insert your card. (typing your card pin number) : ")
        if atm.insert_card(card=Card(pin_number=pin_number)):
            break
        print("[Error] Please insert the right card.")
    
    print("*********************************")
    print("*                               *")
    print("*        Select account         *")
    print("*                               *")
    print("*********************************")
    atm.show_accounts()
    while True:
        select = int(input("-> Please select the account : "))
        try:
            atm.select_account(selected_account=atm.accounts[select])
            break
        except IndexError:
            print("[Error] Please choose the right account.")
            continue
    
    while True:
        print("********************************")
        print("*                              *")
        print("*      1. See Balance          *")
        print("*      2. Deposit              *")
        print("*      3. Withdraw             *")
        print("*      4. Exit                 *")
        print("*                              *")
        print("********************************")
        number = int(input("-> Please select the number : "))
        if number == 1:
            atm.see_balance()
        elif number == 2:
            amount = int(input("-> Enter the desired amount : "))
            if amount > 0:
                atm.deposit(amount=amount)
            else:
                print("[Error] Please enter the right amount.")
        elif number == 3:
            amount = int(input("-> Enter the desired amount : "))
            if amount > 0:
                atm.withdraw(amount=amount)
            else:
                print("[Error] Please enter the right amount.")
        elif number == 4:
            print("Exit.")
            break
        else:
            print("[Error] Please enter the right number.")