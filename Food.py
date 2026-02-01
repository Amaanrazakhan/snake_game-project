from turtle import Turtle 
import random 
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        
        self.penup()
        self.shapesize(stretch_len=0.7,stretch_wid=0.7)
        self.color("red")
        self.speed("fastest")
        self.refresh()
        

    
    def refresh(self):
        x=random.randint(-320,320)
        y=random.randint(-320,320)
        self.goto(x,y)