from turtle import Screen
from snake import Snake
from food import Food
import time

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


snake = Snake()
food = Food()

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

screen.exitonclick()