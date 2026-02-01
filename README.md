Snake Game Project

This is a classic Snake Game that I built using Python and the Turtle graphics library. I created this project to practice Object-Oriented Programming (OOP) and understand how to manage game loops.

How to Play

The goal is to move the snake, eat the food, and grow as long as possible without hitting the walls or your own tail.

Controls:

Up Arrow: Move Up

Down Arrow: Move Down

Left Arrow: Move Left

Right Arrow: Move Right

How to Run the Game

Make sure you have Python installed.
Download all the files in this repository.
Run the file named "snakemain.py".
How I Made This (Code Explanation)

I broke the game down into four main parts using Python Classes:

1. The Snake (snake.py)

The snake is not just one object, but a list of turtle segments.
Movement: To make the snake move, I used a loop that moves the last segment to the position of the one in front of it. The head moves forward last. This makes the tail follow the head.
Direction: I added checks so the snake cannot reverse direction immediately (it cannot go down if it is currently going up).

2. The Food (Food.py)

This class inherits from the Turtle class.
It appears as a small circle.
Every time the snake touches it, it moves to a random X and Y coordinate between -320 and 320.

3. The Scoreboard (scoreboard.py)

This handles the text on the screen.
It keeps track of the score starting at 0.
When the game ends, it moves to the center and writes "GAMEOVER".

4. The Game Loop (snakemain.py)

This is the main file that runs the game.
It turns off automatic screen animation (tracer) so I can update the screen manually. This makes the movement smooth.
It checks for collisions with the wall (coordinates greater than 350) and collisions with the tail.
