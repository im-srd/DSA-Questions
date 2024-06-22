class ATM:
    def __init__(self):
        self.d20 = 0
        self.d50 = 0
        self.d100 = 0
        self.d200 = 0
        self.d500 = 0

    def deposit(self, d):
        if len(d) != 5:
            raise ValueError("Please provide exactly 5 denomination values")
        
        self.d20 = d[0]
        self.d50 = d[1]
        self.d100 = d[2]
        self.d200 = d[3]
        self.d500 = d[4]

        print('20 :', d[0])
        print('50 :', d[1])
        print('100 :', d[2])
        print('200 :', d[3])
        print('500 :', d[4])

    def withdraw(self, amount):
        sol = [0, 0, 0, 0, 0]
        remaining_amount = amount

        if remaining_amount > 0:
            while remaining_amount >= 500 and self.d500 > 0:
                remaining_amount -= 500
                sol[4] += 1
                self.d500 -= 1
            while remaining_amount >= 200 and self.d200 > 0:
                remaining_amount -= 200
                sol[3] += 1
                self.d200 -= 1
            while remaining_amount >= 100 and self.d100 > 0:
                remaining_amount -= 100
                sol[2] += 1
                self.d100 -= 1
            while remaining_amount >= 50 and self.d50 > 0:
                remaining_amount -= 50
                sol[1] += 1
                self.d50 -= 1
            while remaining_amount >= 20 and self.d20 > 0:
                remaining_amount -= 20
                sol[0] += 1
                self.d20 -= 1

        if remaining_amount == 0:
            return sol
        else:
            # Revert the changes if the withdrawal is not possible
            self.d20 += sol[0]
            self.d50 += sol[1]
            self.d100 += sol[2]
            self.d200 += sol[3]
            self.d500 += sol[4]
            return [-1]

atm = ATM()
atm.deposit([0, 2, 0, 10, 1])
print(atm.withdraw(600))  
print(atm.withdraw(530))  