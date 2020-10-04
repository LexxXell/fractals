#!/usr/bin/env python3
# L-system by LexxXell

import turtle

# screen and turtle initialize
W,H = 1920, 1080
screen = turtle.Screen()
screen.setup(W,H)
screen.screensize(2*W, 2*H)
screen.delay(0)
screen.bgcolor("black")
trt = turtle.Turtle()
trt.pensize(2)
trt.speed(0)
trt.color("magenta")
trt.goto(-W//3, -H//2)
trt.clear()
trt.fillcolor("violet")


# l-system settings
axiom = "F"
gens = 7
angle = 120
step = 5
rules = {
    "+":"+",
    "-":"-",
    "G":"GG",
    "F":"F-G+F+G-F"
}

for gen in range(gens):
    axiom = ''.join([rules[chr] for chr in axiom])

# trt.begin_fill() # Uncomment if need fill
for char in axiom:
    if char == "+":
        trt.right(angle)
    elif char == "-":
        trt.left(angle)
    else:
        trt.forward(step)
# trt.end_fill() # Uncomment if need fill

trt.hideturtle()
screen.exitonclick()