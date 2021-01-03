from turtle import Turtle
import random

def randNum():
  return random.randint(0, 280)

class Food(Turtle):

  def __init__(self):
    super().__init__()
    self.shape("circle")
    self.penup()
    self.shapesize(stretch_len=0.5, stretch_wid=0.5)
    self.color("blue")
    self.speed("fastest")
    self.new_loc()

  def new_loc(self):
    rand_x = randNum()
    rand_y = randNum()
    self.goto(rand_x, rand_y)