import json
from datetime import datetime, date

#Starting prompts
print("\n---Expense Tracker---")

while True:
    #Menu section
    print("\n---Main Menu---")

    print("\nWhat do you want to do?")

    print("\n1. Add Expense")
    print("2. View all expenses")
    print("3. Delete expense")
    print("4. View summary")
    print("5. Exit\n")
    
    #Looping till valid Menu item selected
    while True:
        try:
            scan = int(input("Enter the number: "))
            if scan in range(1,6):
                break
            else:
                print("Enter numbers between 1 to 5 !")
        except ValueError:
            print("Enter a numerical value between 1 to 5")

    #Execution
    if scan == 1:

        l = []

        try:
            with open("expenses.json") as f:
                x = json.load(f)
                l = x
        #If file is empty
        except json.decoder.JSONDecodeError:
            print("First Entry !")
        #If file is not found
        except FileNotFoundError:
            print("Initializing file creation...")
        
        #Taking data:-
        
        #Automation of SNo.
        sno = 0
        try:
            for i in x:
                sno += 1
        except NameError:
            sno = 0
        
        #Taking valid amount value
        while True:
            amount = float(input("Enter amount: "))
            if amount <= 0:
                print("Enter a valid amount")
            elif amount == 0:
                print("What's the point of 0 ?!")
            else:
                break
        
        #Category selection
        print("\nChoose category: ")
        print("1.Food")
        print("2.Travel")
        print("3.Shopping")
        print("4.Other")
        print("5.Enter your own category\n") #Complicating the category handling for summary

        while True:
            
            #For valid category number input
            while True:
                try:
                    category_number = int(input("Enter category number: "))
                    break
                except ValueError:
                    print("Enter a Valid category number")
            
            if category_number == 1:
                category = "Food"
                break
            elif category_number == 2:
                category = "Travel"
                break
            elif category_number == 3:
                category = "Shopping"
                break
            elif category_number == 4:
                category = "Other"
                break
            elif category_number == 5:
                category = input("\nEnter category label: ")
                break
            else :
                print("Enter a number between 1 to 5")
        
        #Taking Info
        description = input("Enter description (Optinal): ")
        
        #Taking Date
        while True:
            Date = input("Enter date: ")
            if Date == "":
                Date = date.today().strftime("%d-%m-%Y")
                break
            else:
                try:
                    datetime.strptime(Date, "%d-%m-%Y")
                    break
                except ValueError:
                    print("Enter a valid date in formate 'DD-MM-YYYY'")

        #Strings to Structure
        data = {
                "SNo." : sno + 1,
                "Amount" : amount,
                "Category" : category,
                "Description" : description,
                "Date" : Date
            }

        #Storing it in the list
        l.append(data)

        #Passing the list into the json file
        with open("expenses.json", "w") as f:
            json.dump(l , f, indent = 4)

    #To read entire file
    if scan == 2:
        #Importing data and reading it from the file
        try:
            with open("expenses.json") as f:
                x = json.load(f)
                print(f"\nPrinting data:\n {x}") #Any way to make this pretty?
        #If file is empty
        except json.decoder.JSONDecodeError:
            print("No value is stored in the memory yet")
        #If file is not found
        except FileNotFoundError:
            print("No file has been initialized")

    #To delete entry(s)
    if scan == 3:
        try:
            with open("expenses.json") as f:
                x = json.load(f)
        #If file is empty
        except json.decoder.JSONDecodeError:
            print("No value is stored in the memory yet")
        #If file is not found
        except FileNotFoundError:
            print("No file has been initialized")

        target = int(input("Enter target: "))
        new_list = []

        for data in x:
            if target == int(data["SNo."]):
                continue
            else:
                new_list.append(data)
        
        with open("expenses.json", "w") as f:
            json.dump(new_list , f, indent = 4)

        #Printing appropriate prompt
        if new_list == x:
            print("Entered target is not present in the file")
        else:
            print("Deleted successfully")

    #To get Summary
    if scan == 4:
        #Checking file status
        try:
            with open("expenses.json") as f:
                x = json.load(f)

            #Initializing variables for Expense Handling
            total = 0
            total_amount = 0
            total_amount_now = 0

            for data in x:
                total += 1
                total_amount = total_amount + float(data["Amount"])
                if data["Date"] == datetime.today().strptime(data["Date"],"%d-%m-%Y") :
                    total_amount_now = total_amount_now + float(data["Amount"])

            #Fixing avg dividing by 0
            if total_amount == 0:
                avg = 0
            else:
                avg = total_amount/total

            print("\n=== Expense Summary ===\n")
            print(f"Total expenses tracked: {total}")
            print(f"Total Amount recorded: {total_amount}")
            print(f"Today's total spending: {total_amount_now}")
            print(f"Overall average spending: {avg}")
        
            print("\n--- Category wise Spending ---\n")

            #Initializing variables for category handling
            category_count_Food = 0
            category_total_Food = 0
            category_count_Travel = 0
            category_total_Travel = 0
            category_count_Shopping = 0
            category_total_Shopping = 0
            category_count_Other = 0
            category_total_Other = 0

            #Looping for automation of category handling
            for data in x:
            
                if data["Category"] == "Food":
                    category_count_Food =  category_count_Food + 1
                    category_total_Food = category_total_Food + data["Amount"]
                elif data["Category"] == "Travel":
                    category_count_Travel =  category_count_Travel + 1
                    category_total_Travel = category_total_Travel + data["Amount"]
                elif data["Category"] == "Shopping":
                    category_count_Shopping =  category_count_Shopping + 1
                    category_total_Shopping = category_total_Shopping + data["Amount"]
                else :
                    category_count_Other = category_count_Other + 1
                    category_total_Other = category_total_Other + data["Amount"]

            print(f"Total expenses tracked as Food: {category_count_Food}")
            print(f"Total spending on Food: {category_total_Food}")
            print(f"Total expenses tracked as Travel: {category_count_Travel}")
            print(f"Total spending on Travel: {category_total_Travel}")
            print(f"Total expenses tracked as Shopping: {category_count_Shopping}")
            print(f"Total spending on Shopping: {category_total_Shopping}")
            print(f"Total expenses tracked as Other: {category_count_Other}")
            print(f"Total spending on Other (including coustom categories): {category_total_Other}")

            print("\n=======================")

        #If file is empty
        except json.decoder.JSONDecodeError:
            print("No value is stored in the memory yet")
        #If file is not found
        except FileNotFoundError:
            print("No file has been initialized")
            
    #To end programe
    if scan == 5:
        print("\nEnd of the application !\n")
        break