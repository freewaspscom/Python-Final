def fullReport(listGroup):
    for i in range(len(listGroup.products)):
        print(f"Name: {listGroup.products[i].name}")
        print(f"Category: {listGroup.products[i].category}")
        print(f"Quantity: {listGroup.products[i].quantity}")
        print(f"Price: ${listGroup.products[i].unitPrice}")
        print("-----------------")
    print("Would you like to save this report? (y/N)")
    selection = input("> ")
    if selection.lower() == "y":
            with open("full_report.txt", "w") as f:
                for i in range(len(listGroup.products)):
                    f.write(f"Name: {listGroup.products[i].name}\n")
                    f.write(f"Category: {listGroup.products[i].category}\n")
                    f.write(f"Quantity: {listGroup.products[i].quantity}\n")
                    f.write(f"Price: ${listGroup.products[i].unitPrice}\n")
                    f.write("-----------------\n")


def lowStockReport(listGroup, lowStock):
    for i in range(len(listGroup.products)):
        if listGroup.products[i].quantity <= lowStock:
            print(f"Name: {listGroup.products[i].name}")
            print(f"Category: {listGroup.products[i].category}")
            print(f"Quantity: {listGroup.products[i].quantity}")
            print(f"Price: ${listGroup.products[i].unitPrice}")
            print("-----------------")
    print("Would you like to save this report? (y/N)")
    selection = input("> ")
    if selection.lower() == "y":
            with open("low_stock_report.txt", "w") as f:
                for i in range(len(listGroup.products)):
                    if listGroup.products[i].quantity <= lowStock:
                        f.write(f"Name: {listGroup.products[i].name}\n")
                        f.write(f"Category: {listGroup.products[i].category}\n")
                        f.write(f"Quantity: {listGroup.products[i].quantity}\n")
                        f.write(f"Price: ${listGroup.products[i].unitPrice}\n")
                        f.write("-----------------\n")

def totalInventoryValue(listGroup):
    total = 0
    for i in range(len(listGroup.products)):
        combined = listGroup.products[i].quantity * listGroup.products[i].unitPrice
        total += combined
    print(f"Total worth of current stock: ${total}")
    print("Would you like to save this report? (y/N)")
    selection = input("> ")
    if selection.lower() == "y":
        with open("total_inventory_value.txt", "w") as f:
            f.write(f"Total worth of current stock: ${total}")