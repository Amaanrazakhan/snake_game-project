import turtle as t 
STARTINGPOSITION=[(0,0),(-20,0),(-40,0)]

score=0
forward=20
UP=90
DOWN= 270
RIGHT=0
LEFT=180
movedistance=20
class Snake:
    def __init__(self):
        self.segment=[]
        self.createsnake()
        self.head=self.segment[0]
    def createsnake(self):
        for position in STARTINGPOSITION:
            self.addsegment(position)

    def addsegment(self,position):
            tim=t.Turtle("square")
            tim.color("white")
            tim.penup()
            tim.goto(position)
            self.segment.append(tim)
    def extend(self):
            self.addsegment(self.segment[-1].position())



    def move(self):
        for seg in range(len(self.segment)-1,0,-1):
            newx=self.segment[seg-1].xcor()
            newy=self.segment[seg-1].ycor()
            self.segment[seg].goto(newx,newy)
        self.head.forward(movedistance)

    def up(self):
        if self.head.heading() !=DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() !=UP:
            self.head.setheading(DOWN)
    def right(self):
        if self.head.heading() !=LEFT:
            self.head.setheading(RIGHT)
    def left(self):
        if self.head.heading() !=RIGHT:
            self.head.setheading(LEFT)
