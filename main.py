
import fileinput
from datetime import datetime

_CUSTOMERS_FILE = 'customers.txt'
_CARS_FILE = 'cars.txt'
_ORDERS_FILE = 'orders.txt'

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
def search_order():
    orderid = ''
    valid = False
    found = False
    exit = False
    print("please, enter order id")
    while not valid or not found:
        valid = False
        orderid = input()
        if orderid.isnumeric():
            valid = True
            found= find_order()
            if not found:
                print("Order id"+orderid+"does not exist, do you want to try again?(Y/N)")
                response = input().upper()
                if response != Y:
                    exit=True
                    break
        else:
            print("Invalid order id format! Try again")
    if exit:
        orders()
    
    
def orders():
    print("------Order menu------")
    print("Register an order(1)")
    print("Delete an order(2)")
    print("Print an order list(3)")
    print("Search for a specific order(4)")
    print("Go back(5)")
    selection = -1
    while selection not in [1,2,3,4,5]:
        selection = int(input("Select a valid option to perform\n"))
        if selection not in [1,2,3,4,5]:
            print("Invalid option. please try again")
    if selection == 1:
        register_order()
    elif selection == 2:
        delete_order()
    elif selection ==3:
        print_order_list()
    elif selection == 4:
        search_order()
    else:
        main_menu()
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

def searchcar():
    get_license_number()   

def list_all_cars():
    print("---------list of all cars---------")
    with open('cars.txt','r') as cars_file:
        for line in cars_file:
            line_to_print = line.replace(";", ";")
            print(line_to_print, end="")
    print ("---------OPTIONS---------")
    print ("Search for a specific car(1)")
    print ("Go back(2)")
    selection = -1
    while selection not in [1,2]:
        selection = int(input())
        print("Invalid option. please try again")
        if selection == 1:
            searchcar()
        elif selection ==  2:
            cars()  
    # in the specification it didn't said to show message or to do anything if user input another number.

def list_all_available_cars():
    print("------list of all cars unavailable------")
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
    print("--------OPTIONS--------")
    print("Search for a specific car(1)")
    print("Go back(2)")
    while selection not in [1,2]:
        selection = int(input())
        print("Invalid option. please try again")
        if selection == 1:
            searchcar()
        elif selection ==  2:
            cars()  

def list_all_unavailable_cars():
   print("------list of all cars available------")
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
   except:   
        print("\nThe file doesn't exist!")

   print("--------OPTIONS--------")
   print("Search for a specific car(1)")
   print("Go back(2)")
   while selection not in [1,2]:
        selection = int(input())
        print("Invalid option. please try again")
        if selection == 1:
            searchcar()
        elif selection ==  2:
            cars()  
   
def cars():
    print("-------Cars menu-------")
    print("List of all cars in a car fleet(1)")
    print("List of unavailable cars(2)")
    print("List of available cars(3)")
    print("Search for a specific car(4)")
    print("Add new car(5)")
    print("Go back(6)")
    selection = -1
    while selection not in [1,2,3,4,5,6]:
           selection = int(input("Select a valid option to perform\n"))
           if selection not in [1,2,3,4,5,6]:
               print("Invalid option. Please try again!")
    if selection == 1:
        list_all_cars()
    elif selection == 2:
        list_all_available_cars()
    elif selection == 3:
        list_all_unavailable_cars()
    elif selection == 4:
        searchcar()
    elif selection == 5:
        license_plate = get_license_plate()
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
        
   # elif ch5=='6':
        main_menu() 
        
#--------------------------------------------------------------------------------------------    
    
    
# CUSTOMER FUNCTION---------------------------------------------------------------------------------------------------    

def customers_menu():
    print("------Customer menu------")
    print("Register new customer(1)")
    print("List of current customers(2)")
    print("Search for a customer(3)")
    print("Go back(4)")
    selection = -1
    while selection not in [1,2,3,4]:
        selection = int(input("Select a valid option to perform\n"))
        if selection not in [1,2,3,4]:
            print("Invalid option. Please try again!")
    if selection == 1:
        add_new_customer()
    elif selection == 2: 
        list_customers()
    elif selection == 3:
        search_customer()
    else:
        main_menu()


def add_new_customer():
    first_name=str(get_first_name())
    last_name = str(get_last_name())
    address=str(get_address())
    passport_id=str(get_passport_id())
    credit_card=str(get_credit_card())
    final_record = f"{first_name};{last_name};{address};{passport_id};{credit_card}"
    with open(_CUSTOMERS_FILE, 'a') as customers_file:
        customers_file.write(final_record)
    print(f"Customer registered successfully: {first_name}, {last_name}, {address}, {passport_id}, {credit_card}.")

def get_first_name():
    first_name = ''
    valid = False
    print("Please, enter your first name:")
    while not valid:
        first_name = input()
        if first_name.isalpha():
            valid = True
        else:
            print("Only letters are allowed, try again")
    return first_name

def get_last_name():
    last_name = ''
    valid = False
    print("Please, enter your last name:")
    while not valid:
        last_name = input()
        if last_name.isalpha():
            valid = True
        else:
            print("Only letters are allowed, try again")
    return last_name

def get_address():
    address = ''
    print("Please, enter your address:")
    address = input()
    if len(address)<30:
        return address
    else:
        return address[0:30]

def get_passport_id():
    passport_id = ''
    valid = False
    print("Please, enter your passport/id:")
    while not valid:
        if len(passport_id) == 9 and passport_id[0:7].isnumeric() and passport_id[7:8] == '-' and passport_id[8:9].isalpha():
            valid = True
        else:
            print("Passport number or ID format is SSSSSSS-A, where SSSSSSS is the seven-digit serial number and A is the literal, please correct your input")    
    return passport_id

def get_credit_card():
    credit_card = ''
    valid = False
    print("Please, enter your credit card:")
    while not valid:
        credit_card=input()
        if len(credit_card) == 16 and credit_card[0:16].isnumeric():
            valid = True
        else:
            print("Expected input for the credit card number is 16 digits without blank spaces, please try again")             
    return credit_card

def list_customers():
    print("-----List of current customers------")
    print("First name; Last name; Address; Passport/id; Credit card")
    with open(_CUSTOMERS_FILE, 'r') as customers_file:
        for line in customers_file:
            line_to_print = line.replace(";", "; ")
            print(line_to_print, end="")
    print("-----What to do now?------")
    print("Register new customers(1)")
    print("Delete a customer(2)")
    print("Go back(3)")
    print("Please, select an option")
    selection = -1
    while selection not in [1,2,3]:
        selection = int(input())
        print("Invalid option. Please try again!")
    if selection == 1:
        add_new_customer()
    elif selection == 2:
        delete_customer()
    else:
        customers_menu()

def delete_customer():
    passport_id = ''
    valid = False
    found_deleted = False
    exit = False
    print("Please, enter your passport/id:")
    while not valid or not found_deleted:
        valid = False
        passport_id = input()
        if len(passport_id) == 9 and passport_id[0:7].isnumeric() and passport_id[7:8] == '-' and passport_id[8:9].isalpha():
            valid = True
            found_deleted = find_delete_customer(passport_id)
            if not found_deleted:
                print(f"The customer with that passport {passport_id} does not exist, do you want to try again ? (y/n)")
                response = input().upper()
                if response != 'Y':
                    exit = True
                    break
        else:
            print("Passport number or ID format is SSSSSSS-A, where SSSSSSS is the seven-digit serial number and A is the literal, please correct your input")
    if exit:
        customers_menu()

def find_delete_customer(passport_id):
    deleted = False
    with open(_CUSTOMERS_FILE, "r") as customers_file:
        lines = customers_file.readlines()

    with open(_CUSTOMERS_FILE, "w") as customers_file:
        for line in lines:
            if passport_id in line:
                deleted = True
            else:
                customers_file.write(line)

    return deleted

def search_customer():
    passport_id = ''
    valid = False
    found = False
    exit = False
    print("Please, enter your passport/id:")
    while not valid or not found:
        valid = False
        passport_id = input()
        if len(passport_id) == 9 and passport_id[0:7].isnumeric() and passport_id[7:8] == '-' and passport_id[8:9].isalpha():
            valid = True
            found = find_diplay_customer(passport_id)
            if not found:
                print(f"The customer with that passport {passport_id} does not exist, do you want to try again ? (y/n)")
                response = input().upper()
                if response != 'Y':
                    exit = True
                    break
        else:
            print("Passport number or ID format is SSSSSSS-A, where SSSSSSS is the seven-digit serial number and A is the literal, please correct your input")
    if exit:
        customers_menu()

def find_diplay_customer(passport_id):
    found = False
    with open(_CUSTOMERS_FILE, "r") as customers_file:
        lines = customers_file.readlines()

    for line in lines:
        if passport_id in line:
            found = True
            data = line.split(";")
            print(f"Customer found: {data[0]}, {data[1]}, {data[2]}, {data[3]}, {data[4]}")

    return found         

# MAIN MENU FUNCTION---------------------------------------------------------------------------------------------------    

# TODO fix this, drop customer menu and use function like the others
# TODO also check the option nº 4 and 5 not implemented
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
