
class Atm(object):
    def __init__(self, atm_card_no, atm_pin):
        self.atmCard = atm_card_no
        self.atmPin = atm_pin

    def checkBalance(self):
        print("Your balance is $50k")

    def cashWithdrawl(self, amount):
        self.cash = 50000-amount
        print("withdrawn amount is"+str(amount) + "your balance is "+ str(self.cash))

def main():
    cardNo = input("enter your card no.")
    pin = input("enter your card pin")
    activity = int(input(" your activity no.:\n 1 check balance \n 2 withdrawl"))
    atm = Atm(cardNo, pin)
    if activity == 1:
        atm.checkBalance()
    elif activity == 2:
        amount = int(input("enter the amount to withdraw"))
        atm.cashWithdrawl(amount)
    else:
        print("thank you!!")

main()


       
    