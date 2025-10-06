import turtle
t = turtle.Turtle()
t.speed(5) # 1:slowest, 3:slow, 5:normal, 10:fast, 0:fastest

def tree(i):
  if i < 10:
    return
  else:
    t.forward(i)
    t.left(30)
    tree(3*i/4)
    t.right(60)
    tree(3*i/4)
    t.left(30)
    t.backward(i)

#tree(80)

def koch_curve(order, length):
  if order == 0:
    t.forward(length)
  else:  
    koch_curve(order - 1, length / 3)
    t.left(60)
    koch_curve(order - 1, length / 3)
    t.right(120)
    koch_curve(order - 1, length / 3)
    t.left(60)
    koch_curve(order - 1, length / 3)

koch_curve(2, 100)   
