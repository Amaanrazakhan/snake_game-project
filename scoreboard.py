from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.penup()
        self.color("white")
        self.goto(0,270)
        self.updatescoreboard()
        self.hideturtle() 
    def updatescoreboard(self):
         self.write(f" score {self.score}",align="center",font=("Arial" ,24,"normal"))
    
    def gameover(self):
        self.goto(0,0)
        self.write("GAMEOVER",align="center",font=("Arial" ,24,"normal"))
    
    def increasescore(self):

        self.score+=1
        self.clear()
        self.updatescoreboard()
        