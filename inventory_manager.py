from models import Product
from models import Vendor
from models import PurchaseOrder
from lists import Lists


def searchProducts(search, listGroup): # Searches the array for the product the user specifies
    for i in range(len(listGroup.products)):
        if search == listGroup.products[i].name:
            print("Product found!")
            return i # Returns the index value of the product
    else:
        print("Product not found.")


def removeProduct(listGroup): # Takes the specified item out of the list
    search = input("Enter the product name...\n> ")
    productItem = searchProducts(search)
    listGroup.products.pop(productItem)


def orderProducts(listGroup): # Allows the user to order as many products as they would like
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



def displayLowStock(listGroup, lowStock):
    for i in range(len(listGroup.products)):
        if listGroup.products[i].quantity <= lowStock:
            print(f"{listGroup.products[i].name}\n{listGroup.products[i].quantity} left")


def searchVendors(search):
    for i in range(len(listGroup.vendors)):
        if search == listGroup.vendors[i].vendorName:
            print("Vendor found!")
            return i
    else:
        print("Vendor not found.")


def removeVendor(listGroup):
    search = input("Enter the vendor name...\n> ")
    vendorItem = searchVendors(search)
    listGroup.vendors.pop(vendorItem)


def vendorSelector(listGroup):
    search = input("Enter the vendor name...\n> ")
    searchVendors(search)
    return listGroup.vendors[i].vendorID


def searchPOs(search, listGroup):
    for i in range(len(listGroup.orders)):
        if search == listGroup.sort[i].numberPO:
            print("Order found!")
            return i
    else:
        print("Order not found.")


def markRecieved(listGroup):
     search = input("What is the PO number?\n> ").strip()
     i = searchPOs(search)
     listGroup.sort[i].status = "Delivered"
