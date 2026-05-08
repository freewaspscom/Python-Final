from models import Product
from models import Vendor
from models import PurchaseOrder
from inventory_manager import *
from lists import Lists





while True:
    print("Temp nhtr")
    print("1. Add a product\n2. View All Products\n3. Search for products\n4. Edit a product\n5. deactivate a product\n6. Display low-stock products\n7. Exit")
    selection = input(">")
    if selection == "1":
        newProduct = addProduct()
        productsList.append(newProduct)
    