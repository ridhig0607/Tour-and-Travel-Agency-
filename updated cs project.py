import mysql.connector as myl
from colorama import init, Fore, Back, Style
from tabulate import tabulate
from termcolor import colored
from datetime import datetime

# Initialize colorama
init(autoreset=True)

# Database connection
mydb = myl.MySQLConnection(host="localhost", user="root", password="2022", database="csproject")
mycursor = mydb.cursor()


# Create table if not exists
cr = ("""CREATE TABLE IF NOT EXISTS customer2bz (
    S_No INTEGER, 
    Name VARCHAR(50), 
    PhoneNo VARCHAR(20), 
    Fromlocation VARCHAR(100), 
    Destination VARCHAR(50), 
    Numberofdaysofstay INTEGER, 
    Numberoftravellers INTEGER, 
    Modeoftransportation VARCHAR(55), 
    Modeofpayment VARCHAR(50)

);""")
mycursor.execute(cr)

# Main program loop
ch = "y"
lst = 0
m = " "
mop = 0
print(Fore.GREEN + "WELCOME")

while ch == "y":
    print(Fore.RED + "1. REGISTER for your trip ")
    print(Fore.RED + "2. REVISIT the details to rectify")
    print(Fore.RED + "3. CANCEL your trip bookings ")
    print(Fore.WHITE + "")
    a = int(input("Specify your desired options -"))

    if a == 1:
        # Registration logic
        print(Fore.YELLOW + "")
        name = input("Enter your NAME- ")
        ph = input("Enter your10 DIGIT PHONE NUMBER- ")
        while len(ph)!= 10:
            print("Error Found!!Enter your valid 10 digit phone number")
            ph =input("Enter your 10 DIGIT PHONE NUMBER- ")
            
        initial = input("Enter your FROM LOCATION- ")
        final = input("Enter your DESTINATION- ")
        time = int(input("Enter NUMBER OF DAYS OF STAY- "))
        num = int(input("Enter NUMBER OF TRAVELLERS- "))
        print(Fore.BLACK + "")
        print(Back.GREEN + "CHOOSE YOUR CONVENIENT MODE OF PAYMENT- ")
        print(Back.BLACK + "")
        print(Fore.BLUE + "1. credit card")
        print(Fore.BLUE + "2. PAYTM")
        print(Fore.BLUE + "3. UPI")
        print(Fore.BLUE + "4. debit card")
        mop = int(input("Enter your favourable mode of payment number-"))

        if mop == 1:
            m = "creditcard"
            ccn = input("enter credit card number(16 digits)-")
            while len(ccn) != 16:
                print(Fore.WHITE + "")
                print("ERROR FOUND!!!! TYPE YOUR CREDIT CARD NUMBER AGAIN")
                ccn = input("enter your CREDIT CARD NUMBER -")
            cvv = input("enter your CVV(3 digits) -")
            while len(cvv) != 3:
                print(Fore.WHITE + "")
                print("ERROR FOUND! TYPE YOUR CVV NUMBER AGAIN")
                cvv = input("enter your CVV -")
            exp = input("enter EXPIRATION OF CREDIT CARD (YYYY-MM-DD): -")
            try:
                exp = datetime.strptime(exp, "%Y-%m-%d")
                current_date = datetime.now()
                if exp<current_date:
                    print("ERROR FOUND! type your Expiration of credit card again, the date is less than the current date.")
                    exp = input("enter EXPIRATION OF CREDIT CARD (YYYY-MM-DD):- ")
            except ValueError:
                print("Invalid date format. Please enter the date in YYYY-MM-DD format.")
            bank=input("""Chose the option for your bank name:
                        1. SBI(15% discount)
                        2.Kotak(10% discount)
                        3.Other(5% discount)\n""")
            if bank=="1":
                print(Fore.WHITE + "")
                print("You will be given 15% discount on total amount")
            if bank=="2":
                print(Fore.WHITE + "")
                print("You will be given 10% discount on total amount")
            if bank=="3":
                print(Fore.WHITE + "")
                print("You will be given 5% discount on total amount")
            

        elif mop == 2:
            m = "paytm"
            paytmno = input("enter your PAYTM NUMBER- ")
            while len(paytmno) != 10:
                print("ERROR FOUND! type your paytm number again")
                paytmno = input("enter your PAYTM NUMBER- ")
            bank=input("""Chose the option for your bank name:
                        1. SBI(15% discount)
                        2.Kotak(10% discount)
                        3.Other(5% discount)\n""")
            if bank=="1":
                print(Fore.WHITE + "")
                print("You will be given 15% discount on total amount")
            if bank=="2":
                print(Fore.WHITE + "")
                print("You will be given 10% discount on total amount")
            if bank=="3":
                print(Fore.WHITE + "")
                print("You will be given 5% discount on total amount")
            

        elif mop == 3:
            m = "UPI"
            upino = input("enter your UPI NUMBER- ")
            while len(upino) != 10:
                print(Fore.CYAN + "ERROR FOUND! enter your UPI number again")
                upino = input("enter your UPI NUMBER- ")
            bank=input("""Chose the option for your bank name:
                        1. SBI(15% discount)
                        2.Kotak(10% discount)
                        3.Other(5% discount)\n""")
            if bank=="1":
                print(Fore.WHITE + "")
                print("You will be given 15% discount on total amount")
            if bank=="2":
                print(Fore.WHITE + "")
                print("You will be given 10% discount on total amount")
            if bank=="3":
                print(Fore.WHITE + "")
                print("You will be given 5% discount on total amount")
            

        elif mop == 4:
            m = "debitcard"
            ccn = input("enter DEBIT CARD NUMBER(16 digits)- ")
            while len(ccn) != 16:
                print(Fore.CYAN + "ERROR FOUND!!!! TYPE YOUR DEBIT CARD NUMBER AGAIN")
                ccn = input("enter DEBIT CARD NUMBER- ")
            cvv = input("enter your CVV NUMBER(3 digits)- ")
            while len(cvv) != 3:
                print("ERROR FOUND! type your cvv number again")
                cvv = input("enter your CVV NUMBER- ")
            exp = input("enter EXPIRATION OF DEBIT CARD (YYYY-MM-DD): -")
            try:
                exp = datetime.strptime(exp, "%Y-%m-%d")
                current_date = datetime.now()
                if exp<current_date:
                    print("ERROR FOUND! type your Expiration of debit card again, the date is less than the current date.")
                    exp = input("enter EXPIRATION OF DEBIT CARD (YYYY-MM-DD):- ")
            except ValueError:
                print("Invalid date format. Please enter the date in YYYY-MM-DD format.")
            bank=input("""Chose the option for your bank name:
                        1. SBI(15% discount)
                        2.Kotak(10% discount)
                        3.Other(5% discount)\n""")
            if bank=="1":
                print(Fore.WHITE + "")
                print("You will be given 15% discount on total amount")
            if bank=="2":
                print(Fore.WHITE + "")
                print("You will be given 10% discount on total amount")
            if bank=="3":
                print(Fore.WHITE + "")
                print("You will be given 5% discount on total amount")
            
        print(Style.RESET_ALL)
        print(" CHOOSE MODE OF TRANSPORTATION- ")
        print("1. by air (money according to ticket)")
        print("2. by road")
        tr = int(input("Specify your choice "))
        transport = " "
        mon = 0

        if tr == 1:
            transport = "by air"
            print("Your departing dates will be notified earliest in a week ")
        elif tr == 2:
            print("1. car")
            print("2. bus")
            rt = int(input("enter your choice"))
            if rt == 1:
                transport = "car"
                print("1. Celerio (Rs 8,000 per day)")
                print("2. Innova (Rs 10,000 per day)")
                print("3. Fortuner (Rs 10,600 per day)")
                print("4. Swift Dzire (Rs 1,000)")
                print("5. XUV (Rs 13,000)")
                cars = 0
                while cars not in [1, 2, 3, 4, 5]:
                    cars = int(input("Select from them (1, 2, 3, 4, 5)"))
                if cars == 1:
                    mon = 8000
                elif cars == 2:
                    mon = 10000
                elif cars == 3:
                    mon = 10600
                elif cars == 4:
                    mon = 1000
                elif cars == 5:
                    mon = 13000
                else:
                    print("Wrong input")
            elif rt == 2:
                transport = "bus"
                print("1. Mini(Rs.15000)")
                print("2. Deluxe(Rs.20000)")
                bus = int(input("enter your choice"))
                if bus == 1:
                    mon = 15000
                    transport = "by road (mini bus)"
                elif bus == 2:
                    mon = 20000
                    transport = "by road (deluxe bus)"


        print(Fore.WHITE + "")
        print("AVAILABLE HOTELS")
        print("1: 3 star(Rs.4000)")
        print("2: 5 star(Rs.7000)")
        print("3: 7 star(Rs.10000)")
        hotm = 0
        hot = 0
        while hot not in [1, 2, 3]:
            hot = int(input("Choose among 1, 2, 3: "))
            if hot == 1:
                hotm = 4000
                break
            elif hot == 2:
                hotm = 7000
                break
            elif hot == 3:
                hotm = 10000
                break
            else:
                print("Wrong input")

        hotmt = hotm * time
        mycursor.execute("SELECT * FROM customer2bz")
        data = mycursor.fetchall()

        for i in data:
            if i[0] > lst:
                lst = i[0]

        lst += 1
        print("YOUR REFERENCE CODE IS - ", lst)
        print("*************************")
        print("*************************")
        print("TOUR AND TRAVELS")
        print(Fore.CYAN + "CUSTOMER NAME:", name)
        print(Fore.CYAN + "PHONE NUMBER:", ph)
        print(Fore.CYAN + "MODE OF PAYMENT:", m)
        print(Fore.CYAN + "NUMBER OF PEOPLE:", num)
        print(Fore.CYAN + "NUMBER OF DAYS OF STAY:", time)
        print(Fore.CYAN + "FROM:", initial, "to", final)
        print(Fore.CYAN + "HOTEL CHARGES:", hotmt)
        if mon == 0:
            print(Fore.CYAN + "TRANSPORTATION CHARGES: Will be according to tickets")
        else:
            mon=mon*time
            print(Fore.CYAN + "TRANSPORTATION CHARGES:", mon)
            
        total_sum = hotmt + mon
        if bank=="1":
            discount=total_sum*0.15
        if bank=="2":
            discount=total_sum*0.10
        if bank=="3":
            discount=total_sum*0.05
        print(Fore.WHITE + "")
        print("TOTAL MONEY (before discount):", total_sum)
        print("TOTAL MONEY (after discount):", total_sum-discount)
        print(Fore.CYAN + "REFERENCE CODE NUMBER:", lst)
        print(Back.BLACK + "")
        print(Fore.RESET + "")
        print("*************************")
        print("*************************")

        # Insert customer data into the database
        r = (lst, name, ph, initial, final, time, transport, m, num)
        add1 = """INSERT INTO customer2bz(S_No, Name, PhoneNo, Fromlocation, Destination, Numberofdaysofstay,
            Modeoftransportation, Modeofpayment, Numberoftravellers)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        mycursor.execute(add1, r)
        mydb.commit()

    elif a == 2:
        # Rectify details logic
        print(Fore.WHITE + "")
        rno1 = int(input("Enter your REFERENCE CODE- "))
        print("You can rectify the following details:")
        print("1. Name")
        print("2. Phone Number")
        print("3. Fromlocation")
        print("4. Destination")
        print("5. No of days of stay")
        print("6. Number of People")
        print("Which detail do you want to rectify?")

        doubt = input("Enter the detail to rectify: ").lower()

        if doubt == "name":
            new_name = input("Enter the new name: ")
            u1 = "UPDATE customer2bz SET Name = %s WHERE S_No = %s"
            mycursor.execute(u1, (new_name, rno1))
            print("Name updated!!!")
            mydb.commit()
        elif doubt == "phone number":
            new_phone = input("Enter the new phone number: ")
            u1 = "UPDATE customer2bz SET Phoneno = %s WHERE S_No = %s"
            mycursor.execute(u1, (new_phone, rno1))
            print("Phone number updated!!!")
            mydb.commit()
        elif doubt == "Fromlocation":
            new_location = input("Enter the new location: ")
            u1 = "UPDATE customer2bz SET Fromlocation = %s WHERE S_No = %s"
            mycursor.execute(u1, (new_location, rno1))
            print("Fromlocation updated!!!")
            mydb.commit()
        elif doubt == "destination":
            new_destination = input("Enter the new destination: ")
            u1 = "UPDATE customer2bz SET Destination = %s WHERE S_No = %s"
            mycursor.execute(u1, (new_destination, rno1))
            print("Destination updated!!!")
            mydb.commit()
        elif doubt == "No of days of stay":
            new_tenure = int(input("Enter the new no of days of stay: "))
            u1 = "UPDATE customer2bz SET Numberofdaysofstay = %s WHERE S_No = %s"
            mycursor.execute(u1, (new_tenure, rno1))
            print("Tenure updated!!!")
            mydb.commit()
        elif doubt == "Number of People":
            new_people = int(input("Enter the new number of people: "))
            u1 = "UPDATE customer2bz SET Numberoftravellers = %s WHERE S_No = %s"
            mycursor.execute(u1, (new_people, rno1))
            print("Number of people updated!!!")
            mydb.commit()
        else:
            print("Invalid input! Please ensure you typed the correct option.")

    elif a == 3:
        # Delete record logic
        print(Fore.WHITE + "")
        number = int(input("Enter your Reference Code: "))
        query = "DELETE FROM customer2bz WHERE S_No = %s"
        mycursor.execute(query, (number,))
        mydb.commit()
        print("Record deleted successfully!")

    else:
        print("Wrong input! Press 'y' to continue.")
        ch = input("DO YOU WANT TO CONTINUE? (y/n): ").lower()
