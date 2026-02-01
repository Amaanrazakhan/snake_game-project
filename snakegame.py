import turtle as t


screen=t.Screen()
screen.setup(width=700,height=700)
screen.bgcolor('grey')
screen.title("the kuchipuchi snake")
starting_position=[(0,0),(-20,0),(-40,0)]

tim=t.Turtle()
tim.color("white")
tim.shape("turtle")

tim2=t.Turtle()
tim2.color("white")
tim2.shape("square")
tim2.goto(-20,0)

tim3=t.Turtle()
tim3.shape("square")
tim3.color("white")
tim3.goto(-40,0)
tim.penup()
tim2.penup()
tim3.penup()







screen.exitonclick()
