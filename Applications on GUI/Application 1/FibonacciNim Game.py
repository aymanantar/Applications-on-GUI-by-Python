import time
from tkinter import *
from random import randint
main=Tk()
coins = randint(1, 50)
s=coins-1
main.title("Coins game")
flag=False
# checking the game status
def check (fp,s):
    global flag
    global p1
    global p2
    global coins
    global left
    coins -= fp
    # the case no coins left (game is over)
    if (not coins) : 
        left.pack_forget()
        end=Label(main,text=f"Congratulations ! {s} is the winner\n ")
        end.pack()        
        p2.pack_forget()
        p1=Button(command=exit,text="close the game")
        p1.pack()
        flag=True
    # case the still on
    else :
        left.pack_forget()        
        left=Label(main,text=f"The pile now has {coins} coins.\n")
        left.pack()
# checking if first player input was valid 
def v1 () :
    global m1
    global m2
    global temp
    global p2
    global p1
    global e
    global s
    n=e.get()
    #checking if the input was not an intger
    try :
            i = int(n)
    except :
            temp.pack_forget()        
            temp=Label(main,text="your number is not valid ")
            temp.pack()
            return
    #checking if the input was not in the valid range
    if (i not in range (1,s+1)):
        temp.pack_forget()        
        temp=Label(main,text="your number is not valid ")
        temp.pack()
        return         
    # if the input was valid then pass it to the game status checker and move to the second player 
    else :
        temp.pack_forget()                
        m1.pack_forget()
        check(i,"first player")
        if (flag): return        
        s=min(2*i,coins)                
        p1.pack_forget()
        p2.pack()
        m2=Label(main,text=f"second player to play, pick a number in range 1 , {min (2 * i, coins)} .\n")
        m2.pack()

# checking if second player input was valid         
def v2 () :
    global m1
    global m2
    global temp
    global p2
    global p1    
    global e    
    global s   
    n=e.get()
    #checking if the input was not an intger
    
    try :
            i = int(n)
    except :
            temp.pack_forget()        
            temp=Label(main,text="your number is not valid, ")
            temp.pack()
            return
    #checking if the input was not in the valid range    
    if ( i not in range (1, s+1 )):
        temp.pack_forget()        
        temp=Label(main,text="your number is not valid, ")
        temp.pack()
        return         
    # if the input was valid then pass it to the game status checker and move to the first player    
    else :
        temp.pack_forget()                
        m2.pack_forget()
        check(i,"second player")
        if (flag): return        
        s=min(coins,2*i)
        p2.pack_forget()
        p1.pack()
        m1=Label(main,text=f"first player to play, pick a number in range 1 , {min (2 * i, coins)} .\n")
        m1.pack()


# Starting the game
e=Entry(main)
e.pack()
left=Label(main,text=f"The pile has {coins} coins.\n")
left.pack()   
p1=Button(main,command=v1,text="enter")
p2=Button(main,command=v2,text="enter")
p1.pack()
m1=Label(main,text=f"first player, pick a number in range 1 , {coins - 1 } .\n")
m1.pack()
#only for declaration
temp=Label(main)    
m2=Label(main) 
            
    

main.mainloop()