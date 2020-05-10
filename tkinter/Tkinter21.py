from tkinter import *
from tkinter import messagebox

def get_data(event=None):
    print("String:",strVar.get())
    print("Integer:",intVar.get())
    print("Double: ",dblVar.get())
    print("Boolean: ",boolVar.get())
    
def bind_button(event):
    if boolVar.get():
        getDataButton.unbind("<Button-1>")
    else:
        getDataButton.bind("<Button-1>",get_data)

root=Tk()
strVar = StringVar()
intVar=IntVar()
dblVar=DoubleVar()
boolVar=BooleanVar()

strVar.set("Enter String")
intVar.set("Enter Integer")
dblVar.set("Enter Double")
boolVar.set(True)

strEntry=Entry(root,textvariable=strVar)
strEntry.pack(side=LEFT)

intEntry=Entry(root,textvariable=intVar)
intEntry.pack(side=LEFT)

dblEntry=Entry(root,textvariable=dblVar)
dblEntry.pack(side=LEFT)

boolEntry=Checkbutton(root,text="Switch", variable=boolVar)
boolEntry.bind("<Button-1>",bind_button)
boolEntry.pack(side=LEFT)

getDataButton=Button(root,text="Get Data!")
getDataButton.bind("<Button-1>",get_data)
getDataButton.pack(side=LEFT)



root.mainloop()