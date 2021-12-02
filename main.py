
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
        file_read = open(_CARS_FILE, "r")
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
    orderid = ''
    valid = False
    found_deleted = False
    exist = False
    print("Please, enter order id:")
    while not valid or not found_deleted:
        valid = False
        orderid = input()
        if orderid.isnumeric():
            valid = True
            found_deleted = find_delete_order(orderid)
            if not found_deleted:
                print(f"The order id does not exist, do you want to try again?(Y/N)")
                response= input().upper
                if response != 'Y':
                  exist=True
                  break
        else:
            print("order id format is wrong,try again!")
    if exit:
        orders()

def find_delete_order(orderid):
    deleted = False
    with open(_ORDERS_FILE, "r") as orders_file:
        lines = order_file.readlines()

    with open(_CUSTOMERS_FILE, "w") as customers_file:
        for line in lines:
            if orderid in line:
                deleted = True
            else:
                order_file.write(line)
    return deleted

def print_order_list():
  #  file = open('orders.txt', 'r')
  #   print(file.read())
    with open(_ORDERS_FILE, 'r') as order_file:
        for line in order_file:
            line_to_print = line.replace(";", "; ")
            print(line_to_print, end="")
    print("-------OPTIONS-------")
    print("Search for a specific order(1)")
    print("Go back(2)")
    selection = '-1'
    while selection not in ['1','2']:
        selection = input()
        print("Invalid option. please try again")
    if selection == '1':
        search_order()
    else:
        orders() 
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
        
def find_order():
    found = False
    with open(_ORDERS_FILE,"r") as order_file:
        lines = order_file.readline()
    for line in lines:
        if orderid in line:
            found = True
            data = line.split(";")
            print(f"Order found:{data[0]}, {data[1]}, {data[2]}, {data[3]}, {data[4]}, {data[5]}")
    return found
    
    
def orders():
    print("------Order menu------")
    print("Register an order(1)")
    print("Delete an order(2)")
    print("Print an order list(3)")
    print("Search for a specific order(4)")
    print("Go back(5)")
    selection = '-1'
    while selection not in ['1','2','3','4','5']:
        selection = input("Select a valid option to perform\n")
        if selection not in ['1','2','3','4','5']:
            print("Invalid option. please try again")
    if selection == '1':
        register_order()
    elif selection == '2':
        delete_order()
    elif selection == '3':
        print_order_list()
    elif selection == '4':
        search_order()
    else:
        main_menu()
#-----------------------------------------------------------------------------------------            
            
            
            
                      
#--CAR FUNCTION -----------------------------------------------------------------------        

def add_new_car():
    license_plate = get_license_plate()
    car_manu = get_car_manu()
    car_name = get_car_name()
    car_make_year = get_make_year()
    car_type_energy = get_car_type_energy()
    car_type = get_car_type()
    availability = '(0)'
    final_record = f"{car_name}; {car_manu}; {car_make_year}; {license_plate}; {car_type_energy}; {car_type}; (0)"
    with open(_CARS_FILE, 'a') as cars_file:
        cars_file.write(final_record)
    print("Car has been added!")
    
def check_if_license_exist(license_plate):
    with open(_CARS_FILE, "r") as cars_file:
        lines = cars_file.readlines()

    for line in lines:
        if license_plate in line:
            return True
    
    return False

def get_license_plate():
    license_plate = ''
    valid = False
    print("Please, enter the license plate:")
    while not valid:
        license_plate = input()
        if len(license_plate)==7 and license_plate[0:4].isnumeric() and license_plate[4:7].isalpha():
            if not check_if_license_exist(license_plate):
                valid = True
            else:
                print("A car with this license number is already registered in the system")
        else:
            print("License number is of incorrect format, try again")
    return license_plate
                   
def get_car_name():
    car_name = ''
    valid = False
    print("Please, enter car name")
    while not valid:
        car_name = input()
        if len(car_name) > 0:
            valid = True
        else :
            print("Invalid format, try again!")
    
    return car_name

def get_car_manu():
    manufacturer = ''
    valid = False
    print("Please, enter car manufacturer")
    while not valid:
        manufacturer = input()
        if len(manufacturer) > 0:
            if not True in [char.isdigit() for char in manufacturer]:
                valid = True
        else:
            print("Invalid format, try again!")    
    return manufacturer

def get_make_year():
    car_make_year = ''
    valid = False
    print("Please, enter car make year")
    while not valid:
        car_make_year = input()
        if len(car_make_year) == 4 and car_make_year.isnumeric():
            valid = True
        else:
            print("Invalid format, try again!")
    return car_make_year

def get_car_type_energy():
    car_type_energy = ''
    valid = False
    print("Please, enter type of energy")
    print("Type of energy (Petrol, Diesel, Metan or Electric) type in the name")
    while not valid:
        car_type_energy = input().lower()
        if 'petrol' == car_type_energy or 'electric' == car_type_energy or 'metan' == car_type_energy or 'diesel' == car_type_energy:
            valid = True
        else:
            print("Wrong type of fuel, try again!")
    return car_type_energy

def get_car_type():
    car_type = ''
    valid = False
    print("---------car types---------")
    print("Hatchback (1)")
    print("Sedan (2)")
    print("Coupe (3)")
    print("SUV (4)")
    print("Please, select car type")
    while not valid:
        car_type = input()
        if car_type not in ['1', '2', '3', '4']:
            rint("Invalid type , try again!")
    if car_type == '1':
        return 'Hatchback'
    elif car_type == '2':
        return 'Sedan'
    elif car_type == '3':
        return 'Coupe'
    else:
        return 'SUV'
                                        
def assign_avalilability(license_number, availability):
    exit = False
    with open(_CARS_FILE, "r") as cars_file:
        lines = cars_file.readlines()

    with open(_CARS_FILE, "w") as cars_file:
        for line in lines:
            if license_number in line:
                if availability in line:
                    if availability == '(0)':
                        print("Car already on the list of available cars")
                    else:
                        print("Car already on the list of unavailable cars")
                    exit = True
                else:
                    if availability == '(0)':
                        line = line.replace('(1)', '(0)')
                        print("Car successfully moved from unavailable to available")
                    else:
                        line = line.replace('(0)', '(1)')
                        print("Car successfully moved from unavailable to available")
                    cars_file.write(line)
            else:
                cars_file.write(line)

    if exit:
        assign_avalilability_menu(license_number)   

def assign_avalilability_menu(license_number):
    print("---OPTIONS---")
    print("Assign to the list of available cars(1)")
    print("Assign to the list of unavailable cars(2)")
    print("Go back(3)")
    selection = '-1'
    print("Please, enter your choice:")
    while selection not in ['1','2','3']:
        selection = input()
        if selection not in ['1','2','3']:
            print("Invalid option. Please try again!")
    if selection == '1':
        assign_avalilability(license_number, '(0)')
    elif selection == '2':
        assign_avalilability(license_number, '(1)')
    else:
        cars()

def get_license_number():
    print("Please, enter a license number:")
    license_number = ''
    valid = False
    found = False
    exit = False
    while not valid or not found:
        valid = False
        license_number = input()
        if len(license_number)==7 and license_number[0:4].isnumeric() and license_number[4:8].isalpha():
            valid = True
            file_to_read = open(_CARS_FILE, "r")
            flag = 0
            index = 0
            for line in file_to_read:  
                index += 1
                if license_number in line:
                    flag = 1
                    found = True 
                    break
            file_to_read.close()
            if flag == 0: 
                print(f'License_number {license_number} does not exist, do you want to try again ? (Y/y)')
                ch10=input().upper()
                if ch10 !='Y':
                    exit = True
                    break
            else:
                print(f'{license_number} found In System!')
                file_to_read=open(_CARS_FILE)
                lines=file_to_read.readlines()
                file_to_read.close()
                print("{","--Name--","Manufacturer--","Year made--","License number--","Type of energy--", "Category--", "Availability--","}")
                print(lines[(index-1)])                
        else :
            print("Invalid license number format! Try again")

    if exit:
        cars()

    assign_avalilability_menu(license_number)

def searchcar():
    get_license_number()   

def list_all_cars():
    print("---------list of all cars---------")
    with open(_CARS_FILE,'r') as cars_file:
        for line in cars_file:
            line_to_print = line.replace(";", ";")
            print(line_to_print, end="")
    print ("---------OPTIONS---------")
    print ("Search for a specific car(1)")
    print ("Go back(2)")
    selection = '-1'
    while selection not in ['1','2']:
        selection = input()
        if selection not in ['1','2']:
            print("Invalid option. please try again")
    if selection == '1':
        searchcar()
    elif selection == '2':
        cars()  
    # in the specification it didn't said to show message or to do anything if user input another number.

def list_all_available_cars():
    print("------list of all cars available------")
    try:
        file_read = open(_CARS_FILE, "r")
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
            print("\n**** List of unavailable cars  ****\n")
            for i in range(lineLen):
                print(new_list[i])
    except :
        print("\nThe file doesn't exist!")
    print("--------OPTIONS--------")
    print("Search for a specific car(1)")
    print("Go back(2)")
    selection = '-1'
    while selection not in ['1','2']:
        selection = input()
        if election not in ['1','2']:
            print("Invalid option. please try again")
    if selection == '1':
        searchcar()
    else:
        cars()  

def list_all_unavailable_cars():
    print("------list of all cars unavailable------")
    try:
        file_read = open(_CARS_FILE, "r")
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
            print("\n**** List of available cars  ****\n")
            for i in range(lineLen):
                print(new_list[i])
    except:   
        print("\nThe file doesn't exist!")

    print("--------OPTIONS--------")
    print("Search for a specific car(1)")
    print("Go back(2)")
    selection = '-1'
    while selection not in ['1','2']:
        selection = input()
        if selection not in ['1','2']:
                print("Invalid option. please try again")
    if selection == '1':
        searchcar()
    else:
        cars()  
   
def cars():
    print("-------Cars menu-------")
    print("List of all cars in a car fleet(1)")
    print("List of unavailable cars(2)")
    print("List of available cars(3)")
    print("Search for a specific car(4)")
    print("Add new car(5)")
    print("Go back(6)")
    selection = '-1'
    print("Select a valid option to perform")
    while selection not in ['1','2','3','4','5','6']:
           selection = input()
           if selection not in ['1','2','3','4','5','6']:
               print("Invalid option. Please try again!")
    if selection == '1':
        list_all_cars()
    elif selection == '2':
        list_all_unavailable_cars()
    elif selection == '3':
        list_all_available_cars()
    elif selection == '4':
        searchcar()
    elif selection == '5':
        add_new_car()
    else:
        main_menu() 
        
#--------------------------------------------------------------------------------------------    
    
    
# CUSTOMER FUNCTION---------------------------------------------------------------------------------------------------    

def customers_menu():
    print("------Customer menu------")
    print("Register new customer(1)")
    print("List of current customers(2)")
    print("Search for a customer(3)")
    print("Go back(4)")
    selection = '-1'
    while selection not in ['1','2','3','4']:
        selection = input("Select a valid option to perform\n")
        if selection not in ['1','2','3','4']:
            print("Invalid option. Please try again!")
    if selection == '1':
        add_new_customer()
    elif selection == '2': 
        list_customers()
    elif selection == '3':
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
    selection = '-1'
    while selection not in ['1','2','3']:
        selection = input()
        if selection not in ['1','2','3']:
            print("Invalid option. Please try again!")
    if selection == '1':
        add_new_customer()
    elif selection == '2':
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

def main_menu():
    print("-------Main Menu-------")
    print("Orders(1)")
    print("Cars(2)")
    print("Customers(3)")
    print("Register an Order(4)")
    print("Exit(5)")
    print("Please, enter your choice")
    selection = '-1'
    while selection not in ['1','2','3','4','5']:
        selection = input()
        if selection not in ['1','2','3','4','5']:
            print("Invalid option. Please try again!")
    if selection == '1':
        orders()
    elif selection == '2':
        cars()
    elif selection == '3':
        customers_menu()
    elif selection == '4':
            register_order()
    else:
        exit()
             
#---------------------------------------------------------------------------------------------------------------------   


# Main program------------------------------------------------------------------------ 
# TODO -> BEFORE UPLOAD ASSIGNMENT, CREATE IN HERE THE TYPICAL MAIN CALL TO MAIN_MENU
#-----------------------------------------------------------------------------
