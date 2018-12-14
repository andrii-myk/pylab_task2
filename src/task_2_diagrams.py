import sys
from turtle import *

dict = {}

"""Needs text file given as command line argument """

def load_file():
    if len(sys.argv) == 2:
        with open(sys.argv[1], 'r') as file:
            for line in file:
                for word in line.split():
                    words_to_dict(word.lower(), dict)
    else:
        print("You didn't give an argument.")


def words_to_dict(word, dict):
    if word in dict:
        temp_value = dict[word]
        dict[word] = temp_value + 1
    else:
        dict[word] = 1


def turtle_config(turtle):
    turtle.penup()
    turtle.setpos(-480, -200)
    turtle.pensize(3)
    turtle.color("red")
    turtle.pendown()
    turtle.forward(961)
    turtle.screen.bgcolor("#f2f2f2")
    turtle.screen.title("The greates diagrams builder app")


def draw_diagram(dict, turtle):
    turtle.penup()
    turtle.setx(-470)
    turtle.pendown()
    colors = ("blue", "black", "green", "orange", "purple", "red")
    turtle.left(90)
    counter = 0
    for value in dict.values():
        turtle.color(colors[counter % len(colors)])
        turtle.pensize(5)
        turtle.forward(value * 50)
        turtle.right(90)
        turtle.forward(5)
        turtle.right(90)
        turtle.forward(value * 50)
        turtle.left(90)
        turtle.pensize(1)
        turtle.color("red")
        turtle.forward(10)
        turtle.left(90)
        counter += 1
        if turtle.xcor() > 481:
            break

    counter = 0
    turtle.goto(-470, -220)
    for key in dict.keys():
        turtle.penup()
        turtle.color(colors[counter % len(colors)])
        turtle.write(f"{counter} {key}\t", True, font=14)
        counter += 1
        if turtle.xcor() > 470:
            turtle.goto(-470, turtle.ycor() - 20)


def main():
    load_file()
    #print(dict)
    turtle = Turtle()
    turtle.screen.screensize(800, 600)
    turtle_config(turtle)
    draw_diagram(dict, turtle)
    turtle.screen.exitonclick()


if __name__ == "__main__":
    main()