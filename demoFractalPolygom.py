import turtle
import hw6Functions

n = int(input("How many sides? "))
radius = int(input("Enter radius (between 10 - 200 "))
depth = int(input("Enter depth for Sierpinski "))
window = turtle.Screen()
bob = turtle.Turtle()
bob.hideturtle()
bob.getscreen().tracer(0)
hw6Functions.draweverything(bob, radius, n, depth)
bob.getscreen().update()
window.exitonclick()
