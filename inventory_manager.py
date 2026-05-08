from models import Product
from models import Vendor
from models import PurchaseOrder

def addProduct():
    productID = input("What is the ID of the product?\n>")
    name = input("What is the name of the product?\n>")
    category = input("What category is the product?\n>")
    quantity = input("How many of this product are being ordered?\n>")
    reorderLevel = input("How many do you want in stock?\n>")
    reorderQuantity = 5 # Replace this with reorderLevel - quantity
    unitPrice = input("What is the price of each individual item?\n>")
    vendorID = input("What is the ID of the vendor?\n>")
    status = input("What is the status of the product?\n>")

    newProduct = Product(productID, name, category, quantity, reorderLevel, reorderQuantity, unitPrice, vendorID, status)
    return newProduct