import hw6Functions
import turtle

n = int(input("How many sides? "))
radius = int(input("Enter radius (between 100 - 500 "))
depth = int(input("Enter depth for Sierpinski "))
bob = turtle.Turtle()
bob.hideturtle()
bob.getscreen().tracer(0)
hw6Functions.drawinverted(bob, radius, n, depth)
bob.getscreen().update()
window = turtle.Screen()
window.exitonclick()
