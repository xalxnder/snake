import turtle
from turtle import Turtle, Screen
import time
from random import randint
screen = Screen()
screen.tracer(0)
screen.setup(800, 800)
snake_body = []
count = 0


#Initiate the snake body
for i in range(7):
	snake = Turtle()
	snake.penup()
	snake.shape("square")
	snake.speed(1)
	snake_body.append(snake)
	snake.setpos(count, 0)
	count += 10


def move_snake():
	for i in range(len(snake_body) - 1, 0, -1):
		print(i)
		snake_body[i].goto(snake_body[i - 1].xcor(), snake_body[i - 1].ycor())
	snake_body[0].forward(20)


#Snake Controls
def up():
	if snake_body[0].heading() != 270:
		snake_body[0].setheading(90)

def down():
	if snake_body[0].heading() != 90:
		snake_body[0].setheading(270)

def left():
	if snake_body[0].heading() != 0:
		snake_body[0].setheading(180)

def right():
	if snake_body[0].heading() != 180:
		snake_body[0].setheading(0)

screen.onkey(up, "Up")
screen.onkey(down, "Down")
screen.onkey(left, "Left")
screen.onkey(right, "Right")

#Generate food
def random_coord():
	x = randint(-350, 350)
	y = randint(-350, 300)
	return (x,y)
food = Turtle()
food.shape("circle")
food.fillcolor("blue")
food.penup()

#Detetct when snake eats food
food.goto(random_coord())

while True:
	screen.listen()
	time.sleep(0.1)
	screen.update()
	move_snake()
	if snake_body[0].distance(food) < 15:
		food.goto(random_coord())


screen.exitonclick()



