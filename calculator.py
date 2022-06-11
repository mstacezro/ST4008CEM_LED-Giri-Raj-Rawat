'''
A simple calculator is made importing tkinter module in python
'''

#import tkintr


from tkinter import*



#object name for the tkinter project
root=Tk()


#name/title of the project
root.title("CALCULATOR")


#dimension of calculator
root.geometry("465x400")
root.resizable(0,0)     #nonresizable, for resizable (True,True)
root.configure(bg="grey")


#icon of calculator
##NOTE:  win.iconbitmap("personlog.ico") doesnot work in ubuntu
from PIL import Image, ImageTk
logo = ImageTk.PhotoImage(file='/home/mstacezro/Documents/SOFTWARICA/Programming and Algorithms--Giri Raj Rawat/CODES/twaake-nter/calculator/cal_icon.png')
root.tk.call('wm', 'iconphoto', root._w, logo)


#defining a string variable 
scvalue=StringVar()
scvalue.set("") #setting initial value of string variable as blank


#entry box for calculation
screen=Entry(root, textvar=scvalue,font="arial 30 bold")
screen.grid(row=0,column=0,columnspan=4,padx=10,pady=10)


#calculation functions define
def click(event):       #inputing numbers as in buttons in display
    global scvalue      #global value can be modified inside this function
    text=event.widget.cget("text")      #event.widget gives the button which is clicked and cget gives me texts from a widget
    print(text)
    
    #defining conditions for operations
   
    if text=="=":
        if scvalue.get().isdigit():    #this if condition changes digits in scvalue into integers
            value=int(scvalue.get())
        else:       #if not digit, 
           
            try:
                value=eval(screen.get())    #eval evaluates string
            except Exception as e:
                    value="ERROR"

        scvalue.set(value)              #set value to scvalue
        screen.update()
    elif text=="C":             
        """when clear button is pressed,clears the text input area"""
        scvalue.set("")         #sets scvalue to blank
        screen.update
    else:
        scvalue.set(scvalue.get()+text)   #modifying scvalue with text inputed
        screen.update                   #updates screen value with new scvalue    




#define number buttons for input
button_1=Button(root, text="1",padx=40,pady=20,bg="gray67")
button_2=Button(root, text="2",padx=42,pady=20,bg="gray67")
button_3=Button(root, text="3",padx=42,pady=20,bg="gray67")
button_4=Button(root, text="4",padx=40,pady=20,bg="gray67")
button_5=Button(root, text="5",padx=42,pady=20,bg="gray67")
button_6=Button(root, text="6",padx=42,pady=20,bg="gray67")
button_7=Button(root, text="7",padx=40,pady=20,bg="gray67")
button_8=Button(root, text="8",padx=42,pady=20,bg="gray67")
button_9=Button(root, text="9",padx=42,pady=20,bg="gray67")
button_0=Button(root, text="0",padx=40,pady=20,bg="gray67")
button_dot=Button(root, text=".",padx=44,pady=20,bg="gray67")


#define operation button for input
button_clear=Button(root, text="C",padx=30,pady=6,bg="red",fg="black",font="arial 30 bold")
button_power=Button(root, text="**",padx=39,pady=20,bg="yellow")
button_modulo=Button(root, text="%",padx=40,pady=20,bg="yellow")
button_divide=Button(root, text="/",padx=44,pady=20,bg="yellow")
button_multiply=Button(root, text="*",padx=42,pady=20,bg="yellow")
button_minus=Button(root, text="-",padx=43,pady=20,bg="yellow")
button_add=Button(root, text="+",padx=40,pady=20,bg="yellow")
button_equal=Button(root, text="=",padx=100,pady=20, bg="green",fg="white")

#display buttons on screen
#first row
button_clear.grid(row=1,column=0)
button_power.grid(row=1,column=1)
button_modulo.grid(row=1,column=2)
button_divide.grid(row=1,column=3)

#second row
button_7.grid(row=2,column=0)
button_8.grid(row=2,column=1)
button_9.grid(row=2,column=2)
button_multiply.grid(row=2,column=3)

#third row
button_4.grid(row=3,column=0)
button_5.grid(row=3,column=1)
button_6.grid(row=3,column=2)
button_minus.grid(row=3,column=3)

#fourth row
button_1.grid(row=4,column=0)
button_2.grid(row=4,column=1)
button_3.grid(row=4,column=2)
button_add.grid(row=4,column=3)

#fifth row
button_0.grid(row=5,column=0)
button_dot.grid(row=5,column=1)
button_equal.grid(row=5,column=2,columnspan=2)

#Events can be key presses or mouse operations by the user using bind syntax to the left-mouse click button
button_1.bind("<Button-1>",click)
button_2.bind("<Button-1>",click)
button_3.bind("<Button-1>",click)
button_4.bind("<Button-1>",click)
button_5.bind("<Button-1>",click)
button_6.bind("<Button-1>",click)
button_7.bind("<Button-1>",click)
button_8.bind("<Button-1>",click)
button_9.bind("<Button-1>",click)
button_0.bind("<Button-1>",click)
button_dot.bind("<Button-1>",click)

button_clear.bind("<Button-1>",click)
button_power.bind("<Button-1>",click)
button_modulo.bind("<Button-1>",click)
button_divide.bind("<Button-1>",click)
button_multiply.bind("<Button-1>",click)
button_minus.bind("<Button-1>",click)
button_minus.bind("<Button-1>",click)
button_add.bind("<Button-1>",click)
button_equal.bind("<Button-1>",click)


#running the project till it is closed
root.mainloop()