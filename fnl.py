import turtle
import random

class Shape:
    def __init__(self, num_sides, color, ratio=1):
        self.num_sides = num_sides
        self.size = random.randint(50, 150)
        self.orientation = random.randint(0, 90)
        self.location = [random.randint(-300, 300), random.randint(-200, 200)]
        self.color = color
        self.border_size = random.randint(1, 10)
        self.reduction_ratio = ratio

    def draw(self):
        turtle.penup()
        turtle.goto(self.location[0], self.location[1])
        turtle.setheading(self.orientation)
        turtle.color(self.color)
        turtle.pensize(self.border_size)
        turtle.pendown()
        for _ in range(self.num_sides):
            turtle.forward(self.size)
            turtle.left(360 / self.num_sides)
        turtle.penup()
        turtle.tracer(0)
        turtle.speed(0)
        turtle.bgcolor('black')
        turtle.colormode(255)
        turtle.penup()
        turtle.forward(self.size * (1 - self.reduction_ratio) / 2)
        turtle.left(90)
        turtle.forward(self.size * (1 - self.reduction_ratio) / 2)
        turtle.right(90)
        self.location[0] = turtle.pos()[0]
        self.location[1] = turtle.pos()[1]

    def set_color(self, new_color):
        self.color = new_color

    def repeat(self):
        self.size *= self.reduction_ratio

