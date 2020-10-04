import turtle

turtle.hideturtle()
turtle.tracer(0)
turtle.penup()
turtle.setposition(-380, 300)
turtle.pensize(2)
turtle.pendown()

axiom = input("Enter the starting axiom (chars available: F+-):\n")
itr = int(input("Enter the number of iterations:\n"))

rule = {
    "+":"+",
    "-":"-",
    "F":"F+F-F-F+F"
}

tmp_axiom = ""

for i in range(itr):
    for char in axiom:
        tmp_axiom += rule[char]
    axiom, tmp_axiom = tmp_axiom, ""

for char in axiom:
    if char == "+":
        turtle.right(90)
    elif char == "-":
        turtle.left(90)
    else:
        turtle.forward(5)

turtle.update()
turtle.mainloop()
