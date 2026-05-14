def fullReport(listGroup):
    for i in range(len(listGroup.products)):
        print(f"Name: {listGroup.products[i].name}")
        print(f"Category: {listGroup.products[i].category}")
        print(f"Quantity: {listGroup.products[i].quantity}")
        print(f"Price: ${listGroup.products[i].unitPrice}")

def lowStockReport(listGroup, lowStock):
    for i in range(len(listGroup.products)):
        if listGroup.products[i].quantity <= lowStock:
            print(f"Name: {listGroup.products[i].name}")
            print(f"Category: {listGroup.products[i].category}")
            print(f"Quantity: {listGroup.products[i].quantity}")
            print(f"Price: ${listGroup.products[i].unitPrice}")

def totalInventoryValue(listGroup):
    total = 0
    for i in range(len(listGroup.products)):
        combined = listGroup.products[i].quantity * listGroup.products[i].unitPrice
        total += combined
    print(f"Total worth of current stock: ${total}")