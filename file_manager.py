from models import *
from inventory_manager import *
from lists import Lists
import json

def saveToFile(listGroup):
    with open("products.json", "w") as f:
        f.write("")
    productList = []
    for i in range(len(listGroup.products)):
        newProduct = listGroup.products[i].convertToDictionary()

        productList.append(newProduct)
    jsonStr = json.dumps(productList, indent=4)
    with open("products.json", "a") as f:
        f.write(jsonStr)

    with open("vendors.json", "w") as f:
        f.write("")
    vendorList = []
    for i in range(len(listGroup.vendors)):
        newVendor = listGroup.vendors[i].convertToDictionary()
        vendorList.append(newVendor)

    jsonStr = json.dumps(vendorList, indent=4)
    with open("vendors.json", "a") as f:
        f.write(jsonStr)

    with open("orders.json", "w") as f:
        f.write("")
    ordersList = []
    for i in range(len(listGroup.orders)):
        productsOrdered = listGroup.orders[i].convertToDictionary()
        ordersList.append(productsOrdered)


    jsonStr = json.dumps(ordersList, indent=4)
    with open("orders.json", "a") as f:
        f.write(jsonStr)
    print("Saved successfully!")

def loadFromFile(listGroup):
    try:
        with open("products.json", "r") as f:
            data = json.load(f)
            for i in range(len(data)):
                savedProduct = [data[i]["productID"], data[i]["name"], data[i]["category"], data[i]["quantity"], data[i]["reorderLevel"], data[i]["reorderQuantity"], data[i]["unitPrice"], data[i]["vendorID"], data[i]["status"]]
                loadedProduct = Product(savedProduct)
                listGroup.products.append(loadedProduct)
    except FileNotFoundError:
        print("There is no data to be loaded.")
    except json.decoder.JSONDecodeError:
        pass
    
    try:
        with open("vendors.json", "r") as f:
            data = json.load(f)
            for i in range(len(data)):
                savedVendor = [data[i]["vendorID"], data[i]["vendorName"], data[i]["contactName"], data[i]["phoneNumber"], data[i]["email"], data[i]["address"]]
                loadedVendor = Vendor(savedVendor)
                listGroup.vendors.append(loadedVendor)
    except FileNotFoundError:
        print("There is no data to be loaded.")
    except json.decoder.JSONDecodeError:
        pass

    try:
        with open("orders.json", "r") as f:
            data = json.load(f)
            for i in range(len(data)):
                savedOrder = [data[i]["numberPO"], data[i]["vendorID"], data[i]["dateCreated"], data[i]["itemsOrdered"], data[i]["quantityOrdered"], data[i]["totalCost"], data[i]["status"]]
                loadedOrder = PurchaseOrder(savedOrder)
                listGroup.orders.append(loadedOrder)
    except FileNotFoundError:
        print("There is no data to be loaded.")
    except json.decoder.JSONDecodeError:
        pass