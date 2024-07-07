from turtle import Turtle
from random import randint

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.8, 0.8)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        randx = randint(-280, 280)
        randy = randint(-280, 280)
        self.goto(randx, randy)