class ATM(object):
    def __init__(self):
        self.cardNum = input("Please enter your ATM card number: ")
        self.pinNum = input("Please enter your pin number: ")
    def withdrawl(self):
        print("For Cash Withdrawl")
    def BalanceEnquiry(self):
        print("To Balance the Enquiry")

a = ATM()
b = a.withdrawl()
print(b)
c = a.BalanceEnquiry()
print(c)