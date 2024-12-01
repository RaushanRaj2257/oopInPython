class Atm:

    def __init__(self):
        self.balance=0
        self.pin=""
        self.menu()
    
    def menu(self):
        user_input=input("""
                    Hello, How would you like to proceed
                    1.Enter 1 for Create pin
                    2.Enter 2 for deposit
                    3.Enter 3 for withdraw
                    4.Enter 4 for Check Balance
                    5.Enter 5 for Exit
                    
                
 """)
        
        if user_input=="1":
            self.set_pin()
            self.menu()
        elif user_input=="2":
            self.deposit()
            self.menu()
        elif user_input=="3":
            self.withdraw()
            self.menu()
        elif user_input=="4":
            self.check_balance()
            self.menu()
        elif user_input=="5":
            self.exit_atm()

    def set_pin(self):
        self.pin=input("Enter your pin")
        print("pin set successfully")
    def deposit(self):
        temp=input("Enter your pin:")
        if temp==self.pin:
            amount=int(input("Enter your amount:"))
            self.balance+=amount
            print("deposit Successfully")
        else:
            print("Your pin wrong so please try again")
            self.deposit()

    def withdraw(self):
        temp=input("Enter your pin:")
        if self.pin==temp:
            amount=int(input("Enter withdrawal amount:"))
            self.balance-=amount
            print("Withdrawal successfully done")
        else:
            print("You Enter Wrong pin so please try again")
            self.withdraw()
    def check_balance(self):
        temp=input("Enter your pin:")
        if temp==self.pin:
            print("your balance=",self.balance)
        else:
            print("Your pin is wrong so please try again")
            self.check_balance()
    def exit_atm(self):
        print(("Thank you for using this application"))
        exit(0)


        

sbi=Atm()