import tkinter as tk
#using the grid system to show the files, we can specify which file stays at the top and which one stays at the bottom
#using rows and columns
#the positioning here is relative to the size of the gui of the screens
""" root=tk.Tk()
label1= tk.Label(text="Namaste!",foreground="white",background="black")
label2=tk.Label(text="I am shreshtha", foreground="white",background="black")
label1.grid(row=0,column=1)
label2.grid(row=1, column=1 )
root.mainloop() """

#USING BUTTONS
""" root=tk.Tk()
label1= tk.Label(text="Namaste!",foreground="white",background="black")
label2=tk.Label(text="I am shreshtha", foreground="white",background="black")
label1.grid(row=0,column=1)
label2.grid(row=1, column=1 )
button1=tk.Button(text="About Me")
#we can also pad this button i.e. define the button using the x and y axis by using
button1.grid(row=15,column=15, padx=20, pady=15)
root.mainloop() """
#this doesnt actually do anything, in order to do something, we need to define a function that does the stuff
""" root=tk.Tk()
label1= tk.Label(text="Namaste!",foreground="white",background="black")
label2=tk.Label(text="I am shreshtha", foreground="white",background="black")
def button_click():
    label_show=tk.Label(text="you clicked the buttom")
    label_show.pack()
    return
label1.pack()
label2.pack()
button1=tk.Button(text="click this",command=button_click)
button1.pack()
root.mainloop() """
#so this was our button journey

#CREATING ENTRY IN THE PROMPT
#we can change the width, background and forgeround colour of this entry prompt and borderwidth
""" root=tk.Tk()
entryy=tk. Entry()
entryy.pack()
def button_click():
    label_show=tk.Label(text=entryy.get())
    label_show.pack()
    return
button1=tk.Button(text="click this",command=button_click)
button1.pack()
root.mainloop() """
#now that we have created entry in the prompt, let us focus on the more important things
#in order to enter some default text inside of your text we can use entryy.insert(text="text to be inserted")
root=tk.Tk()
label1= tk.Label(text="Namaste!",foreground="white",background="black")
label2=tk.Label(text="I am shreshtha", foreground="white",background="black")
def button_click():
    label_show=tk.Label(text="you clicked the buttom")
    label_show.pack()
    return
label1.pack()
label2.pack()
button1=tk.Button(text="click this",command=button_click)
button1.pack()
root.mainloop()

