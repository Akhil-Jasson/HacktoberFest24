from turtle import Turtle
from random import randint


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.penup()
        self.speed("fastest")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5) # Shape is usually 20x20 pxs -> Becomes 10x10 pxs
        rand_x = randint(-280, 280)
        rand_y = randint(-280, 280)
        self.goto(rand_x, rand_y)

    def refresh(self):
        rand_x = randint(-280, 280)
        rand_y = randint(-280, 280)
        self.goto(rand_x, rand_y)

