from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")


game_running = True

while game_running:
  screen.update()
  time.sleep(0.1)
  snake.move()

  #Collision with food item
  if(snake.head.distance(food) <= 15):
    food.new_loc()
    snake.add_body()
    score.add_point()

  #Collision with each window
  if(snake.head.xcor() > 280):
    snake.head.goto(x = -280, y = snake.head.ycor())
  if(snake.head.xcor() < -280):
    snake.head.goto(x = 280, y = snake.head.ycor())

  if(snake.head.ycor() > 280):
    snake.head.goto(x = snake.head.xcor(), y = -280)

  if(snake.head.ycor() < -280):
    snake.head.goto(x = snake.head.xcor(), y = 280)

  #Self collision, game over using slicing
  for obj in snake.snakes[1:]:
    if (snake.head.distance(obj) < 10):
      game_running = False
      score.game_over()




screen.exitonclick()