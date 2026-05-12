from models import *
from inventory_manager import *
from lists import Lists


# Variables go here
listGroup = Lists()
lowStock = 30


# Temporary functions location while I work on making it work elsewhere
def searchProducts(search):
    for i in range(len(listGroup.products)):
        if search == listGroup.products[i].name:
            print("Product found!")
            return i
    else:
        print("Product not found.")


def removeProduct():
    search = input("Enter the product name...\n> ")
    productItem = searchProducts(search)
    listGroup.products.pop(productItem)


def orderProducts():
    orderList = {}
    while True:
        print('Type "Done" to finish adding items.')
        search = input("Enter the product name...\n> ")
        if search.lower() != "done":
            i = searchProducts(search)
            orderList["Name"] = listGroup.products[i].name
            orderList["Cost"] = listGroup.products[i].unitPrice
        else:
            break



def displayLowStock():
    for i in range(len(listGroup.products)):
        if listGroup.products[i].quantity <= 30:
            print(f"{listGroup.products[i].name}\n{listGroup.products[i].quantity} left")


def searchVendors():
    search = input("Enter the vendor name...\n> ")
    for i in range(len(listGroup.vendors)):
        if search == listGroup.vendors[i].vendorName:
            print("Vendor found!")
            return i
    else:
        print("Vendor not found.")


def removeVendor():
    search = input("Enter the vendor name...\n> ")
    vendorItem = searchVendors()
    listGroup.vendors.pop(vendorItem)


def vendorSelector():
    searchVendors()
    return listGroup.vendors[i].vendorID





# Actual program starts here ------------------------------------------------------------------------------------------------------------------------------------------------------------
while True:
    print("Product Manager")
    print("Which would you like to use?")
    print("1. Product Management\n2. Vendor Management\n3. Purchase Order System\n4. Shipment Recieving\n5. Search\n6. Sort\n7. Report\nSave and Load\n8. Exit")
    selection = input("> ")
    
    
    
    

    # Products --------------------------------------------------------------------------------------------------------------------------------------------------------------------
    if selection == "1":
        while True:
            print("Product Management")
            print("1. Add a Product\n2. View All Products\n3. Search for a Product\n4. Deactivate a Product\n5. Display Low-Stock Products\n6. Back to Main Menu")
            selection = input("> ")



            if selection == "1":
                newProduct = Product()
                listGroup.products.append(newProduct)
                print("Product successfully added!")

            elif selection == "2":
                for i in range(len(listGroup.products)):
                    print(listGroup.products[i].name)

            elif selection == "3":
                search = input("Enter the product name...\n> ")
                searchProducts(search)

            elif selection == "4":
                removeProduct()

            elif selection == "5":
                displayLowStock()

            elif selection == "6":
                break

            else:
                print("That is not a valid option. Please try again.")






    # Vendors --------------------------------------------------------------------------------------------------------------------------------------------------------------------
    elif selection == "2":
        while True:
            print("Vendor Management")
            print("1. Add a Vendor\n2. View All Vendors\n3. Search for a Vendor\n4. Deactivate a Vendor\n5. Back to Main Menu")
            selection = input("> ")



            if selection == "1":
                newVendor = Vendor()
                listGroup.vendors.append(newVendor)
                print("Vendor successfully added!")

            elif selection == "2":
                for i in range(len(listGroup.vendors)):
                    print(listGroup.vendors[i].vendorName)

            elif selection == "3":
                searchVendors()

            elif selection == "4":
                removeVendor()

            elif selection == "5":
                break

            else:
                print("That is not a valid option. Please try again.")






    # Purchase Order System -------------------------------------------------------------------------------------------------------------------------------------------------------------
    elif selection == "3":
        while True:
            print("Purchase Ordering")
            print("1. Create an Order\n2.View Existing Orders\n3.Mark Order as Recieved\n4. Back to Main Menu")
            selection = input("> ")



            if selection == "1":
                newOrder = PurchaseOrder()
                listGroup.orders.append(newOrder)
                print("Vendor successfully added!")

            elif selection == "2":
                for i in range(len(listGroup.orders)):
                    print(listGroup.orders[i].itemsOrdered)

            elif selection == "3":
                searchVendors()

            elif selection == "4":
                break

            else:
                print("That is not a valid option. Please try again.")































    else:
        print("That is not a valid option. Please try again.")






# Apparently swearing in code comments means the code is higher quality, so here I go... heck