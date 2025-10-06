import turtle
t = turtle.Turtle()
t.speed(5) # 1:slowest, 3:slow, 5:normal, 10:fast, 0:fastest

t.setpos(0,0) # Define la posición inicial 
t.goto(-20,-20) # Mueve a la tortuga a la coordenada (-20, -20)

t.forward(100)
t.setpos(-100,-100)
t.penup()
t.right(90)
t.forward(100)
t.pendown()
t.right(90)
t.forward(100)

