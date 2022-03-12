from tkinter import *

BORDER_WIDTH = 0
ACTIVE_COLOR ="#EC670B"
BUTTON_COLOR = "#DEECF0"

root = Tk()
root.geometry("280x400")
root.resizable(0,0)
root.title("Simple Calculator")
frame1 = Frame(root, bg=BUTTON_COLOR, height=50)
frame1.pack(expand=True, fill="both")
frame2 = Frame(root, bg="white", height=350)
frame2.pack(expand=True, fill="both")
entry = Entry(frame1, justify="right", font=("Arial", 18, "italic"), bd=4)
entry.place(relheight=0.9, relwidth=0.9, rely=0.05, relx=0.05)

def button_add_click():
    initial_num = entry.get()
    global first_number
    global calc
    calc = "add"
    first_number = float(initial_num)
    entry.delete(0, END)

def button_sub_click():
    initial_num = entry.get()
    global first_number
    global calc
    calc = "sub"
    first_number = initial_num
    entry.delete(0, END)

def button_mul_click():
    initial_num = entry.get()
    global first_number
    global calc
    calc = "mul"
    first_number = initial_num
    entry.delete(0, END)

def button_div_click():
    initial_num = entry.get()
    global first_number
    global calc
    calc = "div"
    first_number = initial_num
    entry.delete(0, END)

def button_equal_click():
    second_number = entry.get()
    entry.delete(0, END)
    
    if calc == "add":
        ans = float(first_number) + float(second_number)
        ans_convert = int(ans)
        answer = ans == ans_convert
        if answer == True:
            entry.insert(0, ans_convert)
        else:
            entry.insert(0, ans)
    if calc == "sub":
        ans = float(first_number) - float(second_number)
        ans_convert = int(ans)
        answer = ans == ans_convert
        if answer == True:
            entry.insert(0, ans_convert)
        else:
            entry.insert(0, ans)
    if calc == "mul":
        ans = float(first_number) * float(second_number)
        ans_convert = int(ans)
        answer = ans == ans_convert
        if answer == True:
            entry.insert(0, ans_convert)
        else:
            entry.insert(0, ans)
    if calc == "div":
        ans = float(first_number) / float(second_number)
        ans_convert = int(ans)
        answer = ans == ans_convert
        if answer == True:
            entry.insert(0, ans_convert)
        else:
            entry.insert(0, ans)
  
def button_num_click(value):
    initial_num = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(initial_num) + str(value))

def button_clear_click():
    entry.delete(0, END)

def button_back_click():
    entry.delete(entry.index(END)-1)
        
    

clear_button = Button(frame2, text="Clear", bg=BUTTON_COLOR, fg="black", activebackground=ACTIVE_COLOR, 
                      font=("Arial", 20, "italic"), borderwidth=BORDER_WIDTH, command=button_clear_click)
clear_button.place(relheight=0.2, relwidth=0.375)

back_button = Button(frame2, text="Back", bg=BUTTON_COLOR, fg="black", activebackground=ACTIVE_COLOR, 
                      font=("Arial", 20, "italic"), borderwidth=BORDER_WIDTH, command=button_back_click)
back_button.place(relheight=0.2, relwidth=0.375, relx=0.375)

div_button = Button(frame2, text="\u00F7", bg=BUTTON_COLOR, fg="black", activebackground=ACTIVE_COLOR, 
                      font=("Arial", 30, "italic"), borderwidth=BORDER_WIDTH, command=button_div_click)
div_button.place(relheight=0.2, relwidth=0.251, relx=0.75)

button_7 = Button(frame2, text="7", bg=BUTTON_COLOR, fg="black", activebackground=ACTIVE_COLOR, 
                      font=("Arial", 30, "bold italic"), borderwidth=BORDER_WIDTH, command=lambda: button_num_click(7))
button_7.place(relheight=0.2, relwidth=0.25, rely=0.2)

button_8 = Button(frame2, text="8", bg=BUTTON_COLOR, fg="black", activebackground=ACTIVE_COLOR, 
                      font=("Arial", 30, "bold italic"), borderwidth=BORDER_WIDTH, command=lambda: button_num_click(8))
button_8.place(relheight=0.2, relwidth=0.25, relx=0.25, rely=0.2)

button_9 = Button(frame2, text="9", bg=BUTTON_COLOR, fg="black", activebackground=ACTIVE_COLOR, 
                      font=("Arial", 30, "bold italic"), borderwidth=BORDER_WIDTH, command=lambda: button_num_click(9))
button_9.place(relheight=0.2, relwidth=0.25, relx=0.5, rely=0.2)

button_mul = Button(frame2, text="\u00D7", bg=BUTTON_COLOR, fg="black", activebackground=ACTIVE_COLOR, 
                      font=("Arial", 30, "italic"), borderwidth=BORDER_WIDTH, command=button_mul_click)
button_mul.place(relheight=0.2, relwidth=0.25, relx=0.75, rely=0.2)

button_4 = Button(frame2, text="4", bg=BUTTON_COLOR, fg="black", activebackground=ACTIVE_COLOR, 
                      font=("Arial", 30, "bold italic"), borderwidth=BORDER_WIDTH, command=lambda: button_num_click(4))
button_4.place(relheight=0.2, relwidth=0.25, rely=0.4)

button_5 = Button(frame2, text="5", bg=BUTTON_COLOR, fg="black", activebackground=ACTIVE_COLOR, 
                      font=("Arial", 30, "bold italic"), borderwidth=BORDER_WIDTH, command=lambda: button_num_click(5))
button_5.place(relheight=0.2, relwidth=0.25, relx=0.25, rely=0.4)

button_6 = Button(frame2, text="6", bg=BUTTON_COLOR, fg="black", activebackground=ACTIVE_COLOR, 
                      font=("Arial", 30, "bold italic"), borderwidth=BORDER_WIDTH, command=lambda: button_num_click(6))
button_6.place(relheight=0.2, relwidth=0.25, relx=0.5, rely=0.4)

button_sub = Button(frame2, text="-", bg=BUTTON_COLOR, fg="black", activebackground=ACTIVE_COLOR, 
                      font=("Arial", 30, "italic"), borderwidth=BORDER_WIDTH, command=button_sub_click)
button_sub.place(relheight=0.2, relwidth=0.25, relx=0.75, rely=0.4)

button_1 = Button(frame2, text="1", bg=BUTTON_COLOR, fg="black", activebackground=ACTIVE_COLOR, 
                      font=("Arial", 30, "bold italic"), borderwidth=BORDER_WIDTH, command=lambda: button_num_click(1))
button_1.place(relheight=0.2, relwidth=0.25, rely=0.6)

button_2 = Button(frame2, text="2", bg=BUTTON_COLOR, fg="black", activebackground=ACTIVE_COLOR, 
                      font=("Arial", 30, "bold italic"), borderwidth=BORDER_WIDTH, command=lambda: button_num_click(2))
button_2.place(relheight=0.2, relwidth=0.25, relx=0.25, rely=0.6)

button_3 = Button(frame2, text="3", bg=BUTTON_COLOR, fg="black", activebackground=ACTIVE_COLOR, 
                      font=("Arial", 30, "bold italic"), borderwidth=BORDER_WIDTH, command=lambda: button_num_click(3))
button_3.place(relheight=0.2, relwidth=0.25, relx=0.5, rely=0.6)

button_add = Button(frame2, text="+", bg=BUTTON_COLOR, fg="black", activebackground=ACTIVE_COLOR, 
                      font=("Arial", 30, "italic"), borderwidth=BORDER_WIDTH, command=button_add_click)
button_add.place(relheight=0.2, relwidth=0.25, relx=0.75, rely=0.6)

button_0 = Button(frame2, text="0", bg=BUTTON_COLOR, fg="black", activebackground=ACTIVE_COLOR, 
                      font=("Arial", 30, "bold italic"), borderwidth=BORDER_WIDTH, command=lambda: button_num_click(0))
button_0.place(relheight=0.2, relwidth=0.25, rely=0.8)

button_dot = Button(frame2, text=".", bg=BUTTON_COLOR, fg="black", activebackground=ACTIVE_COLOR, 
                      font=("Arial", 30, "bold italic"), borderwidth=BORDER_WIDTH, command=lambda: button_num_click("."))
button_dot.place(relheight=0.2, relwidth=0.25, relx=0.25, rely=0.8)

button_equal = Button(frame2, text="=", bg="#F5CE6C", fg="black", activebackground=ACTIVE_COLOR, 
                      font=("Arial", 30, "italic"), borderwidth=BORDER_WIDTH, command=button_equal_click)
button_equal.place(relheight=0.2, relwidth=0.5, relx=0.5, rely=0.8)


root.mainloop()

