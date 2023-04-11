import tkinter as tk
from tkinter import ttk
 #This is the code to create a calculator in tkinter
root=tk.Tk()
root.title("Calculator")
entryvar=tk.IntVar()
#data

entry=ttk.Entry(root)
def on_click(digit):
    entry.insert("end",digit)
def add():
    num1=entry.get()
    num1=int(num1)
    global fnum
    fnum=num1
    entry.delete(0,"end")
    global button_click
    button_click=0
def subtract():
    num1=entry.get()
    num1=int(num1)
    global fnum
    fnum=num1
    entry.delete(0,"end")
    global button_click
    button_click=1

def multiply():
    num1=entry.get()
    num1=int(num1)
    global fnum
    fnum=num1
    entry.delete(0,"end")
    global button_click
    button_click=2

def divide():
    num1=entry.get()
    num1=int(num1)
    global fnum
    fnum=num1
    entry.delete(0,"end")
    global button_click
    button_click=3

def equals():
    num2=entry.get()
    num2=int(num2)
    if button_click==0:
        num3=int(num2+fnum)
    elif button_click==1:
        num3=int(fnum-num2)
    elif button_click==2:
        num3=int(fnum*num2)
    elif button_click==3:
        num3=float(fnum/num2)
    entry.delete(0,"end")
    entry.insert("end",num3)

def clear():
    entry.delete(0,"end")

def cross():
    entry.delete(0)
button0=tk.Button(root,text="0",borderwidth=2,command=lambda:on_click(0))
button1=tk.Button(root,text="1",borderwidth=2,command=lambda:on_click(1))
button2=tk.Button(root,text="2",borderwidth=2,command=lambda:on_click(2))
button3=tk.Button(root,text="3",borderwidth=2,command=lambda:on_click(3))
button4=tk.Button(root,text="4",borderwidth=2,command=lambda:on_click(4))
button5=tk.Button(root,text="5",borderwidth=2,command=lambda:on_click(5))
button6=tk.Button(root,text="6",borderwidth=2,command=lambda:on_click(6))
button7=tk.Button(root,text="7",borderwidth=2,command=lambda:on_click(7))
button8=tk.Button(root,text="8",borderwidth=2,command=lambda:on_click(8))
button9=tk.Button(root,text="9",borderwidth=2,command=lambda:on_click(9))
buttonplus=tk.Button(root,text="+",borderwidth=2,command=add)
buttonminus=tk.Button(root,text="-",borderwidth=2,command=subtract)
buttonequals=tk.Button(root, text="=",command=equals)
buttonclear=tk.Button(root,text="clear",borderwidth=2,command=clear)
buttonmultiply=tk.Button(root,text="*",borderwidth=2,command=multiply)
buttondivide=tk.Button(root, text="%",borderwidth=2,command=divide)
buttoncross=tk.Button(root, text="x",command=cross)
#layout
entry.grid(row=1,column=1,columnspan=10)
button0.grid(row=2,column=2)
button1.grid(row=2,column=3)
button2.grid(row=2,column=4)
button3.grid(row=2,column=5)

button4.grid(row=3,column=2)
button5.grid(row=3,column=3)
button6.grid(row=3,column=4)
button7.grid(row=3,column=5)

button8.grid(row=4,column=2)
button9.grid(row=4,column=3)
buttonplus.grid(row=4,column=4)
buttonminus.grid(row=4,column=5)

buttonclear.grid(row=6,column=1,columnspan=10)

buttonequals.grid(row=5,column=2)
buttonmultiply.grid(row=5,column=3)
buttondivide.grid(row=5,column=4)
buttoncross.grid(row=5,column=5)

root.mainloop()