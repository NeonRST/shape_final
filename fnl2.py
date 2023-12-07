import fnl
import random
import turtle


def get_new_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


com = int(input("Which art do you want to generate? Enter a number between 1 to 8, inclusive: "))
turtle.colormode(255)
if com == 1:
    for i in range(random.randint(20, 30)):
        shape1 = fnl.Shape(3, get_new_color())
        fnl.Shape.draw(shape1)
if com == 2:
    for i in range(random.randint(20, 30)):
        shape1 = fnl.Shape(4, get_new_color())
        fnl.Shape.draw(shape1)
if com == 3:
    for i in range(random.randint(20, 30)):
        shape1 = fnl.Shape(5, get_new_color())
        fnl.Shape.draw(shape1)
if com == 4:
    for i in range(random.randint(20, 30)):
        shape1 = fnl.Shape((random.randint(3, 5)), get_new_color())
        fnl.Shape.draw(shape1)
if com == 5:
    for i in range(random.randint(20, 30)):
        shape1 = fnl.Shape(3, get_new_color(), 0.618)
        for j in range(3):
            fnl.Shape.draw(shape1)
            fnl.Shape.repeat(shape1)
if com == 6:
    for i in range(random.randint(20, 30)):
        shape1 = fnl.Shape(4, get_new_color(), 0.618)
        for j in range(3):
            fnl.Shape.draw(shape1)
            fnl.Shape.repeat(shape1)
if com == 7:
    for i in range(random.randint(20, 30)):
        shape1 = fnl.Shape(5, get_new_color(), 0.618)
        for j in range(3):
            fnl.Shape.draw(shape1)
            fnl.Shape.repeat(shape1)
if com == 8:
    for i in range(random.randint(20, 30)):
        shape1 = fnl.Shape((random.randint(3, 5)), get_new_color(), 0.618)
        for j in range(3):
            fnl.Shape.draw(shape1)
            fnl.Shape.repeat(shape1)

turtle.speed(0)
turtle.bgcolor('black')
turtle.tracer(0)
turtle.done()