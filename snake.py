import turtle
from turtle import Turtle, Screen
import time
from random import randint
screen = Screen()
screen.tracer(0)
screen.setup(800, 800)


class Snake:
	def __init__(self,):
		self.snake_body = []
		self.count = 0

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
