from turtle import Screen
import turtle as t
from snake import Snake
from Food import Food
import time
from scoreboard import Scoreboard


screen=t.Screen()
screen.setup(width=700,height=700)
screen.bgcolor("grey")
screen.title("My snake game")
screen.tracer(0)
snake=Snake()
food=Food()
scoreboard=Scoreboard()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")

gameison=True

while gameison:
    screen.update()
    time.sleep(.08)
    snake.move()
    if snake.head.distance(food)<18:
        food.refresh()
        snake.extend()
        scoreboard.increasescore()
    if snake.head.xcor()>350 or snake.head.xcor()<-350 or snake.head.ycor()>350 or snake.head.ycor()<-350:
        gameison=False
        scoreboard.gameover()

    #detection collision with snake tail
    for j in snake.segment[1:]:
        if snake.head.distance(j)<10:
            if j==snake.head:
                pass
            elif snake.head.distance(j)<10:
                gameison=False
                scoreboard.gameover()
screen.exitonclick()