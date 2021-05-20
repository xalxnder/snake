import turtle
from turtle import Turtle, Screen
import time
from random import randint
from snake import Snake, Target, ScoreBoard
screen = Screen()
screen.tracer(0)
screen.setup(800, 800)

snake = Snake()
food = Target()
score = ScoreBoard()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

for i in range(3):
	snake.create_snake()
#

#Generate food
food.goto(food.random_cord())


game_on = True

while game_on:
	screen.listen()
	time.sleep(0.1)
	screen.update()
	snake.move_snake()
	# Detetct when snake eats food
	if snake.snake_body[0].distance(food) < 15:
		score.score += 1
		score.clear()
		score.add_score()
		snake.create_snake()
		food.goto(food.random_cord())

#Detect collision with body
	for body in snake.snake_body:
		if body == snake.snake_body[0]:
			pass
		elif snake.snake_body[0].distance(body) < 10:
			game_on = False
			print("Ahh")

#
screen.exitonclick()