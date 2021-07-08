import turtle


screen = turtle.Screen()

t = turtle.Turtle()
t.color("red")
t.shape("turtle")
t.pensize(5)
turtle.bgcolor("black")

def circle():
  t.circle(150)

x = 0 
while x > 30:
  circle()
  x += 1

