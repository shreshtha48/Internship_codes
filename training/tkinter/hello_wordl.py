#in tkinter the first thing that you create is a root widget which is sort of like a graphical programming window
import tkinter
root= tkinter.Tk()
label = tkinter.Label(root, text="Hello, Tkinter",foreground="white",background="purple",width=25,height=10)
#In order to create anything in tkinter, it is a two step process, we have to first define the thing and then we have to put it up on the window as well
#showing stuff on screen has several options, first is pack which means just shoving stuff in there at the first avaialbe space
label.pack()
root.mainloop()