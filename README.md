# Product Management System 
This program allows for the tracking of products, vendors, and shipment orders.
This program features:
- Adding products
- Searching by name
- Searching for category
- Sorting by category
- Removing products
- Displaying low-stock products
- Adding vendors
- Searching for vendors
- Removing vendors
- Sorting by vendor name
- Creating orders
- Viewing orders
- Marking orders as received
- Sorting by cost
- Generating a full report
- Generating a low-stock report
- Generating a total inventory value report
- Save to JSON
- Load from JSON

It contains the files:
- main.py
- file_manager.py
- inventory_manager.py
- models.py
- lists.py
- reports.py
- orders.json
- products.json
- vendors.json
- code_explanation.txt
- README.md
- reflection.md

The program contains a master list of all submenus. Once a submenu is entered, the program will stay on that submenu until the user quits out.
All products, vendors, and orders are stored as objects, and their data is stored as attributes. Those objects are then stored in an array.
The program asks the user if they would like to generate a text file of their report. If they say yes, the program takes what was output to the console and puts it into a text file.

Jaden Yoder, IT-070
