from turtle import speed, left, right, forward, setpos, clear
speed('fastest')


def draw_triangle(angle, size):
    if size > 0.5:
        left(angle)
        draw_triangle(-angle, size - 0.5)
        right(angle)
        draw_triangle(angle, size - 0.5)
        right(angle)
        draw_triangle(-angle, size - 0.5)
        left(angle)
    else:
        left(angle)
        forward(size)
        right(angle)
        forward(size)
        right(angle)
        forward(size)
        left(angle)


setpos(-300, -300)
clear()
draw_triangle(60, 10)