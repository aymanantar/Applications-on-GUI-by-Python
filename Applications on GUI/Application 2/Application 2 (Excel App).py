import openpyxl

# Access to the excel file
book = openpyxl.load_workbook("D:\\ME71\\2.Second Term\\Dr. Mohamed Elramly\\Assignment\\Countries.xlsx")

# Access to each excel sheet
sheet1 = book["Egypt"]
sheet2 = book["US"]
sheet3 = book["Turkey"]
sheet4 = book["Italy"]
sheet5 = book["Morocco"]

#Get State and population of each country
def population_stated():
    print(lst_countries)
    name_country = input("Choose country from the list: ")

    if name_country.title() == "Egypt":
        cells = sheet1["A1":"B128"]
        for c1, c2 in cells:
            print("{0:8} {1:8}".format(c1.value, c2.value))
        rows1 = sheet1.rows
        values1 = [] # List that has all the population in one country
        for row in rows1:
            for cell in row:
                check = str(cell.value)
                check1 = check[:len(check) - 2]
                if check1.isnumeric():
                    values1.append(cell.value)
        print("Total population in the country: {0}".format(sum(values1)))

    elif name_country.upper() == "USA":
        cells = sheet2["A1":"B170"]
        for c1, c2 in cells:
            print("{0:8} {1:8}".format(c1.value, c2.value))
        rows2 = sheet2.rows
        values2 = []
        for row in rows2:
            for cell in row:
                check = str(cell.value)
                check1 = check[:len(check) - 2]
                if check1.isnumeric():
                    values2.append(cell.value)
        print("Total population in the country: {0}".format(sum(values2)))

    elif name_country.title() == "Turkey":
        cells = sheet3["A1":"B198"]
        for c1, c2 in cells:
            print("{0:8} {1:8}".format(c1.value, c2.value))
        rows3 = sheet3.rows
        values3 = []
        for row in rows3:
            for cell in row:
                check = str(cell.value)
                check1 = check[:len(check) - 2]
                if check1.isnumeric():
                    values3.append(cell.value)
        print("Total population in the country: {0}".format(sum(values3)))

    elif name_country.title() == "Italy":
        cells = sheet4["A1":"B160"]
        for c1, c2 in cells:
            print("{0:8} {1:8}".format(c1.value, c2.value))
        rows4 = sheet4.rows
        values4 = []
        for row in rows4:
            for cell in row:
                check = str(cell.value)
                check1 = check[:len(check) - 2]
                if check1.isnumeric():
                    values4.append(cell.value)
        print("Total population in the country: {0}".format(sum(values4)))

    elif name_country.title() == "Morocco":
        cells = sheet5["A1":"B87"]
        for c1, c2 in cells:
            print("{0:8} {1:8}".format(c1.value, c2.value))
        rows5 = sheet5.rows
        values5 = []
        for row in rows5:
            for cell in row:
                check = str(cell.value)
                check1 = check[:len(check) - 2]
                if check1.isnumeric():
                    values5.append(cell.value)
        print("Total population in the country: {0}".format(sum(values5)))

# Get maximum and minimum population of each country
def max_min():
    print(lst_countries)
    name_country = input("Choose country from the list: ")
    
    if name_country.title() == "Egypt":
        rows = sheet1.rows
        values = []
        for row in rows:
            for cell in row:
                check = str(cell.value)
                check1 = check[:len(check) -2]
                if check1.isnumeric():
                    values.append(cell.value)
        print("Minimum value: {0}".format(min(values)))
        print("Maximum value: {0}".format(max(values)))

    elif name_country.upper() == "USA":
        rows = sheet2.rows
        values = []
        for row in rows:
            for cell in row:
                check = str(cell.value)
                check1 = check[:len(check) - 2]
                if check1.isnumeric():
                    values.append(cell.value)
        print("Minimum value: {0}".format(min(values)))
        print("Maximum value: {0}".format(max(values)))

    elif name_country.title() == "Turkey":
        rows = sheet3.rows
        values = []
        for row in rows:
            for cell in row:
                check = str(cell.value)
                check1 = check[:len(check) - 2]
                if check1.isnumeric():
                    values.append(cell.value)
        print("Minimum value: {0}".format(min(values)))
        print("Maximum value: {0}".format(max(values)))

    elif name_country.title() == "Italy":
        rows = sheet4.rows
        values = []
        for row in rows:
            for cell in row:
                check = str(cell.value)
                check1 = check[:len(check) - 2]
                if check1.isnumeric():
                    values.append(cell.value)
        print("Minimum value: {0}".format(min(values)))
        print("Maximum value: {0}".format(max(values)))

    elif name_country.title() == "Morocco":
        rows = sheet5.rows
        values = []
        for row in rows:
            for cell in row:
                check = str(cell.value)
                check1 = check[:len(check) - 2]
                if check1.isnumeric():
                    values.append(cell.value)
        print("Minimum value: {0}".format(min(values)))
        print("Maximum value: {0}".format(max(values)))

# Choose options of application 
while True:
    print("\n Options: \n\t 1.Display the state, its population, and the total population in the country.\n\t 2.Display Max or Min Population. \n\t 3.Quit")
    choice = int(input("\nChoose number from the previous choices: "))
    lst_countries = ["Egypt", "USA", "Morocco", "Turkey", "Italy"]
    if choice == 2:
        max_min()
    elif choice == 1:
        population_stated()
    elif choice == 3:
        break