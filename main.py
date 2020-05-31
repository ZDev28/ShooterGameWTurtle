from time import sleep
import random
import turtle

wn = turtle.Screen()
wn.bgcolor("red")

wintimes = 0

player = turtle.Turtle()
player.shape("turtle")

enemy = turtle.Turtle()

enemy.shape("turtle")
enemy.color("green")

bullet = turtle.Turtle()
bullet.hideturtle()

x = random.randint(1,300)
y = random.randint(1,300)

enemy.goto(x,y)


def forwardd():
  player.forward(25)

def backwardd():
  player.backward(25)

def leftt():
  player.left(90)

def rightt():
  player.right(90)

def shoot():
  thenewx = random.randint(1,300)
  thenewy = random.randint(1,300)
  enemy.hideturtle()
  enemy.goto(thenewx,thenewy)
  sleep(2.0)
  enemy.showturtle()
  global wintimes
  wintimes += 1
  if wintimes == 10:
    print("Alright! You win! Clear all!")
    wn.clear()

wn.onkey(forwardd, "Up")
wn.onkey(backwardd, "Down")
wn.onkey(leftt, "Left")
wn.onkey(rightt, "Right")
wn.onkey(shoot, "x")

wn.listen()
