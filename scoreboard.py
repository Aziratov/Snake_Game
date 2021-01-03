from turtle import Turtle

class Scoreboard(Turtle):

  def __init__(self):
    super().__init__()
    self.score = 0
    self.color("white") 
    self.penup()
    self.goto(0, 270)
    self.hideturtle()
    self.fillcolor("black")
    self.update_score()
  
  def add_point(self):
    self.clear()
    self.score += 1
    self.update_score()

  def update_score(self):
    self.write(f"Score: {self.score}", move=False, align="center", font=("Verdana", 16, "normal"))

  def game_over(self):
    self.clear()
    self.goto(0, 0)
    self.write(f"***GAME OVER*** FINAL SCORE: {self.score}", move=False, align="center", font=("Verdana", 16, "normal"))
