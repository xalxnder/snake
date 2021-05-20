from turtle import Turtle, Screen
from random import randint
import time
screen = Screen()
screen.tracer(0)


screen.setup(800, 800)



class Food(Turtle):
	def __init__(self):
		super().__init__()
		self.shape("circle")
		self.penup()
		self.color("blue")

	def random_cord(self):
		x = randint(-350, 350)
		y = randint(-350, 300)
		return (x, y)





target = Food()
target.goto(target.random_cord())


time.sleep(0.1)
screen.update()
screen.exitonclick()