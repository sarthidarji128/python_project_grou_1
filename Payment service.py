from Project.gpay import Pay
import time
import random
Pay.welcome()
Pay.login()
def otp():
    otp = random.randint(1000,9999)
    print("OTP :",otp)
    
otp()
def choose_option():
    #Menu of options in google pay
    print()
    print("1. Electricity Bills")
    print()
    print("2. Mobile Recharge")
    print()
    print("3. Request Money")
    print()
    print("4. Investment")
    print()
    choice = int(input(" "))
    if choice == 1:
        Pay.electricity_bills()
        choose_option()
    elif choice == 2:
        Pay.show_recharge_offers()
        choose_option()
    elif choice == 3:
        Pay.request_money()
        choose_option()
    elif choice == 4:
        y=int(input("1.Indian Market\n2.Crypto Currency"))
        if y==1:
            from Project.binance import India
            India.indm()
            choose_option()
        elif y==2:
            from Project.binance import Crypto
            Crypto.forex()
            choose_option()
        else:
            print("Invalid Choice")
    else :
        print("Invalid Option")
while True:
    time.sleep(1)
    choose_option()
