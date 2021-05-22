from turtle import Turtle, Screen
from random import randint
import time
screen = Screen()
screen.tracer(0)

screen.setup(800, 800)


class Snake:
	def __init__(self,):
		self.snake_body = []
		self.count = 0
		self.score = 0

	#Add snake body
	def create_snake(self):
		snake = Turtle()
		snake.penup()
		snake.shape("square")
		snake.speed(1)
		self.snake_body.append(snake)
		snake.setpos(self.count, 0)
		self.count += 10

	#The snake movement
	def move_snake(self):
		for i in range(len(self.snake_body) - 1, 0, -1):
			self.snake_body[i].goto(self.snake_body[i - 1].xcor(), self.snake_body[i - 1].ycor())
		self.snake_body[0].forward(20)

	# Snake Controls
	def up(self):
		if self.snake_body[0].heading() != 270:
			self.snake_body[0].setheading(90)

	def down(self):
		if self.snake_body[0].heading() != 90:
			self.snake_body[0].setheading(270)

	def left(self):
		if self.snake_body[0].heading() != 0:
			self.snake_body[0].setheading(180)

	def right(self):
		if self.snake_body[0].heading() != 180:
			self.snake_body[0].setheading(0)


class Target(Turtle):
	def __init__(self):
		super().__init__()
		self.shape("circle")
		self.penup()
		self.color("blue")

	def random_cord(self):
		x = randint(-350, 350)
		y = randint(-350, 300)
		return (x, y)

class ScoreBoard(Turtle):
	def __init__(self):
		super().__init__()
		self.score = 0
		self.penup()
		self.hideturtle()
		self.goto(0,350)
		self.write("Score = " + str(self.score), True, align="center", font=("Arial", 30, "normal"))

	def add_score(self):
		self.score += 1
		self.goto(0,350)
		self.write("Score = " + str(self.score), True, align="center", font=("Arial", 30, "normal"))


class GameOver(Turtle):
	def __init__(self):
		super().__init__()


	def message(self):
		self.penup()
		self.hideturtle()
		self.write("Game Over", True, align="center", font=("Arial", 30, "normal"))






