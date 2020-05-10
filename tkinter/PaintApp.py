#Python Paint Application
from tkinter import *
import tkinter.font

#---------Define my class -----------------

class PaintApp:

# Define Class variables
    drawing_tool="arc"
    
    left_but="up"

    x_pos,y_pos=None,None
    x1_line,y1_line,x2_line,y2_line=None,None,None,None

    
# Catch Mouse Down
    def left_but_down(self,event=None):
        self.left_but="down"
        self.x1_line=event.x
        self.y1_line=event.y
        
        
# Catch Mouse up
    def left_but_up(self,event=None):
        self.left_but_up="up"
        
        self.x_pos=None
        self.y_pos=None
    
        self.x2_line=event.x
        self.y2_line=event.y
    
        if self.drawing_tool=="line":
            self.line_draw(event)
        elif self.drawing_tool=="arc":
            self.arc_draw()
        
# Catch Mouse Move
    def motion(self,event=None):
        if self.drawing_tool=="pencil":
            self.pencil_draw(event)
        
        
# Draw with a pencil
    def pencil_draw(self,event=None):
        if self.left_but=="down":
            if self.x_pos is not None and self.y_pos is not None:
                event.widget.create_line(self.x_pos,self.y_pos,event.x,event.y,smooth=True)
            self.x_pos=event.x
            self.y_pos=event.y
            
# Draw a line

    def line_draw(self,event=None):
        if None not in (self.x1_line,self.y1_line,self.x2_line,self.y2_line):
            event.widget.create_line(self.x1_line,self.y1_line,self.x2_line,self.y2_line,smooth=True,fill="green")
        
        
# Draw Arc
    
    def arc_draw(self,event=None):
        if None not in (self.x1_line, self.y1_line, self.x2_line, self.y2_line):
            coords=self.x1_line, self.y1_line, self.x2_line, self.y2_line
        
            event.widget.create_arc(coords,start=0,extent=150, style=ARC)
            

# Draw Oval
    def oval_draw(self,event=None):
        if None not in (self.x1_line, self.y1_line, self.x2_line, self.y2_line):
            event.widget.create_oval(self.)
        
# Draw Rectangle
# Draw Text
# Initialize
    def __init__(self,root):
        drawing_area=Canvas(root)
        drawing_area.pack()
        drawing_area.bind("<Motion>",self.motion)
        drawing_area.bind("<ButtonPress-1>", self.left_but_down)
        drawing_area.bind("<ButtonRelease-1>", self.left_but_up)
        
root=Tk()
paint_app=PaintApp(root)
root.mainloop()

