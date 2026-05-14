from models import *
from inventory_manager import *
from lists import Lists
from file_manager import *
from reports import *
import json



# Variables go here
listGroup = Lists()
lowStock = 30





# Actual program starts here ------------------------------------------------------------------------------------------------------------------------------------------------------------
while True:
    print("Product Manager")
    print("Which would you like to use?")
    print("1. Product Management\n2. Vendor Management\n3. Purchase Order System\n4. Create Report\n5. Save and Load\n6. Exit")
    selection = input("> ")
    
    
    
    

    # Products --------------------------------------------------------------------------------------------------------------------------------------------------------------------
    if selection == "1":
        while True:
            print("Product Management")
            print("1. Add a Product\n2. View All Products\n3. Search for a Product Name\n4. Search for a Product Category\n5. Sort by Category\n6. Deactivate a Product\n7. Display Low-Stock Products\n8. Back to Main Menu")
            selection = input("> ")



            if selection == "1":
                productID = input("What is the ID of the product?\n> ").strip()
                name = input("What is the name of the product?\n> ").strip()
                category = input("What category is the product?\n> ").strip()
                quantity = int(input("How many of this product are being ordered?\n> ").strip())
                reorderLevel = int(input("How many do you want in stock?\n> ").strip())
                reorderQuantity = reorderLevel - quantity
                unitPrice = float(input("What is the price of each individual item?\n> ").strip())
                vendorID = input("What is the ID of the vendor?\n> ").strip()
                status = input("What is the status of the product?\n> ").strip()
                productItems = [productID, name, category, quantity, reorderLevel, reorderQuantity, unitPrice, vendorID, status]
                newProduct = Product(productItems)
                listGroup.products.append(newProduct)
                print("Product successfully added!")

            elif selection == "2":
                for i in range(len(listGroup.products)):
                    print(listGroup.products[i].name)

            elif selection == "3":
                search = input("Enter the product name...\n> ")
                searchProducts(search, listGroup)

            elif selection == "4":
                search = input("Enter the product category...\n> ")
                searchProductCategories(search, listGroup)


            elif selection == "5":
                sortedProducts = sorted(listGroup.products, key=lambda x: x.category)
                for i in range(len(sortedProducts)):
                    print(listGroup.products[i].name)


            elif selection == "6":
                removeProduct(listGroup)

            elif selection == "7":
                displayLowStock(listGroup, lowStock)

            elif selection == "8":
                break

            else:
                print("That is not a valid option. Please try again.")






    # Vendors --------------------------------------------------------------------------------------------------------------------------------------------------------------------
    elif selection == "2":
        while True:
            print("Vendor Management")
            print("1. Add a Vendor\n2. View All Vendors\n3. Search for a Vendor\n4. Deactivate a Vendor\n5. Sort by Vendor Name\n6. Back to Main Menu")
            selection = input("> ")



            if selection == "1":
                vendorID = input("What is the ID of the vendor?\n> ").strip()
                vendorName = input("What is the name of the vendor?\n> ").strip()
                contactName = input("What is the contact name of the vendor?\n> ").strip()
                phoneNumber = input("What is the phone number of the vendor?\n> ").strip()
                email = input("What is the email of the vendor?\n> ").strip()
                address = input("What is the address of the vendor?\n> ").strip()
                vendorItems = [vendorID, vendorName, contactName, phoneNumber, email, address]
                newVendor = Vendor(vendorItems)
                listGroup.vendors.append(newVendor)
                print("Vendor successfully added!")

            elif selection == "2":
                for i in range(len(listGroup.vendors)):
                    print(listGroup.vendors[i].vendorName)

            elif selection == "3":
                search = input("Enter the vendor name...\n> ")
                searchVendors(listGroup, search)

            elif selection == "4":
                removeVendor(listGroup)
            
            elif selection == "5":
                sortedVendors = sorted(listGroup.vendors, key=lambda x: x.vendorName)
                for i in range(len(sortedVendors)):
                    print(listGroup.vendors[i].vendorName)

            elif selection == "6":
                break

            else:
                print("That is not a valid option. Please try again.")






    # Purchase Order System -------------------------------------------------------------------------------------------------------------------------------------------------------------
    elif selection == "3":
        while True:
            print("Purchase Ordering")
            print("1. Create an Order\n2.View Active Orders\n3.Mark Order as Recieved\n4. Sort by Cost\n5. Back to Main Menu")
            selection = input("> ")



            if selection == "1":
                numberPO = input("What is the order number?\n> ").strip()
                vendorID = vendorSelector(listGroup)
                dateCreated = input("What is the date the order started?\n> ").strip()
                itemsOrdered = orderProducts(listGroup)
                quantityOrdered = calculateQuantity(itemsOrdered)
                totalCost = calculateTotal(itemsOrdered)
                orderItems = [numberPO, vendorID, dateCreated, itemsOrdered, quantityOrdered, totalCost]
                newOrder = PurchaseOrder(orderItems)
                listGroup.orders.append(newOrder)
                print("Order placed!")

            elif selection == "2":
                for i in range(len(listGroup.orders)):
                    if listGroup.orders[i].status != "Delievered":
                        print(listGroup.orders[i].itemsOrdered)

            elif selection == "3":
                markRecieved(listGroup)
            
            elif selection == "4":
                sortedOrders = sorted(listGroup.orders, key=lambda x: x.totalCost)
                for i in range(len(sortedOrders)):
                    print(listGroup.orders[i].totalCost)

            elif selection == "5":
                break

            else:
                print("That is not a valid option. Please try again.")












    # Reports----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    elif selection == "4":
        while True:
            print("1. Full Report\n2. Low Stock Report\n3. Total Inventory Value\n4. Exit")
            selection = input("> ")



            if selection == "1":
                fullReport(listGroup)

            elif selection == "2":
                lowStockReport(listGroup, lowStock)

            elif selection == "3":
                totalInventoryValue(listGroup)

            elif selection == "4":
                break

            else:
                print("That is not a valid option. Please try again.")   















    # Save and load -----------------------------------------------------------------------------------------------------------------------------------------------------------------
    elif selection == "5":
        print("1. Save\n2. Load\nNote: Load data before saving to avoid data loss.")
        selection = input("> ")
        if selection == "1":
            saveToFile(listGroup)
        elif selection == "2":
            loadFromFile(listGroup)
        else:
            print("That is not a valid option. Please try again.")












    elif selection == "6":
        print("Exiting program...")
        break

    else:
        print("That is not a valid option. Please try again.")






# Apparently swearing in code comments means the code is higher quality, so here I go... heck