import turtle


screen = turtle.Screen()

t = turtle.Turtle()
t.color("red")
t.shape("turtle")
t.pensize(2)
turtle.bgcolor("grey")

t2 = turtle.Turtle()
t.color("green")
t.shape("arrow")
t.pensize(3)

t3 = turtle.Turtle()
t.color("blue")
t.shape("turtle")
t.pensize(3)

def square2():
  for i in range(4):
    t.forward(120)
    t.left(90)


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
while x < 75:
  square()
  t2.left(5) 
  x+=1

for i in range(30):
  circle()
  t.right(10)  

for i in range(30):
  square2()
  t.right(14)