class Product:
    
    def __init__(self):
        self.productID = input("What is the ID of the product?\n> ").strip()
        self.name = input("What is the name of the product?\n> ").strip()
        self.category = input("What category is the product?\n> ").strip()
        self.quantity = int(input("How many of this product are being ordered?\n> ").strip())
        self.reorderLevel = int(input("How many do you want in stock?\n> ").strip())
        self.reorderQuantity = 5 # Replace this with reorderLevel - quantity
        self.unitPrice = int(input("What is the price of each individual item?\n> ").strip())
        self.vendorID = input("What is the ID of the vendor?\n> ").strip()
        self.status = input("What is the status of the product?\n> ").strip()
        self.content = {
            "productID": self.productID,
            "name": self.name,
            "category": self.category,
            "quantity": self.quantity,
            "reorderLevel": self.reorderLevel,
            "reorderQuantity": self.reorderQuantity,
            "unitPrice": self.unitPrice,
            "vendorID": self.vendorID,
            "status": self.status,
        }

class Vendor:

    def __init__(self):
        self.vendorID = input("What is the ID of the vendor?\n> ").strip()
        self.vendorName = input("What is the name of the vendor?\n> ").strip()
        self.contactName = input("What is the contact name of the vendor?\n> ").strip()
        self.phoneNumber = input("What is the phone number of the vendor?\n> ").strip()
        self.email = input("What is the email of the vendor?\n> ").strip()
        self.address = input("What is the address of the vendor?\n> ").strip()

class PurchaseOrder:
    
    def __init__(self):
        self.NumberPO = input("What is the PO number?\n> ").strip()
        self.vendorID = vendorSelector()
        self.dateCreated = input("What is the date the order started?\n> ").strip()
        self.itemsOrdered = orderProducts()
        self.quantityOrdered = len(itemsOrdered)
        self.totalCost = input("What was the total cost?\n> ").strip()
        self.status = input("What is the status?\n> ").strip()