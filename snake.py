from turtle import Screen, Turtle
import time

CONSTANT_SPEED = 20
#DIRECTIONS
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
  def __init__(self):
    self.snakes = []
    self.create_snake()
    self.head = self.snakes[0]

  def create_snake(self):
    for _ in range(0, 3):  
      self.add_body()
  
  

  def add_body(self):
    loc = -0
    obj = Turtle()
    obj.shape("square")
    obj.color("white")
    obj.penup()
    obj.goto(x = loc, y = 0)
    loc -= 20
    self.snakes.append(obj)

  def move(self):
    for obj_loc in range(len(self.snakes) - 1, 0, -1):
      prev_x = self.snakes[obj_loc-1].xcor()
      prev_y = self.snakes[obj_loc-1].ycor()
      self.snakes[obj_loc].goto(x = prev_x, y = prev_y)
    self.snakes[0].forward(CONSTANT_SPEED)

 #Key bind control
  def up(self):
    if(self.head.heading() != DOWN):
      self.snakes[0].setheading(UP)
  def down(self):
    if(self.head.heading() != UP):
      self.snakes[0].setheading(DOWN)
  def left(self):
    if(self.head.heading() != RIGHT):
      self.snakes[0].setheading(LEFT)
  def right(self):
    if(self.head.heading()  != LEFT):
      self.snakes[0].setheading(RIGHT)

  def get_length(self):
    return len(self.snakes)

  def cut_snake(self):
    for i in range(3, self.get_length()):
      if(self.head.xcor() == self.snakes[i].xcor() and self.head.ycor() == self.snakes[i].ycor()):
        
        exit()
