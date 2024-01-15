#create a python program of Google_Pay program using claas, object, inheritance, array,loops ,strings, lists, dictionaries, datatypes , modules and package create such that the google pay in the beggining it should wlcome you then ask for login next ask user to enter 1.name, 2, number ,3. otp. later ask user what you want to proceed with 1. electricity bills , 2. Mobile recharge, 3. Recharge with number, 4.Request money if choosen electricity display the list as 1. adani electricity 2. tata power 3. torrent power 4. vaghani energy .if selected any of these proceed to ask user to enter 10 dighit number and procced with the payment method, 2.monile recharge in this ask the user which sim you own 1, jio 2.airtel 3. Vi . if choosen 1 show three offer of 28days and 400rupees, secong 3months 790rupees third 1yr 3200rupees same for jio and airtel offers apply same offers 3. pay with phone number in this let the user enter the phone number  after entering the number let it display msg payment done 4. option for request money in this let user enter the number from the person he wants the money from then later display the default msg as user has accepted the request and ask user if he wants the money to be credited in his account in y/n if y display as 10,000 rupees credited if n exit 
from fpdf import FPDF
import random
class Pay():
    def _init_():
        #user data 
        user_data = {}
        bills = {
            1: "Adani Electricity",
            2: "Tata Power",
            3: "Torrent Power",
            4: "Vaghani Energy"
        }

    def welcome():
        Blue = '\033[34m'
        #Welcome message
        print(f'{Blue} !! Welcome Welcome !!')

    def login():
        #User Information
        name = str(input("Enter your name: "))
        number = int(input("Enter your mobile number: "))
        

    def choose_option():
        #Menu of options in google pay
        print()
        print("1. Electricity Bills")
        print("2. Mobile Recharge")
        print("3. Request Money")
        choice = int(input("Enter your choice: "))

        #User Choice
        if choice == 1:
            Pay.electricity_bills()
        elif choice == 2:
            Pay.show_recharge_offers()
        elif choice == 3:
            Pay.show_recharge_offers()

    def electricity_bills():
        id = random.randint(1000000, 99999999)
        #paying bills
        print("Choose an electricity provider:")
        bills = [ "1. Adani Electricity", "2. Tata Power", "3. Torrent Power", "4. Vaghani Energy"]
        for x in range(4):
            print(bills[x])
        # preferred electricity provider
        bill_choice = int(input("Enter your choice: "))
        if bill_choice == 1:
            account_number = input("Enter 10-digit account number: ")
            
            # pending amount
            pending_amount = 4532
            print(f"Pending amount: {pending_amount} INR")

            #User amount
            paid_amount = float(input("Enter the amount you want to pay: "))

            # User ammount is sufficient or not
            if paid_amount >= pending_amount:
                #successful payment
                pending_amount -= paid_amount
                print(f"Bill Paid successfully! Remaining amount: {pending_amount} INR")
                pdf = FPDF()
                pdf.add_page()
                pdf.set_font("Arial", size=15)
                pdf.cell(200, 10, txt="Bill Receipt", ln=1, align='C')
                pdf.cell(200, 10, txt="Order Id :", ln=2, align='C')
                pdf.cell(200, 10, txt=(str(id)), ln=3, align='C')
                pdf.cell(200, 10, txt="Account Number :", ln=4, align='C')
                pdf.cell(200, 10, txt=(str(account_number)), ln=5, align='C')
                pdf.cell(200, 10, txt="Bill Amount you paid in INR", ln=6, align='C')
                pdf.cell(200, 10, txt=str(paid_amount), ln=7, align='C')
                pdf.cell(200, 13, txt="congratulation!!", ln=9, align='C')
                pdf.output("Adanielectrycitybill.pdf")

            else:
                #insufficient payment
                print("Payment amount is less than the pending amount. Payment failed.")
        elif bill_choice == 2:
            account_number = input("Enter 10-digit account number: ")
            
            # pending amount
            pending_amount = 999
            print(f"Pending amount: {pending_amount} INR")

            #User amount
            paid_amount = float(input("Enter the amount you want to pay: "))

            # User ammount is sufficient or not
            if paid_amount >= pending_amount:
                #successful payment
                pending_amount -= paid_amount
                print(f"Bill Paid successfully! Remaining amount: {pending_amount} INR")
                pdf = FPDF()
                pdf.add_page()
                pdf.set_font("Arial", size=15)
                pdf.cell(200, 10, txt="Bill Receipt", ln=1, align='C')
                pdf.cell(200, 10, txt="Order Id :", ln=2, align='C')
                pdf.cell(200, 10, txt=(str(id)), ln=3, align='C')
                pdf.cell(200, 10, txt="Account Number :", ln=4, align='C')
                pdf.cell(200, 10, txt=(str(account_number)), ln=5, align='C')
                pdf.cell(200, 10, txt="Bill Amount you paid in INR", ln=6, align='C')
                pdf.cell(200, 10, txt=str(paid_amount), ln=7, align='C')
                pdf.cell(200, 13, txt="congratulation!!", ln=9, align='C')
                pdf.output("Tatapowerbill.pdf")
            else:
                #insufficient payment
                print("Payment amount is less than the pending amount. Payment failed.")
        elif bill_choice == 3:
            account_number = input("Enter 10-digit account number: ")
            
            # pending amount
            pending_amount = 1450
            print(f"Pending amount: {pending_amount} INR")

            #User amount
            paid_amount = float(input("Enter the amount you want to pay: "))

            # User ammount is sufficient or not
            if paid_amount >= pending_amount:
                #successful payment
                pending_amount -= paid_amount
                print(f"Bill Paid successfully! Remaining amount: {pending_amount} INR")
                pdf = FPDF()
                pdf.add_page()
                pdf.set_font("Arial", size=15)
                pdf.cell(200, 10, txt="Bill Receipt", ln=1, align='C')
                pdf.cell(200, 10, txt="Order Id :", ln=2, align='C')
                pdf.cell(200, 10, txt=(str(id)), ln=3, align='C')
                pdf.cell(200, 10, txt="Account Number :", ln=4, align='C')
                pdf.cell(200, 10, txt=(str(account_number)), ln=5, align='C')
                pdf.cell(200, 10, txt="Bill Amount you paid in INR", ln=6, align='C')
                pdf.cell(200, 10, txt=str(paid_amount), ln=7, align='C')
                pdf.cell(200, 13, txt="congratulation!!", ln=9, align='C')
                pdf.output("Torrentpowerbill.pdf")
            else:
                #insufficient payment
                print("Payment amount is less than the pending amount. Payment failed.")
        elif bill_choice == 4:
            account_number = input("Enter 10-digit account number: ")
            
            # pending amount
            pending_amount = 2999
            print(f"Pending amount: {pending_amount} INR")

            #User amount
            paid_amount = float(input("Enter the amount you want to pay: "))

            # User ammount is sufficient or not
            if paid_amount >= pending_amount:
                #successful payment
                pending_amount -= paid_amount
                print(f"Bill Paid successfully! Remaining amount: {pending_amount} INR")
                pdf = FPDF()
                pdf.add_page()
                pdf.set_font("Arial", size=15)
                pdf.cell(200, 10, txt="Bill Receipt", ln=1, align='C')
                pdf.cell(200, 10, txt="Order Id :", ln=2, align='C')
                pdf.cell(200, 10, txt=(str(id)), ln=3, align='C')
                pdf.cell(200, 10, txt="Account Number :", ln=4, align='C')
                pdf.cell(200, 10, txt=(str(account_number)), ln=5, align='C')
                pdf.cell(200, 10, txt="Bill Amount you paid in INR", ln=6, align='C')
                pdf.cell(200, 10, txt=str(paid_amount), ln=7, align='C')
                pdf.cell(200, 13, txt="congratulation!!", ln=9, align='C')
                pdf.output("VaghaniEnergybill.pdf")
            else:
                #insufficient payment
                print("Payment amount is less than the pending amount. Payment failed.")
        else:
            #invalid choice
            print("Invalid choice.")

  
    def show_recharge_offers():
        tra = random.randint(10000000,999999999)
        num = int(input("Enter 10-digit only mobile number"))
        print("\nChoose your mobile operator:\n")
        print("1. vi")
        print("2. jio")
        print("3. airtel")
        vi=["1. 28 days - 299₹ ","2. 3 months - 699₹ ","3. 1 year - 3200₹"]
        jio=["1. 28 days - 239₹ ","2. 3 months - 533₹ ","3. 1 year - 2999₹"]
        airtel=["1. 28 days - 299₹ ","2. 3 months - 750₹ ","3. 1 year - 2999₹"]
        recharge_choice = int(input("Enter your choice: "))
        print("\nRecharge Offers:")
        if recharge_choice==1:
            for i in range(3):
                print(vi[i])
        elif recharge_choice==2:
            for i in range(3):
                print(jio[i])
        elif recharge_choice==3:
            for i in range(3):
                print(airtel[i])
        else:
            print("input error!!")
        s=int(input("\nenter the plan number to pay :"))
        if s == 1 and recharge_choice == 1:
            print("\npayment successful...")
            print("""Get Unlimited Calls + 1.5 GB/Day Data + 100 SMS/Day + Enjoy Night data without limits from 12am to 6am + Weekend Data Rollover + Vi Movies & TV Classic access.""")
        elif s == 1 and recharge_choice == 2:
            print("\npayment successful...")
            print("""Get 3 GB/Day + Unlimited Calls + 100 SMS/Day valid for 56 Days. Enjoy unlimited Night data from 12am to 6am! Carry Mon-Fri unused data into Sat-Sun. 2GB of backup Data every month at no extra Cost! Vi Movies & TV access!Post daily quota, data speed will be upto 64Kbps. Post daily SMS quota charges applicable at Rs 1/1.5 for Local/STD SMS. 5GB Extra Data only valid for 3 days. """)
        elif s ==1 and recharge_choice == 3:
            print("\npayment successful...")
            print("""1 Yr Prime Video Mobile edition + Get Unlimited Calls + 2GB/Day Data for 365 Days. Enjoy unlimited Night data from 12am to 6am! Carry Mon-Fri unused data into Sat-Sun. 2GB of backup Data every month at no extra Cost! Vi Movies & TV access!Post daily quota, data speed will be upto 64Kbps. Post daily SMS quota charges applicable at Rs 1/1.5 for Local/STD SMS""")
        elif s == 2 and recharge_choice == 1:
            print("\npayment successful...")
            print("""Get Free Unlimited Voice Calls + 1.5 GB/day Data + 100 SMS/Day + Complimentary subscription to Jio Apps - JioTV, JioCinema (Premium Subscription not included), JioCloud.(Save Rs.51 on recharge of Plan 666 (239 plan of 28 days x 3 times=Rs.717) + Unlimited True 5G Data for eligible subscribers. """)
        elif s == 2 and recharge_choice == 2:
            print("\npayment successful...")
            print("""	Get Free Unlimited Voice Calls + 2 GB/Day Data + 100 SMS/Day + Complimentary subscription to Jio Apps - JioTV, JioCinema (Premium Subscription not included), JioCloud + Unlimited True 5G Data for eligible subscribers.""")
        elif s == 2 and recharge_choice == 3:
            print("\npayment successful...")
            print("""Get Free Unlimited Voice Calls + 2.5 GB/day Data + 100 SMS/Day + Complimentary subscription to Jio Apps - JioTV, JioCinema (Premium Subscription not included), JioCloud, (Special Offer : 24 days extra validity) + Unlimited True 5G Data for eligible subscribers + Special Offer : 389 days (365 + 24 days extra)""")
        elif s == 3 and recharge_choice == 1:
            print("\npayment successful...")
            print(""" unlimited voice calls (local, STD, roaming) and 100 SMS per day, with a validity of 28 days and  2GB per day with 14 gb extra !!!""")
        elif s == 3 and recharge_choice == 2:
            print("\npayment successful...")
            print("""1.5GB daily data benefit. Additionally, it also offers benefits that are offered with the Rs. 519 plan, except that this plan comes with a validity of 90 days. Some of the benefits include 100 SMS per day""")
        elif s == 3 and recharge_choice == 3:
            print("\npayment successful...")
            print("""Unlimited Prepaid eSIM Plan that comes with benefits like Calling - Unlimited, Data - 2 GB/day, SMS - 100/day with a Validity of 365 days.""")
        else :
            print("invalid input!!")
    def request_money():
        requested_number = str(input("\n Enter the number/upi id you want to request money :"))
        requested_amount = int(input("\n Enter the amount :"))
        print("Your request is send......")
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=15)
        pdf.cell(200, 10, txt="Request Receipt", ln=1, align='C')
        pdf.cell(200, 10, txt="Request Id :", ln=2, align='C')
        pdf.cell(200, 10, txt=(str(id)), ln=3, align='C')
        pdf.cell(200, 10, txt="Number/UPI :", ln=4, align='C')
        pdf.cell(200, 10, txt=(str(requested_number)), ln=5, align='C')
        pdf.cell(200, 10, txt="Amount in INR", ln=6, align='C')
        pdf.cell(200, 10, txt=str(requested_amount), ln=7, align='C')
        pdf.cell(200, 13, txt="request send....", ln=9, align='C')
        pdf.output("request.pdf")
        
        
