from turtle import Turtle

class Scoreboard(Turtle):

  def __init__(self):
    super().__init__()
    self.score = 0
    self.high_score = 0
    self.color("white") 
    self.penup()
    self.goto(0, 270)
    self.hideturtle()
    self.fillcolor("black")
    self.update_score()
    with open("high_score.txt") as file:
      self.high_score = int(file.read())
  
  def add_point(self):
    self.clear()
    self.score += 1
    self.update_score()

  def update_score(self):
    self.clear()
    self.write(f"Score: {self.score} High Score: {self.high_score}", move=False, align="center", font=("Verdana", 16, "normal"))

#  def game_over(self):
#    self.clear()
#    self.goto(0, 0)
#    self.write(f"***GAME OVER*** FINAL SCORE: {self.score}", move=False, align="center", font=("Verdana", 16, "normal"))

  def reset(self):
    if self.score > int(self.high_score):
      self.high_score = self.score
      with open("high_score.txt", "w") as file:
        file.write(f"{self.high_score}")
    self.score = 0
    self.update_score()
