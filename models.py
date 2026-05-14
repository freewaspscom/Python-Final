class Product:
    
    def __init__(self, productItems):
        self.productID = productItems[0]
        self.name = productItems[1]
        self.category = productItems[2]
        self.quantity = productItems[3]
        self.reorderLevel = productItems[4]
        self.reorderQuantity = productItems[5]
        self.unitPrice = productItems[6]
        self.vendorID = productItems[7]
        self.status = productItems[8]
    

    def convertToDictionary(self):
        storedProduct =     {
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
        return storedProduct






class Vendor:

    def __init__(self, vendorItems):
        self.vendorID = vendorItems[0]
        self.vendorName = vendorItems[1]
        self.contactName = vendorItems[2]
        self.phoneNumber = vendorItems[3]
        self.email = vendorItems[4]
        self.address =vendorItems[5]


    def convertToDictionary(self):
        storedVendor =     {
            "vendorID": self.vendorID,
            "vendorName": self.vendorName,
            "contactName": self.contactName,
            "phoneNumber": self.phoneNumber,
            "email": self.email,
            "address": self.address,
        }
        return storedVendor




class PurchaseOrder:
    
    def __init__(self, orderItems):
        self.numberPO = orderItems[0]
        self.vendorID = orderItems[1]
        self.dateCreated = orderItems[2]
        self.itemsOrdered = orderItems[3]
        self.quantityOrdered = orderItems[4]
        self.totalCost = orderItems[5]
        self.status = "Ordered"
    

    def convertToDictionary(self):
        storedVendor =     {
            "numberPO": self.numberPO,
            "vendorID": self.vendorID,
            "dateCreated": self.dateCreated,
            "itemsOrdered": self.itemsOrdered,
            "quantityOrdered": self.quantityOrdered,
            "totalCost": self.totalCost,
            "status": self.status,
        }
        return storedVendor