from fpdf import FPDF
import random
class India:
    def indm():
        id=random.randint(1000000,99999999)
        sa = id
        lis1=[1,2,3,4,5,6,7,8,9,10]
        name=["Nifty 50","Sensex","SUZLON ENERGY LTD","TATA MOTORS LTD","ZOMATO LTD","ICICI BANK","RELIANCE INDS","INFOSYS LTD","INDIAN OIL CORP","HDFC BANK"]
        price=[21456.65,70514.20,38.55,732.40,123.60,1037.40,2495.60,1578.40,123.80,1656.55]
        sym='₹'
        for x in range(10):
            print(lis1[x],'.',name[x],': ',price[x],sym,end="\n")
            print("\n")
        x=int(input("Enter the list number to purchase:"))
        if x==1:
            print("\n",name[0],': ',price[0],sym,)
            y=int(input("\nEnter quantity: "))
            print("\nTotal amount :",price[0]*y,sym)
            z=int(input("1.Pay\n2.later\n"))
            if(z==1):
                print("Payment done ✅ ")
                pdf = FPDF()
                pdf.add_page()
                pdf.set_font("Arial", size=15)
                pdf.cell(200, 10, txt="Payment Receipt", ln=1, align='C')
                pdf.cell(200, 10, txt="Order Id :", ln=2, align='C')
                pdf.cell(200, 10, txt=(str(id)), ln=3, align='C')
                pdf.cell(200, 10, txt=name[0], ln=4, align='C')
                pdf.cell(200, 10, txt="TOTAL PRICE IN INR ", ln=5, align='C')
                pdf.cell(200, 10, txt=str(price[0]*y), ln=6, align='C')
                pdf.cell(200, 13, txt="congratulation!!", ln=8, align='C')
                pdf.output("Payment Receipt.pdf")
            elif(z==2):
                return India.indm()
            else:
                print("Input error")
        elif x==2:
            print("\n",name[1],': ',price[1],sym,)
            y=int(input("\nEnter quantity: "))
            print("\nTotal amount :",price[1]*y,sym)
            z=int(input("1.Pay\n2.later\n"))
            if(z==1):
                print("Payment done ✅ ")
                pdf = FPDF()
                pdf.add_page()
                pdf.set_font("Arial", size=15)
                pdf.cell(200, 10, txt="Payment Receipt", ln=1, align='C')
                pdf.cell(200, 10, txt="Order Id :", ln=2, align='C')
                pdf.cell(200, 10, txt=(str(id)), ln=3, align='C')
                pdf.cell(200, 10, txt=name[1], ln=4, align='C')
                pdf.cell(200, 10, txt="TOTAL PRICE IN INR", ln=5, align='C')
                pdf.cell(200, 10, txt=str(price[1]*y), ln=6, align='C')
                pdf.cell(200, 13, txt="congratulation!!", ln=8, align='C')
                pdf.output("Payment Receipt.pdf")
            elif(z==2):
                return India.indm()
            else:
                print("Input error")
        elif x==3:
            print("\n",name[2],': ',price[2],sym,)
            y=int(input("\nEnter quantity: "))
            print("\nTotal amount :",price[2]*y,sym)
            z=int(input("1.Pay\n2.later\n"))
            if(z==1):
                print("Payment done ✅ ")
                pdf = FPDF()
                pdf.add_page()
                pdf.set_font("Arial", size=15)
                pdf.cell(200, 10, txt="Payment Receipt", ln=1, align='C')
                pdf.cell(200, 10, txt="Order Id :", ln=2, align='C')
                pdf.cell(200, 10, txt=(str(id)), ln=3, align='C')
                pdf.cell(200, 10, txt=name[2], ln=4, align='C')
                pdf.cell(200, 10, txt="TOTAL PRICE IN INR", ln=5, align='C')
                pdf.cell(200, 10, txt=str(price[2]*y), ln=6, align='C')
                pdf.cell(200, 13, txt="congratulation!!", ln=8, align='C')
                pdf.output("Payment Receipt.pdf")
            elif(z==2):
                return India.indm()
            else:
                print("Input error")
        elif x==4:
            print("\n",name[3],': ',price[3],sym,)
            y=int(input("\nEnter quantity: "))
            print("\nTotal amount :",price[3]*y,sym)
            z=int(input("1.Pay\n2.later\n"))
            if(z==1):
                print("Payment done ✅ ")
                pdf = FPDF()
                pdf.add_page()
                pdf.set_font("Arial", size=15)
                pdf.cell(200, 10, txt="Payment Receipt", ln=1, align='C')
                pdf.cell(200, 10, txt="Order Id :", ln=2, align='C')
                pdf.cell(200, 10, txt=(str(id)), ln=3, align='C')
                pdf.cell(200, 10, txt=name[3], ln=4, align='C')
                pdf.cell(200, 10, txt="TOTAL PRICE IN INR", ln=5, align='C')
                pdf.cell(200, 10, txt=str(price[3]*y), ln=6, align='C')
                pdf.cell(200, 13, txt="congratulation!!", ln=8, align='C')
                pdf.output("Payment Receipt.pdf")
            elif(z==2):
                return India.indm()
            else:
                print("Input error")
        elif x==5:
            print("\n",name[4],': ',price[4],sym,)
            y=int(input("\nEnter quantity: "))
            print("\nTotal amount :",price[4]*y,sym)
            z=int(input("1.Pay\n2.later\n"))
            if(z==1):
                print("Payment done ✅ ")
                pdf = FPDF()
                pdf.add_page()
                pdf.set_font("Arial", size=15)
                pdf.cell(200, 10, txt="Payment Receipt", ln=1, align='C')
                pdf.cell(200, 10, txt="Order Id :", ln=2, align='C')
                pdf.cell(200, 10, txt=(str(id)), ln=3, align='C')
                pdf.cell(200, 10, txt=name[4], ln=4, align='C')
                pdf.cell(200, 10, txt="TOTAL PRICE IN INR", ln=5, align='C')
                pdf.cell(200, 10, txt=str(price[4]*y), ln=6, align='C')
                pdf.cell(200, 13, txt="congratulation!!", ln=8, align='C')
                pdf.output("Payment Receipt.pdf")
            elif(z==2):
                return India.indm()
            else:
                print("Input error")
        elif x==6:
            print("\n",name[5],': ',price[5],sym,)
            y=int(input("\nEnter quantity: "))
            print("\nTotal amount :",price[5]*y,sym)
            z=int(input("1.Pay\n2.later\n"))
            if(z==1):
                print("Payment done ✅ ")
                pdf = FPDF()
                pdf.add_page()
                pdf.set_font("Arial", size=15)
                pdf.cell(200, 10, txt="Payment Receipt", ln=1, align='C')
                pdf.cell(200, 10, txt="Order Id :", ln=2, align='C')
                pdf.cell(200, 10, txt=(str(id)), ln=3, align='C')
                pdf.cell(200, 10, txt=name[5], ln=4, align='C')
                pdf.cell(200, 10, txt="TOTAL PRICE IN INR", ln=5, align='C')
                pdf.cell(200, 10, txt=str(price[5]*y), ln=6, align='C')
                pdf.cell(200, 13, txt="congratulation!!", ln=8, align='C')
                pdf.output("Payment Receipt.pdf")
            elif(z==2):
                return India.indm
            else:
                print("Input error")
        elif x==7:
            print("\n",name[6],': ',price[6],sym,)
            y=int(input("\nEnter quantity: "))
            print("\nTotal amount :",price[6]*y,sym)
            z=int(input("1.Pay\n2.later\n"))
            if(z==1):
                print("Payment done ✅ ")
                pdf = FPDF()
                pdf.add_page()
                pdf.set_font("Arial", size=15)
                pdf.cell(200, 10, txt="Payment Receipt", ln=1, align='C')
                pdf.cell(200, 10, txt="Order Id :", ln=2, align='C')
                pdf.cell(200, 10, txt=(str(id)), ln=3, align='C')
                pdf.cell(200, 10, txt=name[6], ln=4, align='C')
                pdf.cell(200, 10, txt="TOTAL PRICE IN INR", ln=5, align='C')
                pdf.cell(200, 10, txt=str(price[6]*y), ln=6, align='C')
                pdf.cell(200, 13, txt="congratulation!!", ln=8, align='C')
                pdf.output("Payment Receipt.pdf")
            elif(z==2):
                return India.indm()
            else:
                print("Input error")
        elif x==8:
            print("\n",name[7],': ',price[7],sym,)
            y=int(input("\nEnter quantity: "))
            print("\nTotal amount :",price[7]*y,sym)
            z=int(input("1.Pay\n2.later\n"))
            if(z==1):
                print("Payment done ✅ ")
                pdf = FPDF()
                pdf.add_page()
                pdf.set_font("Arial", size=15)
                pdf.cell(200, 10, txt="Payment Receipt", ln=1, align='C')
                pdf.cell(200, 10, txt="Order Id :", ln=2, align='C')
                pdf.cell(200, 10, txt=(str(id)), ln=3, align='C')
                pdf.cell(200, 10, txt=name[7], ln=4, align='C')
                pdf.cell(200, 10, txt="TOTAL PRICE IN INR", ln=5, align='C')
                pdf.cell(200, 10, txt=str(price[7]*y), ln=6, align='C')
                pdf.cell(200, 13, txt="congratulation!!", ln=8, align='C')
                pdf.output("Payment Receipt.pdf")
            elif(z==2):
                return India.indm()
            else:
                print("Input error")
        elif x==9:
            print("\n",name[8],': ',price[8],sym,)
            y=int(input("\nEnter quantity: "))
            print("\nTotal amount :",price[8]*y,sym)
            z=int(input("1.Pay\n2.later\n"))
            if(z==1):
                print("Payment done ✅ ")
                pdf = FPDF()
                pdf.add_page()
                pdf.set_font("Arial", size=15)
                pdf.cell(200, 10, txt="Payment Receipt", ln=1, align='C')
                pdf.cell(200, 10, txt="Order Id :", ln=2, align='C')
                pdf.cell(200, 10, txt=(str(id)), ln=3, align='C')
                pdf.cell(200, 10, txt=name[8], ln=4, align='C')
                pdf.cell(200, 10, txt="TOTAL PRICE IN INR", ln=5, align='C')
                pdf.cell(200, 10, txt=str(price[8]*y), ln=6, align='C')
                pdf.cell(200, 13, txt="congratulation!!", ln=8, align='C')
                pdf.output("Payment Receipt.pdf")
            elif(z==2):
                return India.indm()
            else:
                print("Input error")
        elif x==10:
            print("\n",name[9],': ',price[9],sym,)
            y=int(input("\nEnter quantity: "))
            print("\nTotal amount :",price[9]*y,sym)
            z=int(input("1.Pay\n2.later\n"))
            if(z==1):
                print("Payment done ✅ ")
                pdf = FPDF()
                pdf.add_page()
                pdf.set_font("Arial", size=15)
                pdf.cell(200, 10, txt="Payment Receipt", ln=1, align='C')
                pdf.cell(200, 10, txt="Order Id :", ln=2, align='C')
                pdf.cell(200, 10, txt=(str(id)), ln=3, align='C')
                pdf.cell(200, 10, txt=name[9], ln=4, align='C')
                pdf.cell(200, 10, txt="TOTAL PRICE IN INR", ln=5, align='C')
                pdf.cell(200, 10, txt=str(price[9]*y), ln=6, align='C')
                pdf.cell(200, 13, txt="congratulation!!", ln=8, align='C')
                pdf.output("Payment Receipt.pdf")
            elif(z==2):
                return India.indm()
            else:
                print("Input error")
        else :
            print("Input error!!")


class Crypto:
    def forex():
        id = random.randint(1000000, 99999999)
        lis1=[1,2,3,4,5,6,7,8,9,10]
        name=["Bitcoin","Ethereum","Tether","BNB","Solana","Cosmos","The Graph","Binance","Quant","NEO"]
        price=[42770.09,2273.32,1.00001247,249.89905,79.0806,11.32725,0.168,0.99,112.51,13.43]
        sym='$'
        for x in range(10):
            print(lis1[x],'.',name[x],': ',sym,price[x],end="\n\n")
        x=int(input("Enter the list number to purchase:"))
        if x==1:
            print("\n",name[0],': ',price[0],sym,)
            y=int(input("\nEnter quantity: "))
            print("\nTotal amount :",price[0]*y,sym)
            z=int(input("1.Pay\n2.later\n"))
            if(z==1):
                print("Payment done ✅ ")
                pdf = FPDF()
                pdf.add_page()
                pdf.set_font("Arial", size=15)
                pdf.cell(200, 10, txt="Payment Receipt", ln=1, align='C')
                pdf.cell(200, 10, txt="Order Id :", ln=2, align='C')
                pdf.cell(200, 10, txt=(str(id)), ln=3, align='C')
                pdf.cell(200, 10, txt=name[0], ln=4, align='C')
                pdf.cell(200, 10, txt="TOTAL PRICE IN USD", ln=5, align='C')
                pdf.cell(200, 10, txt=str(price[0] * y), ln=6, align='C')
                pdf.cell(200, 13, txt="congratulation!!", ln=8, align='C')
                pdf.output("Payment Receipt.pdf")
            elif(z==2):
                return Crypto.forex()
            else:
                print("Input error")
        elif x==2:
            print("\n",name[1],': ',price[1],sym,)
            y=int(input("\nEnter quantity: "))
            print("\nTotal amount :",price[1]*y,sym)
            z=int(input("1.Pay\n2.later\n"))
            if(z==1):
                print("Payment done ✅ ")
                pdf = FPDF()
                pdf.add_page()
                pdf.set_font("Arial", size=15)
                pdf.cell(200, 10, txt="Payment Receipt", ln=1, align='C')
                pdf.cell(200, 10, txt="Order Id :", ln=2, align='C')
                pdf.cell(200, 10, txt=(str(id)), ln=3, align='C')
                pdf.cell(200, 10, txt=name[1], ln=4, align='C')
                pdf.cell(200, 10, txt="TOTAL PRICE IN USD", ln=5, align='C')
                pdf.cell(200, 10, txt=str(price[1] * y), ln=6, align='C')
                pdf.cell(200, 13, txt="congratulation!!", ln=8, align='C')
                pdf.output("Payment Receipt.pdf")
            elif(z==2):
                return Crypto.forex()
            else:
                print("Input error")
        elif x==3:
            print("\n",name[2],': ',price[2],sym,)
            y=int(input("\nEnter quantity: "))
            print("\nTotal amount :",price[2]*y,sym)
            z=int(input("1.Pay\n2.later\n"))
            if(z==1):
                print("Payment done ✅ ")
                pdf = FPDF()
                pdf.add_page()
                pdf.set_font("Arial", size=15)
                pdf.cell(200, 10, txt="Payment Receipt", ln=1, align='C')
                pdf.cell(200, 10, txt="Order Id :", ln=2, align='C')
                pdf.cell(200, 10, txt=(str(id)), ln=3, align='C')
                pdf.cell(200, 10, txt=name[2], ln=4, align='C')
                pdf.cell(200, 10, txt="TOTAL PRICE IN USD", ln=5, align='C')
                pdf.cell(200, 10, txt=str(price[2] * y), ln=6, align='C')
                pdf.cell(200, 13, txt="congratulation!!", ln=8, align='C')
                pdf.output("Payment Receipt.pdf")
            elif(z==2):
                return Crypto.forex()
            else:
                print("Input error")
        elif x==4:
            print("\n",name[3],': ',price[3],sym,)
            y=int(input("\nEnter quantity: "))
            print("\nTotal amount :",price[3]*y,sym)
            z=int(input("1.Pay\n2.later\n"))
            if(z==1):
                print("Payment done ✅ ")
                pdf = FPDF()
                pdf.add_page()
                pdf.set_font("Arial", size=15)
                pdf.cell(200, 10, txt="Payment Receipt", ln=1, align='C')
                pdf.cell(200, 10, txt="Order Id :", ln=2, align='C')
                pdf.cell(200, 10, txt=(str(id)), ln=3, align='C')
                pdf.cell(200, 10, txt=name[3], ln=4, align='C')
                pdf.cell(200, 10, txt="TOTAL PRICE IN USD", ln=5, align='C')
                pdf.cell(200, 10, txt=str(price[3] * y), ln=6, align='C')
                pdf.cell(200, 13, txt="congratulation!!", ln=8, align='C')
                pdf.output("Payment Receipt.pdf")
            elif(z==2):
                return Crypto.forex()
            else:
                print("Input error")
        elif x==5:
            print("\n",name[4],': ',price[4],sym,)
            y=int(input("\nEnter quantity: "))
            print("\nTotal amount :",price[4]*y,sym)
            z=int(input("1.Pay\n2.later\n"))
            if(z==1):
                print("Payment done ✅ ")
                pdf = FPDF()
                pdf.add_page()
                pdf.set_font("Arial", size=15)
                pdf.cell(200, 10, txt="Payment Receipt", ln=1, align='C')
                pdf.cell(200, 10, txt="Order Id :", ln=2, align='C')
                pdf.cell(200, 10, txt=(str(id)), ln=3, align='C')
                pdf.cell(200, 10, txt=name[4], ln=4, align='C')
                pdf.cell(200, 10, txt="TOTAL PRICE IN USD", ln=5, align='C')
                pdf.cell(200, 10, txt=str(price[4] * y), ln=6, align='C')
                pdf.cell(200, 13, txt="congratulation!!", ln=8, align='C')
                pdf.output("Payment Receipt.pdf")
            elif(z==2):
                return Crypto.forex()
            else:
                print("Input error")
        elif x==6:
            print("\n",name[5],': ',price[5],sym,)
            y=int(input("\nEnter quantity: "))
            print("\nTotal amount :",price[5]*y,sym)
            z=int(input("1.Pay\n2.later\n"))
            if(z==1):
                print("Payment done ✅ ")
                pdf = FPDF()
                pdf.add_page()
                pdf.set_font("Arial", size=15)
                pdf.cell(200, 10, txt="Payment Receipt", ln=1, align='C')
                pdf.cell(200, 10, txt="Order Id :", ln=2, align='C')
                pdf.cell(200, 10, txt=(str(id)), ln=3, align='C')
                pdf.cell(200, 10, txt=name[5], ln=4, align='C')
                pdf.cell(200, 10, txt="TOTAL PRICE IN USD", ln=5, align='C')
                pdf.cell(200, 10, txt=str(price[5] * y), ln=6, align='C')
                pdf.cell(200, 13, txt="congratulation!!", ln=8, align='C')
                pdf.output("Payment Receipt.pdf")
            elif(z==2):
                return Crypto.forex()
            else:
                print("Input error")
        elif x==7:
            print("\n",name[6],': ',price[6],sym,)
            y=int(input("\nEnter quantity: "))
            print("\nTotal amount :",price[6]*y,sym)
            z=int(input("1.Pay\n2.later\n"))
            if(z==1):
                print("Payment done ✅ ")
                pdf = FPDF()
                pdf.add_page()
                pdf.set_font("Arial", size=15)
                pdf.cell(200, 10, txt="Payment Receipt", ln=1, align='C')
                pdf.cell(200, 10, txt="Order Id :", ln=2, align='C')
                pdf.cell(200, 10, txt=(str(id)), ln=3, align='C')
                pdf.cell(200, 10, txt=name[6], ln=4, align='C')
                pdf.cell(200, 10, txt="TOTAL PRICE IN USD", ln=5, align='C')
                pdf.cell(200, 10, txt=str(price[6] * y), ln=6, align='C')
                pdf.cell(200, 13, txt="congratulation!!", ln=8, align='C')
                pdf.output("Payment Receipt.pdf")
            elif(z==2):
                return Crypto.forex()
            else:
                print("Input error")
        elif x==8:
            print("\n",name[7],': ',price[7],sym,)
            y=int(input("\nEnter quantity: "))
            print("\nTotal amount :",price[7]*y,sym)
            z=int(input("1.Pay\n2.later\n"))
            if(z==1):
                print("Payment done ✅ ")
                pdf = FPDF()
                pdf.add_page()
                pdf.set_font("Arial", size=15)
                pdf.cell(200, 10, txt="Payment Receipt", ln=1, align='C')
                pdf.cell(200, 10, txt="Order Id :", ln=2, align='C')
                pdf.cell(200, 10, txt=(str(id)), ln=3, align='C')
                pdf.cell(200, 10, txt=name[7], ln=4, align='C')
                pdf.cell(200, 10, txt="TOTAL PRICE IN USD", ln=5, align='C')
                pdf.cell(200, 10, txt=str(price[7] * y), ln=6, align='C')
                pdf.cell(200, 13, txt="congratulation!!", ln=8, align='C')
                pdf.output("Payment Receipt.pdf")
            elif(z==2):
                return Crypto.forex()
            else:
                print("Input error")
        elif x==9:
            print("\n",name[8],': ',price[8],sym,)
            y=int(input("\nEnter quantity: "))
            print("\nTotal amount :",price[8]*y,sym)
            z=int(input("1.Pay\n2.later\n"))
            if(z==1):
                print("Payment done ✅ ")
                pdf = FPDF()
                pdf.add_page()
                pdf.set_font("Arial", size=15)
                pdf.cell(200, 10, txt="Payment Receipt", ln=1, align='C')
                pdf.cell(200, 10, txt="Order Id :", ln=2, align='C')
                pdf.cell(200, 10, txt=(str(id)), ln=3, align='C')
                pdf.cell(200, 10, txt=name[8], ln=4, align='C')
                pdf.cell(200, 10, txt="TOTAL PRICE IN USD", ln=5, align='C')
                pdf.cell(200, 10, txt=str(price[8] * y), ln=6, align='C')
                pdf.cell(200, 13, txt="congratulation!!", ln=8, align='C')
                pdf.output("Payment Receipt.pdf")
            elif(z==2):
                return Crypto.forex()
            else:
                print("Input error")
        elif x==10:
            print("\n",name[9],': ',price[9],sym,)
            y=int(input("\nEnter quantity: "))
            print("\nTotal amount :",price[9]*y,sym)
            z=int(input("1.Pay\n2.later\n"))
            if(z==1):
                print("Payment done ✅ ")
                pdf = FPDF()
                pdf.add_page()
                pdf.set_font("Arial", size=15)
                pdf.cell(200, 10, txt="Payment Receipt", ln=1, align='C')
                pdf.cell(200, 10, txt="Order Id :", ln=2, align='C')
                pdf.cell(200, 10, txt=(str(id)), ln=3, align='C')
                pdf.cell(200, 10, txt=name[9], ln=4, align='C')
                pdf.cell(200, 10, txt="TOTAL PRICE IN USD", ln=5, align='C')
                pdf.cell(200, 10, txt=str(price[9] * y), ln=6, align='C')
                pdf.cell(200, 13, txt="congratulation!!", ln=8, align='C')
                pdf.output("Payment Receipt.pdf")
            elif(z==2):
                return Crypto.forex()
            else:
                print("Input error")
        else :
            print("Input error!!")
        
