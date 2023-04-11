import tkinter as tk
from tkinter import ttk
""" #creating a window
root=tk.Tk()
#setting the title of our app
root.title("Some Dope app")
#setting the size of our tkinter window
#this method is not reccomended
tk.Text(master=root).pack()
root.geometry('550x550')
textbox=ttk.Label(master=root, text="Please enter your text",padding=10)
textbox.pack()
entry=ttk.Entry(master=root)
entry.insert(0,"this is the default text")
entry.pack()
def hello():
   ttk.Label(text="helloworld").pack()
button_exe1=ttk.Button(master=root, text="this WAS THE PART OF AN EXERCISE",command=hello)
button_exe1.pack()
button=ttk.Button(master=root, text="Save")
button.pack()
root.mainloop()
 """
#this tutorial shows you how to get the data using tkinter and how to set the values or modify the values of the widget using tkinter
""" root=tk.Tk()
entry=ttk.Entry(master=root,text="THis is an entry")
entry.grid(row=0,column=0, columnspan=10)
def button_command():
    button['text']=entry.get()
#this button here basically takes the command and then shows the text to the button
button=ttk.Button(master=root,command=button_command)
button.grid(row=1,column=1)
root.mainloop()
 """
#EXERCISE 3
#the task here is to create another button that enables the state and stuff works normally
""" root=tk.Tk()
entry=ttk.Entry(master=root,text="THis is an entry")
entry.grid(row=0,column=0, columnspan=10)
def button_command():
    button['text']=entry.get()
    entry['state']='disabled'
#this button here basically takes the command and then shows the text to the button
button=ttk.Button(master=root,command=button_command)
button.grid(row=1,column=1)
def button_enable():
    entry['state']='enabled'
    button['text']='this has been enabled'
button2=ttk.Button(master=root,text='Enabled', command=button_enable)
button2.grid(row=2,column=2)
root.mainloop()
 """
#EXERCISE 4
#Make is so that the text of the entry variable is same as that of the widget
""" root=tk.Tk()
#this string var is nothing but a tkinter variable
stringvar=tk.StringVar()
entry=ttk.Entry(master=root,text="THis is an entry",textvariable=stringvar)
entry.grid(row=0,column=0, columnspan=10)
label=ttk.Label(master=root,textvariable=stringvar)
label.grid(row=2,column=2)
root.mainloop() """
#EXERCISE 5
#create 2 entries and one label and set the start value of the test
""" root=tk.Tk()
#this string var is nothing but a tkinter variable
stringvar=tk.StringVar(value="Test")
def entry():
    if len(entry.get())!=0:
       entry['state']='enabled'
       entry2['state']='disabled'
    else:
        entry['state']='disabled'
        entry2['state']='enabled'
entry=ttk.Entry(master=root,text="THis is an entry",textvariable=stringvar)
entry.grid(row=0,column=0, columnspan=10)
entry2=ttk.Entry(master=root,text="THis is an entry,duplicate",textvariable=stringvar)
entry2.grid(row=1,column=1, columnspan=10)
label=ttk.Label(master=root,textvariable=stringvar)
label.grid(row=2,column=2)
button=ttk.Button(master=root,text="Find out!",command=entry)
button.grid(row=4,column=4)
root.mainloop()
 """
#BUTTONS IN TKINTER
r""" oot=tk.Tk()
root.title("Buttons")
root.geometry("500x500")
button=ttk.Button(root, text="This is a simple button")
button.pack()
#creating a checkbox
checkbox=ttk.Checkbutton(root, text="this is a checkbox")
checkbox.pack()
#while creating a radiobutton, it is important to set a value as the default values will be zero and not setting a value would mean checking both the buttons at the same time
butt1=ttk.Radiobutton(root, text="button1",value=5)
butt1.pack()
butt2=ttk.Radiobutton(root, text="button2",value=20,command=lambda:print("helloworld"))
butt2.pack()
root.mainloop() """

#EXERCISE 5
# Create check button and two radio buttons
#radio button:
#values for the button are a and B and ticking the radio button removes the check from checkbutton
#radio button prints the value of the check button
#check button:
#ticking the check button prints the value of the radio button
#use tkinter var for boolenas
""" root=tk.Tk()
root.title("Buttons")
root.geometry("500x500")
#creating a checkbox
check_var=tk.BooleanVar()
checkbox=ttk.Checkbutton(root, text="this is a checkbox",command=lambda:print(radio_var.get()),variable=check_var)
checkbox.pack()
#while creating a radiobutton, it is important to set a value as the default values will be zero and not setting a value would mean checking both the buttons at the same time
def radio_function():
    print(checkbox['text'])
    check_var.set(False)
radio_var=tk.StringVar()
butt1=ttk.Radiobutton(root, text="button1",value="A",variable=radio_var,command=radio_function)
butt1.pack()
butt2=ttk.Radiobutton(root, text="button2",value="B",variable=radio_var,command=radio_function)
butt2.pack()
root.mainloop() """
#functions with arguments inside the button
#it is important to use lambda function while using command as pythonexecutes the code from top to bottom
#EVENT BINDING
#Events can be a lot of things ranging from keyboard inputs to widgets getting chsnged, selected/unselected, mouse click motion, wheel wtc
#need to bind events to the widget using widget.bind(event, function)
#FORMAT: MODIFIER-TYPE-DETAIL
#event binding exercise:
#print mousewheel while the user holds down the shift and uses mousewheel while a text is selected
""" root=tk.Tk()
root.title("Buttons")
root.geometry("500x500")
#creating a checkbox
entry=ttk.Entry(root)
entry.pack()
entry.bind('<Shift-KeyPress>',lambda event: print("mousewheel"))
root.mainloop() """

#UNDERSTANDING COMBOBOX AND SPINBOX
#both just need a list of values
#both can be assigned to tkinter variables
#this code uses combox and a special combox event that is enclosed inside <<>>
#we can also use tkinter variables to basically set the first item of combobox
""" root=tk.Tk()
root.title("combo and spin")
root.geometry("500x500")
#creating a combo and spin
#creating a test variable
combobox_values=('noodles','pasta','pizza')
combo_var=tk.StringVar(value=combobox_values[0])
combobox=ttk.Combobox(root,foreground='red',background='yellow',textvariable=combo_var)
combobox.configure(values=combobox_values)
#setting values using works just fine as well but the method above is reccomended
combobox['values']=combobox_values 
combobox.pack()
combobox.bind('<<ComboboxSelected>>', lambda event: print("yes, you selected the event!"))
#creating a spinbox
spinbox=ttk.Spinbox(root, from_=1, to=100, increment=2)
spinbox.pack()
#event bindings for increment and decrement
spinbox.bind('<<Increment>>',lambda event: print("okayy this incremented"))
spinbox.bind('<<Decrement>>',lambda event: print("okayy this decremented"))
root.mainloop()
 """
#EXERCISE 7
#create a spinox with the values A,B,C,D,E
#print the value wheneber the value gets incremented
""" root=tk.Tk()
root.title("combo and spin")
root.geometry("500x500")
spin_values=("A","B","C","D","E")
spin_var=tk.StringVar(value=spin_values[0])
spinbox=ttk.Spinbox(root, textvariable=spin_var)
spinbox.configure(values=spin_values)
spinbox.pack()
#event bindings for increment and decrement
spinbox.bind('<<Increment>>',lambda event: print(spinbox.get()))
root.mainloop()
#CANVAS  """
#Canvas is essentially a widget that allows you to draw stuff 
#TREE VIEW:
#TREE VIEW IN TKINTER IS ESSENTIALLY JUST EXCEL


