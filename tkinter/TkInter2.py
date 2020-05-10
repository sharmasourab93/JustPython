from tkinter import *

from tkinter import ttk

root=Tk()
# Multiple components
# some of the different widgets: Button, Label,
# CanvasMenu, Text, Scale, OptionMenu, Frame
# CheckButton, LabelFrame, MenuButton, PanedWindow,
# Entry, ListBox, Message, RadioButton, Scrollbar,
# Butmap, SpinBox, Image

frame= Frame(root)
labelText=StringVar()
label= Label(frame, textvariable=labelText)
button=Button(frame, text="Click Me!")

labelText.set("I Am a Label")

label.pack()
button.pack()
frame.pack()

root.mainloop()