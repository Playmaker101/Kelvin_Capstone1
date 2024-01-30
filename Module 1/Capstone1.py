warehouse = {
    '1416': { 'name': 'CCTV', 'stock': 30, 'Buy Price': 20.0, 'Sell Price': 25.0, 'Brand': 'Hikvision'},
    '2320': { 'name': 'Monitor', 'stock': 10, 'Buy Price': 80.0, 'Sell Price': 96.0, 'Brand': 'Samsung'},
    '3509': { 'name': 'TV', 'stock': 10, 'Buy Price': 200.0, 'Sell Price': 250.0, 'Brand': 'LG'},
    '4104': { 'name': 'Cable', 'stock': 15, 'Buy Price': 50.0, 'Sell Price': 60.0, 'Brand': 'Hikvision'},
    '5232': { 'name': 'Switch', 'stock': 10, 'Buy Price': 30.0, 'Sell Price': 36.0, 'Brand': 'Tenda'},
}

def show_items():
    print('\t\t\tWelcome to the warehouse data')
    print("+--------+-----------+-------+-----------------+------------------+-------------+")
    print("|  Code  |  Product  | Stock | Buy Price (USD) | Sell Price (USD) |    Brand    |")
    print("+--------+-----------+-------+-----------------+------------------+-------------+")
    for code, details in warehouse.items():
        print(f"| {code:^6} | {details['name']:^9} | {details['stock']:^5} | {details['Buy Price']:^15} | {details['Sell Price']:^16} | {details['Brand']:^11} |")
    print("+--------+-----------+-------+-----------------+------------------+-------------+")

def create_item():
    print('\n')
    code = input("Enter Product code: ")
    if code in warehouse:
        print("Product with the same code already exists.")
    elif code.isdigit()==False:
        print('Product code only contains numbers')
    else:
            while True:
                item_name = input("Enter product name: ")
                if len(item_name.strip()) == 0:
                    print("'Input cannot be empty'\n")
                else:
                    break
            while True:
                item_stock = input("Enter the stock quantity: ")
                if item_stock.isdigit() == False:
                    print("'Input only contains numbers'\n")
                else:
                    break
            while True:
                item_buy = input('Enter the buy price : ')
                if item_buy.isdigit() == False:
                    print("'Input only contains numbers'\n")
                else:
                    break 
            while True:
                item_sell = input('Enter the sell price : ')
                if item_sell.isdigit() == False:
                    print("'Input only contains numbers'\n")
                else:
                    break 
            while True:
                item_brand = input("Enter product brand: ")
                if len(item_brand.strip()) == 0:
                    print("'Input cannot be empty'\n")
                else:
                    break
            print("\n+--------+-----------+-------+-----------------+------------------+-------------+")
            print("|  Code  |  Product  | Stock | Buy Price (USD) | Sell Price (USD) |    Brand    |")
            print("+--------+-----------+-------+-----------------+------------------+-------------+")
            details= {'name': item_name, 'stock': item_stock, 'Buy Price': item_buy, 'Sell Price': item_sell, 'Brand': item_brand}
            print(f"| {code:^6} | {details['name']:^9} | {details['stock']:^5} | {details['Buy Price']:^15} | {details['Sell Price']:^16} | {details['Brand']:^11} |")        
            print("+--------+-----------+-------+-----------------+------------------+-------------+")
            while True:
                confirm = input('Are you sure that you want to create this data (Y/N): ')
                print('\n')
                if confirm == 'Y' or confirm == 'y':
                    warehouse[code] = {'name': item_name, 'stock': item_stock, 'Buy Price': item_buy, 'Sell Price': item_sell, 'Brand': item_brand}
                    show_items()
                    print("'New data created successfully.'")
                    break
                elif confirm == 'N' or confirm == 'n':
                    print("'New data created has been cancelled'")
                    break
                else:
                    print('input only Y or N')

def read_item():
    code = input("Enter product code to show the data: ")
    if code in warehouse:
        item = warehouse[code]
        print('Here is your data request:')
        print("+--------+-----------+-------+-----------------+------------------+-------------+")
        print("|  Code  |  Product  | Stock | Buy Price (USD) | Sell Price (USD) |    Brand    |")
        print("+--------+-----------+-------+-----------------+------------------+-------------+")
        print(f"| {code:^6} | {item['name']:^9} | {item['stock']:^5} | {item['Buy Price']:^15} | {item['Sell Price']:^16} | {item['Brand']:^11} |")
        print("+--------+-----------+-------+-----------------+------------------+-------------+")
    else:
        print("\n'DATA NOT FOUND'.")

def update_item():
    show_items()
    def display_menu():
        print("Update Menu:")
        print("1. Update product name")
        print("2. Update stock quantity")
        print("3. Update Buy Price")
        print("4. Update Sell Price")
        print("5. Update brand")
        print("0. Return to the main menu\n")

    def update_product_info(product_code, field, new_value):
        if product_code in warehouse:
            warehouse[product_code][field] = new_value
            show_items()
            print("'Update successful.'\n")
        else:
            print("'Product code not found.'\n")

    while True:
        display_menu()
        choice = input("Enter your choice from the update menu: ")
        if choice == '0':
            main_menu()
            break

        if choice in ['1', '2', '3', '4','5']:
            print('\n')
            product_code = input("Enter the product code: ")
            if product_code not in warehouse:
                print('DATA NOT FOUND\n')
            else:
                if choice == '1':
                    new_name = input("Enter the new product name: ")
                    while True:
                        confirm = input(f'Are you sure that you want to change it to {new_name} (Y/N): ')
                        if confirm == 'Y' or confirm == 'y':
                            update_product_info(product_code, 'name', new_name)
                            break 
                        elif confirm == 'N' or confirm == 'n':
                            print("'Update cancelled'\n")
                            break
                        else:
                            print("'input only Y or N'\n")   
                elif choice == '2':
                    try:
                        new_stock = int(input("Enter the new stock quantity: "))
                        while True:
                            confirm = input(f'Are you sure that you want to change it to {new_stock} (Y/N): ')
                            if confirm == 'Y' or confirm == 'y':
                                update_product_info(product_code, 'stock', new_stock)
                                break 
                            elif confirm == 'N' or confirm == 'n':
                                print("'Update cancelled'\n")
                                break
                            else:
                                print("'input only Y or N'\n")  
                    except:
                        print('The input of stock quantity only contains integer numbers\n')
                elif choice == '3':
                    try:
                        new_buy_price = float(input("Enter the new Buy Price: "))
                        while True:
                            confirm = input(f'Are you sure that you want to change it to {new_buy_price} (Y/N): ')
                            if confirm == 'Y' or confirm == 'y':
                                update_product_info(product_code, 'Buy Price', new_buy_price)
                                break 
                            elif confirm == 'N' or confirm == 'n':
                                print("'Update cancelled'\n")
                                break
                            else:
                                print("'input only Y or N'\n")  
                    except:
                        print("'The input of the price only contains numbers'\n")
                elif choice == '4':
                    try:
                        new_sell_price = float(input("Enter the new Sell Price: "))
                        while True:
                            confirm = input(f'Are you sure that you want to change it to {new_sell_price} (Y/N): ')
                            if confirm == 'Y' or confirm == 'y':
                                update_product_info(product_code, 'Sell Price', new_sell_price)
                                break 
                            elif confirm == 'N' or confirm == 'n':
                                print("'Update cancelled'\n")
                                break
                            else:
                                print("'input only Y or N'\n") 
                    except:
                        print("'The input of the price only contains numbers'\n")
                elif choice == '5':
                    new_brand = input("Enter the new brand: ")
                    while True:
                            confirm = input(f'Are you sure that you want to change it to {new_brand} (Y/N): ')
                            if confirm == 'Y' or confirm == 'y':
                                update_product_info(product_code, 'Brand', new_brand)
                                break 
                            elif confirm == 'N' or confirm == 'n':
                                print("'Update cancelled'\n")
                                break
                            else:
                                print("'input only Y or N'\n") 
        else:
            print("Invalid choice. Please enter a number among the menu.\n")

def delete_item():
    code = input("\nWhich product code of item you want to delete: ")
    if code in warehouse:
        item = warehouse[code]
        print("+--------+-----------+-------+-----------------+------------------+-------------+")
        print("|  Code  |  Product  | Stock | Buy Price (USD) | Sell Price (USD) |    Brand    |")
        print("+--------+-----------+-------+-----------------+------------------+-------------+")
        print(f"| {code:^6} | {item['name']:^9} | {item['stock']:^5} | {item['Buy Price']:^15} | {item['Sell Price']:^16} | {item['Brand']:^11} |")
        print("+--------+-----------+-------+-----------------+------------------+-------------+")
        while True:
            confirm = input('Are you sure that you want to delete this data (Y/N): ')
            print('\n')
            if confirm == 'Y' or confirm == 'y':
                del warehouse[code]
                show_items()
                print("'Data deleted successfully.'")
                break
            elif confirm == 'N' or confirm == 'n':
                print("'Delete data option has been cancelled'")
                break
            else:
                print("'input only Y or N'")
    else:
        print("'DATA NOT FOUND'")
    
menu = {
    '1': '1. View Warehouse Data', 
    '2': '2. Create new data', 
    '3': '3. Read data', 
    '4': '4. Update data', 
    '5': '5. Delete data',
    '6': '6. Exit'
    }
# Print main menu
def main_menu():
    print("\nWarehouse Data System:")
    for num in menu:
        print(menu[num])
main_menu()

while True:
    print('\n')
    choice = input("Enter your choice: ")
    if choice == '1':
        show_items()
        print(menu['2']);print(menu['3']);print(menu['4']);print(menu['5']);print(menu['6'])
    elif choice == '2':
        create_item()
        while True:
            print('\n1. create another new data')  
            print('0. Return to main menu')
            choice = input("Enter your choice: ")
            if choice == '0':
                main_menu()
                break
            elif choice == '1':
                create_item()
            else:
                print("'Invalid choice. Please enter a correct number from the menu.'")
    elif choice == '3':
        read_item()
        while True:
            print('\n')
            print('1. Read another data')  
            print('0. Return to main menu')
            choice = input("Enter your choice: ")
            if choice == '0':
                main_menu()
                break
            elif choice == '1':
                print('\n')
                read_item()
            else:
                print("'Invalid choice. Please enter a correct number from the menu.'")
    elif choice == '4':
        update_item()
    elif choice == '5':
        show_items()
        print('1. Delete certain data')
        print('2. Clear all data')
        print('0. Return to the main menu')
        while True:
            opt = input('which option do you choose: ')
            if opt == '1':
                delete_item()
                break
            elif opt == '2':
                warehouse.clear()
                show_items()
                break
            elif opt == '0':
                main_menu()
                break
            else:
                print("'Invalid choice. Please enter a correct number from the menu.'")
        if not warehouse:
            print("'All data deleted. Exiting the Warehouse Management System.'\n")
            break
        elif opt == '1':
            while True:
                print('\n1. Delete another data')
                print('2. Clear all data')
                print('0. Return to the main menu')
                choice = input('Enter your choice: ')
                if choice == '1':
                    delete_item()
                    if not warehouse:
                        break 
                elif choice == '0':
                    main_menu()
                    break
                elif choice == '2':
                    warehouse.clear()
                    show_items()
                    break
                else:
                    print("'Invalid choice. Please enter a number among the menu.'\n")
        if not warehouse:
            print("'All data deleted. Exiting the Warehouse Management System.'\n")
            break       
    elif choice == '6':
        print("'Exiting the Warehouse Data System. Goodbye!'\n")
        break
    else:
        print("'Invalid choice. Please enter a correct number from the menu.'")
