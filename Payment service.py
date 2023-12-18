from Project.gpay import Pay
Pay.welcome()
Pay.login()
def choose_option():
    #Menu of options in google pay
    print("Choose an option:")
    print("1. Electricity Bills")
    print("2. Mobile Recharge")
    print("3. Request Money")
    print("4. Investment")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        Pay.electricity_bills()
        choose_option()
    elif choice == 2:
        Pay.show_recharge_offers()
        choose_option()
    elif choice == 3:
        Pay.show_recharge_offers()
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
choose_option()
