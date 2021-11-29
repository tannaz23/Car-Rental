
import fileinput
from datetime import datetime

#--ORDER FUNCTION ----------------------------------------------------------------------
def get_passportid():
    while 1 :
        passportid = input("Enter your passport number ---")
        if len(passportid)==9 and passportid[0:7].isnumeric() and passportid[7:8]=='-' and passportid[8:9].isalpha():
            return passportid
            break
        else:
            print("Passport number is incorrect, try again!") 
def searchcustomer():
    while 1:
        passportid=input('Enter your Passport id : ')
        if len(passportid)==9 and passportid[0:7].isnumeric() and passportid[7:8]=='-' and passportid[8:9].isalpha():
            file3 = open("customers.txt", "r")
            flag = 0
            index = 0
            for line in file3:  
                index += 1
                if passportid in line:
                    flag = 1
                    
                    break
            if flag == 0: 
                print('The customer with that passport_id :', passportid , 'does not exist.')
                ch4=input("do you want to try again ?")
                if ch4=="y" or ch4=='Y':
                    None
                else :
                    customers1()
                    break
            else:
                print('Customer found!')
                file=open('customers.txt')
                lines=file.readlines()
                print(lines[(index-1)])
                file.close()
                break  
def pickup_date():
    while 1 :
        pickup_date = input("Pick up date (DD/MM/YYYY)")
        format = "%d/%m/%Y"
        res = True    
        try:
            res = bool(datetime.strptime(pickup_date, format))
        except ValueError:
            res = False
        if str(res)=='True':
            return pickup_date
            break
        else:
            print("Incorrect date format, try again!")  
def return_date():
    while 1 :
        return_date = input("Return date (DD/MM/YYYY)")
        format = "%d/%m/%Y"
        res = True    
        try:
            res = bool(datetime.strptime(return_date, format))
        except ValueError:
            res = False
        if str(res)=='True':
            return return_date
            break
        else:
            print("Incorrect date format, try again!")        
def price_table():
    print("--------------------------------------")
    print("Car type ","|----------|", "Price     ")
    print("--------------------------------------")
    print("SUV      ","|----------|", "15 000 EUR")
    print("Hatchback","|----------|", " 7 000 EUR")
    print("Sedan    ","|----------|", "12 000 EUR")
    print("Coupe    ","|----------|", "10 000 EUR")
    print("-------")
    print("Please note the daily rate is based on 100 driven kilometers per day on average over the rental period. The fee for driving more than 100 km is based on 1% of the daily fare for each kilometer over 100km.")
def check_unavailable():
    try:
        file_read = open('cars.txt', "r")
        text = '(1)'
        lines = file_read.readlines()
        new_list = []
        idx = 0
        for line in lines: 
            if text in line:
                new_list.insert(idx, line)
                idx += 1
        file_read.close()
        if len(new_list)==0:
            #print("\n\**** car is available ! ****")
            None
        else:
            lineLen = len(new_list)
            print("\n**** car is unavailable  ****\n")
            for i in range(lineLen):
                print(end=new_list[i])
            #print()    
    except :
        print("\nThe file doesn't exist!")
def order_id():
    file = open("orders.txt","r")
    Counter = 0   
    Content = file.read()
    CoList = Content.split("\n")
    for i in CoList:
        if i:
            Counter += 1
    Counter = Counter + 1
    return Counter  
def car_type_choose():
    while 1 :
        print("-----Car types-----")
        print("Hatchback (1)")
        print("Sedan (2)")
        print("Coupe (3)")
        print("SUV (4)")
        ch21=input("What option do you want ?--")
        if ch21=='1' or ch21=='h' or ch21=='H':
            car_type = "Hatchback"
            a = check_unavailable()
            if a == True:
                ch22=input("Car of type ",car_type," is unavailable, Do you want to pick another type (y/n)")
                if ch22=="y" or ch22=="Y":
                    None
                else :
                    orders()
                    break
            else :
                print("Order registered !")
                return car_type
                break 
        elif ch21=='2' or ch21=='s' or ch21=='S':
            car_type = "Sedan"
            a = check_unavailable()
            if a == True:
                ch22=input("Car of type ",car_type," is unavailable, Do you want to pick another type (y/n)")
                if ch22=="y" or ch22=="Y":
                    None
                else :
                    orders()
                    break
            else :
                print("Order registered !")
                return car_type
                break
        elif ch21=='3' or ch21=='c' or ch21=='C':
            car_type = "Coupe"
            a = check_unavailable()
            if a == True:
                ch22=input("Car of type ",car_type," is unavailable, Do you want to pick another type (y/n)")
                if ch22=="y" or ch22=="Y":
                    None
                else :
                    orders()
                    break
            else :
                print("Order registered !")
                return car_type
                break
        elif ch21=='4' or ch21=='s' or ch21=='S':
            car_type = "SUV"
            a = check_unavailable()
            if a == True:
                ch22=input("Car of type ",car_type," is unavailable, Do you want to pick another type (y/n)")
                if ch22=="y" or ch22=="Y":
                    None
                else :
                    orders()
                    break
            else :
                print("Order registered !")
                return car_type
                break   
        else:
            print("Invalid option. Please try again!")          
def register_order():
    while 1:
        counter =str(order_id())
        searchcustomer()
        pickupdate = pickup_date()
        returndate = return_date()
        price_table()
        car_type = car_type_choose()
        if car_type =='Hatchback':
            car_price = '7 000 EUR'
        elif car_type =='Sedan':
            car_price = '12 000 EUR'
        elif car_type =='Coupe':
            car_price = '10 000 EUR'
        elif car_type =='SUV':
            car_price = '15 000 EUR'
        file1 = open("orders.txt", 'a')
        file1.write('-'+counter+'-')
        file1.write(',')
        file1.write(pickupdate)
        file1.write(',')
        file1.write(returndate)
        file1.write(',')
        file1.write(car_type)
        file1.write(',')
        file1.write(car_price)
        file1.write('\n')
        file1.close()
        ch23=input("done?! (y/n)")
        if ch23=='y' or ch23=="Y" :
            break
        else:
            None        
def delete_order():
    while 1: 
        file_read = open('orders.txt', "r")
        orderid = input("enter order id --- ")
        orderid = '-'+orderid+'-'
        lines = file_read.readlines()
        new_list = []
        idx = 0
        for line in lines:
            if orderid in line:
                new_list.insert(idx, line)
                idx += 1
        file_read.close()
        if len(new_list)==0:
            ch24=input("Order id "+orderid +"does not exist, do you want to try again ? (y/n)")
            if ch24=='y' or ch24=='Y':
                delete_order()
            else:
                break    
        else:
            lineLen = len(new_list)
            for i in range(lineLen):
                a = end=new_list[i]
            search_text = str(a)
            replace_text = ""
            with open(r'orders.txt', 'r') as file:
                data = file.read()
                data = data.replace(search_text, replace_text)
            with open(r'orders.txt', 'w') as file:
                file.write(data)
            print("Order with the id of "+ orderid +" has been successfully deleted")
            break
def print_order_list():
    file = open('orders.txt', 'r')
    print(file.read())   
def search_order():
    while 1: 
        file_read = open('orders.txt', "r")
        orderid = input("enter order id --- ")
        orderid = '-'+orderid+'-'
        lines = file_read.readlines()
        new_list = []
        idx = 0
        for line in lines:
            if orderid in line:
                new_list.insert(idx, line)
                idx += 1
        file_read.close()
        if len(new_list)==0:
            ch24=input("Order id "+orderid +"does not exist, do you want to try again ? (y/n)")
            if ch24=='y' or ch24=='Y':
                search_order()
            else:
                break    
        else:
            lineLen = len(new_list)
            for i in range(lineLen):
                print("{  Order id --- Passport number---- Pick-up date ------ Return date------ Type of car----Price}")
                print(end=new_list[i])
                break
            break
def orders():
    print("------OPTIONS------")
    print("Register an order(1)")
    print("Delete an order(2)")
    print("Print an order list(3)")
    print("Search for a specific order(4)")
    print("Go back(5)")
    while 1:
        ch12 = input("What option do you want ?---")
        if ch12 =='1' or ch12=='r':
            register_order()
            break
        elif ch12=='2' or ch12=='d':    
            delete_order()
            break
        elif ch12=='3' or ch12=='p':
            print('heel')
            print_order_list()
            print("-------OPTIONS-------")
            print("Search for a specific order(1)")
            print("Go back(2)")
            ch25 = input("---what option do you want ? ---- ")
            if ch25=='1' or ch25=='s':
                search_order()
                print("-----options ------")
                print("Delete the order(1)")
                print("Go back(2)")
                ch26 = input("What options do you want ?---  ")
                if ch26=='1' or ch26=='d' or ch26=='D':
                    delete_order()
                    break
                elif ch26=='2' or ch26=='g' or ch26=='G':    
                    orders()
                    break
            
                else :
                    print("---Invalid options try again ! ---")
                    
        elif ch12=='4' or ch12=='s':
            search_order()
            break     
        elif ch12=='5' or ch12=='g':
            main_menu()
        else:
            print("---Invalid option , try again !---")
#-----------------------------------------------------------------------------------------            
            
            
            
                      
#--CAR FUNCTION -----------------------------------------------------------------------                    
def get_license_plate():
    while 1 :
        license_plate = input("enter car's license plate ---")
        if len(license_plate)==7 and license_plate[0:4].isnumeric() and license_plate[4:8].isalpha():
            return license_plate
            break
        else:
            print("License number is of incorrect format, try again!")                       
def get_car_name():
    while 1 :
        car_name = input("enter car name ---")
        if car_name.isalpha():
            return car_name
            break
        else :
            print("Invalid format, try again!")                  
def get_car_manu():
    while 1 :
        
        car_manu=input("enter car manufacture ---")
        if car_manu.isalpha():
            return car_manu
            break
        else:
            print("Invalid format, try again!")           
def get_make_year():
    car_make_year =(input("enter Car make year---"))
    if len(car_make_year)==4 and car_make_year.isnumeric() :
        return car_make_year
        pass
    else:
        print("Invalid format, try again!")
        get_make_year()                
def get_car_type_energy():
    car_type_energy = input("Type of energy (Petrol, Diesel, Metan or Electric) type in the name----")
    if 'petrol' or 'Petrol' or 'Diesel' or 'Metan' or 'Electric' or 'electric' or 'metan' or 'diesel' in car_type_energy:
        return car_type_energy
        pass
    else:
        print("Invalid type , try again!")
        get_car_type_energy()
def get_car_type():
    ch8 = input("choose one of options from above---")
    if ch8=='1' or ch8=='h' or ch8=='H':
        car_type ='Hatchback'
    elif ch8 =='2' or ch8=='s' or ch8=='S' :
        car_type ='Sedan'
        pass
    elif ch8 == '3' or ch8=='c' or ch8=='C' :
        car_type='Coupe'
        pass
    elif ch8=='4' or ch8=='s' or ch8=='S':
        car_type ='SUV'
        pass       
    else:
        print("Invalid type , try again!")
        get_car_type()                                              
def available():
    search_text = "(1)"
    replace_text = "(0)"
    with open(r'cars.txt', 'r') as file:
        data = file.read()
        data = data.replace(search_text, replace_text)
    with open(r'cars.txt', 'w') as file:
        file.write(data)    
def unavailable():
    search_text = "(0)"
    replace_text = "(1)"
    with open(r'cars.txt', 'r') as file:
        data = file.read()
        data = data.replace(search_text, replace_text)
    with open(r'cars.txt', 'w') as file:
        file.write(data)
def assign_avalilability():
    file6=open('cars.txt','r')
    lines2=file6.readlines()
    flag = 0
    index = 0
    for line in file6:  
        index += 1  
    
    while 1 :
        ch11= input("what option do you want ? -- ")
        if ch11=='1' :
            file8 = open('cars.txt','r')
            for line in file8:  
                index += 1
                if '(0)' in line:
                    flag = 1
                    break
            if flag ==0:
                available()
                print("Car successfully moved from unavailable to available")
                break
            else:
                print("Car already on the list of available cars")
                break
        elif ch11=='2':
            file4 = open('cars.txt','r')
            for line in file4:  
                index += 1
                if '(0)' in line:
                    flag = 1
            if flag ==0:
                print("Car already on the list of unavailable cars")
                break
            else:
                unavailable()
                print("Car successfully moved from available to unavailable")
                break
                            
            
        elif ch11=='3':
            cars()
        else :
            print("Invalid option Try again!")    
def get_license_number():
    while 1 :
        license_number = input("enter license number : --- ")
        if len(license_number)==7 and license_number[0:4].isnumeric() and license_number[4:8].isalpha():
            file5 = open("cars.txt", "r")
            flag = 0
            index = 0
            for line in file5:  
                index += 1
                if license_number in line:
                    flag = 1 
                    break
            if flag == 0: 
                print(' license_number {', license_number , '} does not exist.')
                ch10=input("do you want to try again ?")
                if ch10=="y" or ch10=='Y':
                    get_license_number()
                else :
                    main_menu()
                    break
            else:
                print('', license_number, 'Found In System')
                file6=open('cars.txt')
                lines=file6.readlines()
                #print(lines[(index-1)])
                file6.close()
                print("{","--Name--","Manufacturer--","Year made--","License number--","Type of energy--", "Category--", "Availability--","}")
                print(lines[(index-1)])
                print("---OPTIONS---")
                print("Assign to the list of available cars(1)")
                print("Assign to the list of unavailable cars(2)")
                print("Go back(3)")
                assign_avalilability()           
        else :
            print("Invalid license number format! Try again")          
def searcher_with_input():
    file_name = input("Enter The File's Name: ")
    try:
        file_read = open(file_name, "r")
        text = input("Enter the String: ")
        lines = file_read.readlines()
        new_list = []
        idx = 0
        for line in lines: 
            if text in line:
                new_list.insert(idx, line)
                idx += 1
        file_read.close()
        if len(new_list)==0:
            print("\n\**** LIST IS EMPTY ! ****")
        else:
            lineLen = len(new_list)
            print("\n**** List of (/-----/)  ****\n")
            for i in range(lineLen):
                print(end=new_list[i])
            print()    
    except :
        print("\nThe file doesn't exist!")
def searcher_without_input_for_unavailable():
    try:
        file_read = open('cars.txt', "r")
        text = '(1)'
        lines = file_read.readlines()
        new_list = []
        idx = 0
        for line in lines: 
            if text in line:
                new_list.insert(idx, line)
                idx += 1
        file_read.close()
        if len(new_list)==0:
            print("\n\**** LIST IS EMPTY ! ****")
        else:
            lineLen = len(new_list)
            print("\n**** List of unavailable cars  ****\n")
            for i in range(lineLen):
                print(end=new_list[i])
            print()    
    except :
        print("\nThe file doesn't exist!")
def searcher_without_input_for_available():
    try:
        file_read = open('cars.txt', "r")
        text = '(0)'
        lines = file_read.readlines()
        new_list = []
        idx = 0
        for line in lines: 
            if text in line:
                new_list.insert(idx, line)
                idx += 1
        file_read.close()
        if len(new_list)==0:
            print("\n\**** LIST IS EMPTY ! ****")
        else:
            lineLen = len(new_list)
            print("\n**** List of available cars  ****\n")
            for i in range(lineLen):
                print(end=new_list[i])
            print()    
    except :
        print("\nThe file doesn't exist!")
def searchcar():
    get_license_number()                          
def cars():
    print("-------Cars menu-------")
    print("List of all cars in a car fleet(1)")
    print("List of unavailable cars(2)")
    print("List of available cars(3)")
    print("Search for a specific car(4)")
    print("Add new car(5)")
    print("Go back(6)")
    ch5= input("what option do you want ?---")
    if ch5 =='1':
        print("---------list of all cars---------")
        file = open('cars.txt','r')
        all_cars = file.read()
        print(all_cars)
        file.close()
        print("---------OPTIONS---------")
        print("Search for a specific car(1)")
        print("Go back(2)")
        
        ch6=input("what option do you want?---")
        if ch6 =='1':
            searchcar()
        elif ch6==2:
            cars() 
            
               
    elif ch5=='2':
        print("------list of all cars unavailable------")
        searcher_without_input_for_unavailable()
        
        
        
        print("--------OPTIONS--------")
        print("Search for a specific car(1)")
        print("Go back(2)")
        ch7=input("what option do you want?---")
        if ch7 =='1':
            searchcar()
        elif ch7=='2':
            cars()
            
            
    elif ch5 =='3':
        print("------list of all cars available------")
        searcher_without_input_for_available()
        print("Search for a specific car(1)")
        print("Go back(2)")
        ch8=input("what option do you want?---")
        if ch8 =='1':
            searchcar()
        elif ch8=='2':
            cars()
            
            
    elif ch5=='4':
        searchcar()
    elif ch5=='5':
        license_plate =get_license_plate()
        car_manu = get_car_manu()
        car_name = get_car_name()
        car_make_year = get_make_year()
        car_type_energy = get_car_type_energy()
        availability = '(0)'
        print("---------car types---------")
        print("Hatchback (1)")
        print("Sedan (2)")
        print("Coupe (3)")
        print("SUV (4)")
        while 1:
            ch8 = input("choose one of options from above---")
            if ch8=='1' or ch8=='h' or ch8=='H':
                car_type ='Hatchback'
                break
            elif ch8 =='2' or ch8=='s' or ch8=='S' :
                car_type ='Sedan'
                break
            elif ch8 == '3' or ch8=='c' or ch8=='C' :
                car_type='Coupe'
                break
            elif ch8=='4' or ch8=='s' or ch8=='S':
                car_type ='SUV'
                break                
            else:
                print("Invalid type , try again!")
        file4 =open("cars.txt", 'a')
        file4.write(car_name)
        file4.write('---')
        file4.write(car_manu)  
        file4.write('---')
        file4.write(car_make_year)
        file4.write('---')
        file4.write(license_plate)
        file4.write('---')
        file4.write(car_type_energy)
        file4.write('---')
        file4.write(car_type)
        file4.write('---')
        file4.write(availability)
        file4.write('\n') 
        file4.close()
        print("-----Car has been added!-------")
        
    elif ch5=='6':
        main_menu()
    else:
        print("-------Invalid option. Please try again!-----------")        
#--------------------------------------------------------------------------------------------    
    
    
# CUSTOMER FUNCTION---------------------------------------------------------------------------------------------------    
def deleteacustomer():
    while 1:
        passportid=input('Enter your Passport id : ')
        if len(passportid)==9 and passportid[0:7].isnumeric() and passportid[7:8]=='-' and passportid[8:9].isalpha():
            file3 = open("customers.txt", "r")
            flag = 0
            index = 0
            for line in file3:  
                index += 1
                if passportid in line:
                    flag = 1
                    break
            if flag == 0: 
                print('The customer with that passport_id :', passportid , 'does not exist.')
                ch4=input("do you want to try again ?")
                if ch4=="y":
                    None
                else :
                    customers1()
                    break
            else:
                print('', passportid, 'Found In System')
                with open("customers.txt", "r") as file3:
                    lines = file3.readlines()
                    print(lines)
                #delete user 
                
                print("customer deleted...")
                
                file3.close()
                #file3.close()
                break
            file3.close()        
        
        
        else:
            print("Passport number or ID format is SSSSSSS-A, where SSSSSSS is the seven digit serial number and A is the literal, please correct your input")            
def listcustomers():
    while 1 :
        print("-----list of current customers menu------")
        file1=open("customers.txt",'r')
        print(file1.read()) 
        print("Register new customers(1)")
        print("Delete a customer(2)")
        print("Go back(3)")
        ch2=int(input("what do you want ?"))
        if ch2==1:
            #customers()
            first_name=str(get_first_name())
            last_name = str(get_last_name())
            address=str(get_address())
            passportid=str(get_passport_id())
            credit_card=str(get_credit_card())
            file1 = open("customers.txt", 'a')
            file1.write(first_name)
            file1.write(',')
            file1.write(last_name)
            file1.write(',')
            file1.write(address)
            file1.write(',')
            file1.write(passportid)
            file1.write(',')
            file1.write(credit_card)
            file1.write('\n')
            file1.close()
            print("Customer registered successfully:","{",first_name,'-----',last_name,'-----',address,'-----',passportid,'-----',credit_card,"}")
            break
        elif ch2==2 :
            deleteacustomer()
            break
        elif ch2==3 :
            print("----back to customer menu...")
            #goback()                   
def searchcustomer():
    while 1:
        passportid=input('Enter your Passport id : ')
        if len(passportid)==9 and passportid[0:7].isnumeric() and passportid[7:8]=='-' and passportid[8:9].isalpha():
            file3 = open("customers.txt", "r")
            flag = 0
            index = 0
            for line in file3:  
                index += 1
                if passportid in line:
                    flag = 1
                    
                    break
            if flag == 0: 
                print('The customer with that passport_id :', passportid , 'does not exist.')
                ch4=input("do you want to try again ?")
                if ch4=="y":
                    None
                else :
                    customers1()
                    break
            else:
                print('', passportid, 'Found In System')
                file=open('customers.txt')
                lines=file.readlines()
                print(lines[(index-1)])
                file.close()
                break 
def main_menu():
    while 1 :
        print("-------Main Menu-------")
        print("Orders(1)")
        print("Cars(2)")
        print("Customers(3)")
        print("Register an Order(4)")
        print("Exit(5)")
        a =int(input("what you want ?! enter the number or first character of it's name ..."))
        #b = input("what you want ?! enter the number or first character of it's name ...")
        if a ==1  :
            orders()
            break
    
        elif a ==2:
            cars()
            break
    
        elif a ==3 :
        
            print("------Customer menu------")
            print("Register new customer(1)")
            print("List of current customers(2)")
            print("Search for a customer(3)")
            print("Go back(4)")
            ch=int(input("what do you want ?"))
            if ch==1 :
                customers1()
                break
            elif ch==2:
                listcustomers()
                break
            elif ch==3:
                searchcustomer()
                break
            elif ch==4:
                customers1()
                break
                
            elif ch==5:
                None    
            else:
                print("-------Invalid option. Please try again!-----------")
def customers1():
    first_name=str(get_first_name())
    last_name = str(get_last_name())
    address=str(get_address())
    passportid=str(get_passport_id())
    credit_card=str(get_credit_card())
def get_first_name():
    while 1 :
        first_name=input("enter your first name: ")
        if first_name.isalpha():
            return first_name
            break
        else:
            print("Only letters are allowed, try again")
def get_last_name():
    while 1 :
        last_name=input("enter your last name : ")
        if last_name.isalpha():
            return last_name
            break
        else:
            print("Only letters are allowed, try again")                
def get_address():
    while 1:
        address=input("enter your address: ")
        if len(address)<30:
            return address
            break
        else:
            address = address[0:30]
            return address
            break            
def get_passport_id():
    while 1 :
        passportid=input('Enter your Passport id : ')
        if len(passportid)==9 and passportid[0:7].isnumeric() and passportid[7:8]=='-' and passportid[8:9].isalpha():
            return passportid
            break
        else:
            print("Passport number or ID format is SSSSSSS-A, where SSSSSSS is the seven digit serial number and A is the literal,please correct your input")              
def get_credit_card():
    while 1:
        credit_card=input("enter your credit card : ")
        if len(credit_card)==16 and credit_card[0:16].isnumeric():
            return credit_card
            break
        else:
            print(credit_card)
            print("Expected input for the credit card number is 16 digits without blankspaces, please try again")             
                
                
                
#---------------------------------------------------------------------------------------------------------------------   


# Main program------------------------------------------------------------------------ 
'''
while 1 :
    print("-------Main Menu-------")
    print("Orders(1)")
    print("Cars(2)")
    print("Customers(3)")
    print("Register an Order(4)")
    print("Exit(5)")
    a =int(input("what you want ?! enter the number or first character of it's name ..."))
    #b = input("what you want ?! enter the number or first character of it's name ...")
    if a ==1  :
        orders()
        break
    
    elif a ==2:
        cars()
        break
    
    elif a ==3 :
        
        print("------Customer menu------")
        print("Register new customer(1)")
        print("List of current customers(2)")
        print("Search for a customer(3)")
        print("Go back(4)")
        ch=int(input("what do you want ?"))
        if ch==1 :
            #customers()
            first_name=str(get_first_name())
            last_name = str(get_last_name())
            address=str(get_address())
            passportid=str(get_passport_id())
            credit_card=str(get_credit_card())
            file1 = open("customers.txt", 'a')
            file1.write(first_name)
            file1.write(',')
            file1.write(last_name)
            file1.write(',')
            file1.write(address)
            file1.write(',')
            file1.write(passportid)
            file1.write(',')
            file1.write(credit_card)
            file1.write('\n')
            file1.close()
            print("Customer registered successfully:","{",first_name,'-----',last_name,'-----',address,'-----',passportid,'-----',credit_card,"}")
            break
        elif ch==2:
            listcustomers()
            break
        elif ch==3:
            searchcustomer()
            break
        elif ch==4:
            main_menu()
            
            
    elif a ==4 :
        #registeranorder()
        break
     
    elif a ==5 :
        main_menu()
    else:
        print("-------Invalid option. Please try again!-----------")
'''
#-----------------------------------------------------------------------------
                                    


def test_mock():
    ch=str(input("what do you want ?"))
    hc=str(input("what's up?"))
    if ch == 'yes' and hc == 'yes':
        return 'yes'
    else:
        return 'no'
                                    