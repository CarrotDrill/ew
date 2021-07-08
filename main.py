import turtle


screen = turtle.Screen()

t = turtle.Turtle()
t.color("red")
t.shape("turtle")
t.pensize(5)
turtle.bgcolor("grey")

t2 = turtle.Turtle()
t.color("green")
t.shape("arrow")
t.pensize(3)

def square():
  t.fillcolor("red")
  t.begin_fill()
  for i in range(4):
    t2.forward(100)
    t2.left(90)
  t.end_fill()
    

def circle():
  t.circle(150)



x = 0 
while x < 30:
  square()
  t2.left(5)
  circle()
  t.right(10) 
  x += 1


