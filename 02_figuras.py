import turtle
donatello = turtle.Turtle()
donatello.speed(5) # 1:slowest, 3:slow, 5:normal, 10:fast, 0:fastest

# Algoritmo para dibujar un cuadrado
lado = 100
donatello.forward(lado)
donatello.left(90)
donatello.forward(lado)
donatello.left(90)
donatello.forward(lado)
donatello.left(90)
donatello.forward(lado)

def cuadrado(lado):
  donatello.forward(lado)
  donatello.left(90)
  donatello.forward(lado)
  donatello.left(90)
  donatello.forward(lado)
  donatello.left(90)
  donatello.forward(lado)

cuadrado(50)
cuadrado(50)
cuadrado(50)

def Hexagono (lado):
  donatello.forward(lado)
  donatello.right(60)
  donatello.forward(lado)
  donatello.right(60)
  donatello.forward(lado)
  donatello.right(60)
  donatello.forward(lado)
  donatello.right(60)
  donatello.forward(lado)
  donatello.right(60)
  donatello.forward(lado)
  donatello.right(60)

Hexagono(100)
