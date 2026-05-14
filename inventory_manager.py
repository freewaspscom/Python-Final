from models import Product
from models import Vendor
from models import PurchaseOrder
from lists import Lists


def searchProducts(search, listGroup): # Searches the array for the product the user specifies | Parameters: user search, the list group 
    for i in range(len(listGroup.products)):
        if search == listGroup.products[i].name:
            print("Product found!")
            return i # Returns the index value of the product
    else:
        print("Product not found.")


def searchProductCategories(search, listGroup): # Searches the array for the product category | Parameters: user search, the list group 
    for i in range(len(listGroup.products)):
        if search == listGroup.products[i].category:
            print("Product found!")
            return i # Returns the index value of the product
    else:
        print("Product not found.")


def removeProduct(listGroup): # Takes the specified item out of the list | Parameter: The list group 
    search = input("Enter the product name...\n> ")
    productItem = searchProducts(search, listGroup)
    listGroup.products.pop(productItem)


def orderProducts(listGroup): # Allows the user to order as many products as they would like | Parameter: The list group 
    itemList = []
    while True:
        print('Type "Done" to finish adding items.')
        search = input("Enter the product name...\n> ")
        if search.lower() != "done":
            i = searchProducts(search, listGroup)
            orderList = {}
            orderList["name"] = listGroup.products[i].name
            orderList["cost"] = float(listGroup.products[i].unitPrice)
            orderList["reorderQuantity"] = int(listGroup.products[i].reorderQuantity)
            itemList.append(orderList)
        else:
            return itemList # Returns the list of items
            break



def displayLowStock(listGroup, lowStock): # Displays products that are considered low stock | Parameters: The list group, the value considered low stock 
    for i in range(len(listGroup.products)):
        if listGroup.products[i].quantity <= lowStock:
            print(f"{listGroup.products[i].name}\n{listGroup.products[i].quantity} left")


def searchVendors(listGroup, search): # Searches through vendors | Parameters: user search, the list group 
    for i in range(len(listGroup.vendors)):
        if search == listGroup.vendors[i].vendorName:
            print("Vendor found!")
            return i # Returns the vendor index
    else:
        print("Vendor not found.")


def removeVendor(listGroup): # Removes a vendor | Parameter: The list group 
    search = input("Enter the vendor name...\n> ")
    vendorItem = searchVendors(listGroup, search)
    listGroup.vendors.pop(vendorItem)


def vendorSelector(listGroup): # Selects a vendor for an order | Parameter: The list group 
    search = input("Enter the vendor name...\n> ")
    i = searchVendors(listGroup, search)
    return listGroup.vendors[i].vendorID


def searchPOs(search, listGroup): # Searches orders | Parameters: user search, the list group 
    for i in range(len(listGroup.orders)):
        if search == listGroup.orders[i].numberPO:
            print("Order found!")
            return i # Returns the order index
    else:
        print("Order not found.")


def markRecieved(listGroup): # Marks an order as recieved | Parameter: The list group 
    search = input("What is the PO number?\n> ").strip()
    i = searchPOs(search, listGroup)
    if listGroup.orders[i].status != "Delivered":
        listGroup.orders[i].status = "Delivered"
        for j in range(len(listGroup.orders[i].itemsOrdered)):
            for k in range(len(listGroup.products)):
                if listGroup.orders[i].itemsOrdered[j]["name"] == listGroup.products[k].name:
                    listGroup.products[k].quantity += listGroup.orders[i].itemsOrdered[j]["reorderQuantity"]
        print("Order marked as recieved!")
    else:
        print("This order has already been recieved.")


def calculateQuantity(itemsOrdered): # Calculates the total amount ordered | Parameter: The items placed for order
    totalAmount = 0
    for i in range(len(itemsOrdered)):
        totalAmount += itemsOrdered[i]["reorderQuantity"]
    return totalAmount # Returns the total amount ordered

def calculateTotal(itemsOrdered): # Calculates the total cost | Parameter: The items placed for order
    totalAmount = 0
    for i in range(len(itemsOrdered)):
        itemCost = itemsOrdered[i]["reorderQuantity"] * itemsOrdered[i]["cost"]
        totalAmount += itemCost
    return totalAmount # Returns the total cost

