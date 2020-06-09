class BankDetails:
    def __init__(self, fname, lname, age, starting_bal):
        self.first = fname
        self.last = lname
        self.age = age
        self.starting_balance = starting_bal

    def cashDeposit(self, deposit):
        if(type(deposit)==str):
            print("Error: Your deposit entry is not a number. Please input a number")
        else:
            balance = self.starting_balance + deposit
            self.starting_balance = balance
            print("{}".format(balance))

    def cashWithdrawal(self, withdraw):

        balance = self.starting_balance - withdraw
        if(balance < 0):
            balance = self.starting_balance + withdraw
            print("Error: Withdrawal cannot exceed account balance")

        else:
            print("{}".format(balance))


andy = BankDetails('Andy', 'Roberts', 35, 30000)
andy.cashDeposit(12000)
andy.cashWithdrawal(5000)