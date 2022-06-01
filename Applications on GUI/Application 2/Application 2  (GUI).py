from tkinter import *
import openpyxl 

# Access to excel sheet
book = openpyxl.load_workbook("D:\\ME71\\2.Second Term\\Dr. Mohamed Elramly\\Assignment\\Countries.xlsx")
sheet1 = book["Egypt"]
sheet2 = book["US"]
sheet3 = book["Turkey"]
sheet4 = book["Italy"]
sheet5 = book["Morocco"]

# Delete option buttons when selected
def clear_main(): 
    myButton1.destroy()
    myButton2.destroy()

# Delete country buttons when selected
def clear_country(x):
    if x == 1:
        button1_max.destroy()
        button2_max.destroy()
        button3_max.destroy()
        button4_max.destroy()
        button5_max.destroy()
    elif x == 2 :
        button1.destroy()
        button2.destroy()
        button3.destroy()
        button4.destroy()
        button5.destroy()


# Canvas form which output information appear
def canvas_menu(exp):
    global canvas, scrollbar
    scrollbar = Scrollbar(gui)
    scrollbar.config() # 1060 480 304
    scrollbar.place(x=1060,y=160, height=504)# side=RIGHT,fill=Y  x=1060,y=600 x=1060,y=160, height=504, width=800
    canvas = Canvas(
            gui,
            height=500,  # 300 800
            width=800,
            background="#E1E3E6", # #160E2C
            yscrollcommand=scrollbar.set
        )   #   0.2 0.6 00
    canvas.place(relx=0.2, rely=0.2, y=00)
    canvas.create_text(100, 50, fill="#000000", font="Helvetica 20 bold", text=exp)
    canvas.configure(scrollregion=canvas.bbox("all"))
    scrollbar.config(command=canvas.yview)

# Check if option button is selected then delete the canvas form
i=0
def canvas_found(i):
    if i >= 1 or i < 0:
        canvas.destroy()
        scrollbar.destroy()

# Display Stat and Population of country
def egypt():
    global i
    clear_country(2)
    exp = "Egypt:\n\n\t"
    cells = sheet1["A1" : "B128"]
    for c1, c2 in cells:
        exp += "{0:8} {1:8}".format(c1.value,c2.value) + "\n\t"
    canvas_menu(exp)
    i = 2
    return exp

def turkey():
    global i
    clear_country(2)
    exp = "Turkey:\n\n\t"
    cells = sheet3["A1" : "B198"]
    for c1, c2 in cells:
        exp += "{0:8} {1:8}".format(c1.value,c2.value) + "\n\t"
    canvas_menu(exp)
    i = 2
    return exp

def usa():
    global i
    clear_country(2)
    exp = "USA:\n\n\t"
    cells = sheet2["A1" : "B170"]
    for c1, c2 in cells:
        exp += "{0:8} {1:8}".format(c1.value,c2.value) + "\n\t"
    canvas_menu(exp)
    i = 2
    return exp

def italy():
    global i
    clear_country(2)
    exp = "Italy:\n\n\t"
    cells = sheet4["A1" : "B160"]
    for c1, c2 in cells:
        exp += "{0:8} {1:8}".format(c1.value,c2.value) + "\n\t"
    canvas_menu(exp)
    i = 2
    return exp

def morocco():
    global i
    clear_country(2)
    exp = "Morocco:\n\n\t"
    cells = sheet5["A1" : "B87"]
    for c1, c2 in cells:
        exp += "{0:8} {1:8}".format(c1.value,c2.value) + "\n\t"
    canvas_menu(exp)
    i = 2
    return exp

# Buttons for each country to show stat and population
def button_display1():
    global myButton1, myButton2
    global button1,button2,button3,button4,button5
    clear_main()

    text_menu.destroy()
    text_menu2 = Label(gui, text="Choose a country ")
    text_menu2.config(font=("Times New Roman",45,"bold"))
    text_menu2.config(bg="#447498",fg="#F5F5F5")
    text_menu2.place(x=438,y=0)


    button1 = Button(gui, text = "Egypt", height=1, width=12, command = egypt)
    button1.config(font=("Times New Roman",22,"bold"))
    button1.config(bg="#E1E3E6", fg="#000000")
    button1.place(x=550,y=150) #180 150
    

    button2 = Button(gui, text = "USA",height=1, width=12,command = usa)
    button2.config(font=("Times New Roman",22,"bold"))
    button2.config(bg="#E1DEA3", fg="#000000") # #C9C68D  #7DD7DA
    button2.place(x=550,y=250) #380 150


    button3 = Button(gui, text = "Turkey",height=1, width=12,command = turkey)
    button3.config(font=("Times New Roman",22,"bold"))
    button3.config(bg="#E1E3E6", fg="#000000")
    button3.place(x=550,y=350) # 580 150

    button4 = Button(gui, text = "Italy",height=1, width=12,command = italy)
    button4.config(font=("Times New Roman",22,"bold"))
    button4.config(bg="#E1DEA3", fg="#000000") # #D6D39B
    button4.place(x=550,y=450)# 780 150

    button5 = Button(gui, text = "Morocco",height=1, width=12,command = morocco)
    button5.config(font=("Times New Roman",22,"bold"))
    button5.config(bg="#E1E3E6", fg="#000000")
    button5.place(x=550,y=550) # 980 150


# Display Max and Min population in country
def egypt_max():
    global i
    clear_country(1)
    max_pop = 0
    min_pop = 10000000000
    exp = ""
    cells = sheet1["A1" : "B128"]
    for c1, c2 in cells:
        if max_pop < int(c2.value):
            max_pop = int(c2.value)
            max_city = c1.value
        if min_pop > int(c2.value):
            min_pop = int(c2.value)
            min_city = c1.value 
    exp = f"Egypt \n\nMaximum value >>> \t {max_city} : \t{max_pop}" + "\n\n" + f"Minimum value >>> \t {min_city}: {min_pop}" + "\n"
   
    i = 1
    canvas_menu(exp)
    return exp 

def usa_max():
    global i
    clear_country(1)
    max_pop = 0
    min_pop = 10000000000
    exp = ""
    cells = sheet2["A1" : "B170"]
    for c1, c2 in cells:
        if max_pop < int(c2.value):
            max_pop = int(c2.value)
            max_city = c1.value
        if min_pop > int(c2.value):
            min_pop = int(c2.value)
            min_city = c1.value 
    exp = f"USA \n\nMaximum value >>> \t {max_city} : {max_pop}" + "\n\n" + f"Minimum value >>> \t {min_city}: {min_pop}" + "\n" 
    i = 1
    canvas_menu(exp)
    return exp 

def turkey_max():
    global i
    clear_country(1)
    max_pop = 0
    min_pop = 10000000000
    exp = ""
    cells = sheet3["A1" : "B198"]
    for c1, c2 in cells:
        if max_pop < int(c2.value):
            max_pop = int(c2.value)
            max_city = c1.value
        if min_pop > int(c2.value):
            min_pop = int(c2.value)
            min_city = c1.value 
    exp = f"Turkey \n\nMaximum value >>> \t {max_city} : {max_pop}" + "\n\n" + f"Minimum value >>> \t {min_city}: {min_pop}" + "\n"
    i = 1
    canvas_menu(exp)
    return exp 

def italy_max():
    global i
    clear_country(1)
    max_pop = 0
    min_pop = 10000000000
    exp = ""
    cells = sheet4["A1" : "B160"]
    for c1, c2 in cells:
        if max_pop < int(c2.value):
            max_pop = int(c2.value)
            max_city = c1.value
        if min_pop > int(c2.value):
            min_pop = int(c2.value)
            min_city = c1.value 
    exp = f"Italy \n\nMaximum value >>> \t {max_city} : {max_pop}" + "\n\n" + f"Minimum value >>> \t {min_city}: {min_pop}" + "\n"
    i = 1
    canvas_menu(exp)
    return exp 

def morocco_max():
    global i
    clear_country(1) 
    max_pop = 0
    min_pop = 10000000000
    exp = ""
    cells = sheet5["A1" : "B87"]
    for c1, c2 in cells:
        if max_pop < int(c2.value):
            max_pop = int(c2.value)
            max_city = c1.value
        if min_pop > int(c2.value):
            min_pop = int(c2.value)
            min_city = c1.value 
    exp = f"Morocco \n\nMaximum value >>> \t {max_city} : {max_pop}" + "\n\n" + f"Minimum value >>> \t {min_city}: {min_pop}" + "\n"
    i = 1
    canvas_menu(exp)
    return exp 

# Buttons for each country to show max and min population
def button_display2():
    global myButton1, myButton2 
    global button1_max,button2_max,button3_max,button4_max,button5_max

    clear_main()
       
    text_menu.destroy()
    text_menu2 = Label(gui, text="Choose a country ")
    text_menu2.config(font=("Times New Roman",45,"bold"))
    text_menu2.config(bg="#447498",fg="#F5F5F5")
    text_menu2.place(x=438,y=0)

    button1_max = Button(gui, text = "Egypt", height=1, width=12, command = egypt_max) # 1 6
    button1_max.config(font=("Times New Roman",22,"bold"))
    button1_max.config(bg="#E1E3E6", fg="#000000")
    button1_max.place(x=550,y=150) #100 0

    button2_max = Button(gui, text = "USA",height=1, width=12,command = usa_max)
    button2_max.config(font=("Times New Roman",22,"bold"))
    button2_max.config(bg="#E1DEA3", fg="#000000")
    button2_max.place(x=550,y=250) #300 0

    button3_max = Button(gui, text = "Turkey",height=1, width=12,command = turkey_max)
    button3_max.config(font=("Times New Roman",22,"bold"))
    button3_max.config(bg="#E1E3E6", fg="#000000")
    button3_max.place(x=550,y=350) # 500 0

    button4_max = Button(gui, text = "Italy",height=1, width=12,command = italy_max)
    button4_max.config(font=("Times New Roman",22,"bold"))
    button4_max.config(bg="#E1DEA3", fg="#000000")
    button4_max.place(x=550,y=450)# 700 0

    button5_max = Button(gui, text = "Morocco",height=1, width=12,command = morocco_max)
    button5_max.config(font=("Times New Roman",22,"bold"))
    button5_max.config(bg="#E1E3E6", fg="#000000")
    button5_max.place(x=550,y=550) # 900 0
 
# Format of application
gui = Tk()
gui.title("Application 0 GUI")
gui.geometry("1280x800") 
gui.config(bg="#447498")  ## Color of background

# Button that returns back to option form
def option_button():
    
    canvas_found(i)
    clear_country(i)

    myButton3 = Button(gui, text = "Options",height=1,width=5, command = main)
    myButton3.config(bg="#000000", fg = "#FFFFFF")  ### Color of background option button and Font
    myButton3.config(font=("Ink Free",12,"bold"))
    myButton3.place(x=0,y=30)

# Exit button
def close_button():

    myButton4 = Button(gui, text = "Exit",height=1,width=5, command = gui.quit)
    myButton4.config(bg="#000000", fg = "#FFFFFF") ### Color of background exit button and Font
    myButton4.config(font=("Ink Free",12,"bold"))
    myButton4.place(x=0,y=0)

# Choose an option form
def main():
    global myButton1, myButton2, text_menu

    start_button.destroy()
    text_start1.destroy()
    text_start.destroy()
    
    text_menu = Label(gui, text="Choose an option ")
    text_menu.config(font=("Times New Roman",45,"bold"))
    text_menu.config(bg="#447498",fg="white") 
    text_menu.place(x=430,y=0)


    option_button()

    myButton1 = Button(gui, text="  Display State and Population.",height=3, width=34, command = button_display1) # 22 32 33
    myButton1.config(bg="#E1E3E6", fg = "#000000")
    myButton1.config(font=("Times New Roman",20,"bold"))
    myButton1.grid(row=0,column=1,padx=10,pady=200)

    myButton2 = Button(gui, text = "   Display Max and Min Population.",height=3, width=34, command = button_display2)
    myButton2.config(bg="#E1E3E6", fg = "#000000")
    myButton2.config(font=("Times New Roman",20,"bold"))
    myButton2.grid(row=0,column=2,padx=145,pady=50)

# Start form of application
def start_menu():
    global start_button, text_start, text_start1

    text_start = Label(gui, text="Application 0 ")
    text_start.config(font=("Times New Roman",40,"bold"))
    text_start.config(bg="#447498",fg="#F5F5F5")
    text_start.place(x=500,y=0)

    text_start1 = Label(gui, text="\n Maya \n Ayman \n Mohamed ")
    text_start1.config(font=("Ink free",40,"bold"))
    text_start1.config(bg="#447498",fg="#F5F5F5")
    text_start1.place(x=1030,y=520)


    start_button = Button(gui, text="Click Here to Start!",height=3, width=30, command = main)
    start_button.config(font=("Times New Roman",30,"bold","italic"))
    start_button.config(bg="#E1E3E6", fg = "#000000") # #676767    #FFFFFF #C6CFD6
    start_button.grid(row=1,column=1,padx=290,pady=250)
    close_button()

start_menu()
gui.mainloop()

