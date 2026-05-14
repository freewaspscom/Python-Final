from models import *
from inventory_manager import *
from lists import Lists
import json

def saveToFile(listGroup):
    productList = []
    for i in range(len(listGroup.products)):
        newProduct = listGroup.products[i].convertToDictionary()

        productList.append(newProduct)
        print(productList)
    json_str = json.dumps(productList, indent=4)
    with open("products.json", "a") as f:
        f.write(json_str)

    vendorList = []
    for i in range(len(listGroup.vendors)):
        newVendor = listGroup.vendors[i].convertToDictionary()
        vendorList.append(newVendor)

    json_str = json.dumps(vendorList, indent=4)
    with open("vendors.json", "a") as f:
        f.write(json_str)


    ordersList = []
    for i in range(len(listGroup.orders)):
        productsOrdered = listGroup.orders[i].convertToDictionary()
        ordersList.append(productsOrdered)


    json_str = json.dumps(ordersList, indent=4)
    with open("orders.json", "a") as f:
        f.write(json_str)
    print("Saved successfully!")

def loadFromFile(listGroup):
    with open("products.json", "r") as f:
        data = json.load(f)
        print(data)