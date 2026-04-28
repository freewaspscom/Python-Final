class Product:
    
    def __init__(self):
        self.productID = productID
        self.name = name 
        self.category = category
        self.quantity = quantity
        self.reorderLevel = reorderLevel
        self.reorderQuantity = reorderQuantity
        self.unitPrice = unitPrice
        self.vendorID = vendorID
        self.status = status
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
        self.vendorID = vendorID
        self.vendorName = vendorName
        self.contactName = contactName
        self.phoneNumber = phoneNumber
        self.email = email
        self.address = address

class PurchaseOrder:
    
    def __init__(self):
        self.NumberPO = NumberPO
        self.vendorID = vendorID
        self.dateCreated = dateCreated
        self.itemsOrdered = itemsOrdered
        self.totalCost = totalCost
        self.status = status