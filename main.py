import turtle


class BezierTurtle(turtle.Turtle):
    def __init__(self):
        super().__init__()

    def linear_bezier(self, x0, y0, x1, y1, res=100):
        """
        Make a linear Bézier curve (straight line) starting at(x0, y0) and going to (x1, y1)
        The optional parameter res (resolution) defines how many points should be used to create the curve.
        Res defaults to 100.
        """
        self.penup()
        for t in range(0, res + 1):
            self.goto(lerp(x0, x1, t / res), lerp(y0, y1, t / res))
            if t == 0:
                self.pendown()
        self.penup()

    def quadratic_bezier(self, x0, y0, x1, y1, x2, y2, res=100):
        """
        Creates a quadratic Bézier curve starting at (x0, y0) and ending at (x2, y2).
        The x1 and y1 parameters are for the control point.
        The optional parameter res (resolution) defines how many points should be used to create the curve.
        Res defaults to 100.
        """
        self.penup()
        for t in range(0, res + 1):
            self.goto(
                lerp(
                    lerp(x0, x1, t / res),
                    lerp(x1, x2, t / res),
                    t / res),
                lerp(
                    lerp(y0, y1, t / res),
                    lerp(y1, y2, t / res),
                    t / res)
            )
            if t == 0:
                self.pendown()
        self.penup()

    def cubic_bezier(self, x0, y0, x1, y1, x2, y2, x3, y3, res=100):
        """
        Creates a cubic Bézier curve starting at (x0, y0) and ending at (x3, y3).
        The x1 and y1 parameters are for the first control point;
        The x2 and y2 parameters are for the second control point.
        """
        self.penup()
        for t in range(0, res + 1):
            self.goto(
                lerp(
                    lerp(
                        lerp(x0, x1, t / res),
                        lerp(x1, x2, t / res),
                        t / res),
                    lerp(
                        lerp(x1, x2, t / res),
                        lerp(x2, x3, t / res),
                        t / res),
                    t / res
                ),

                lerp(
                    lerp(
                        lerp(y0, y1, t / res),
                        lerp(y1, y2, t / res),
                        t / res),
                    lerp(
                        lerp(y1, y2, t / res),
                        lerp(y2, y3, t / res),
                        t / res),
                    t / res
                ),
            )
            if t == 0:
                self.pendown()
        self.penup()


def lerp(x0, x1, t):
    return x0 + (x1 - x0) * t


def resetScreen():
    global click_number
    tr.clear()
    click_number = 0


def draw():
    tr.linear_bezier(start_x, start_y, end_x, end_y, 10000)
    tr.quadratic_bezier(start_x, start_y, control1_x, control1_y, end_x, end_y, 10000)
    tr.cubic_bezier(start_x, start_y, control1_x, control1_y, control2_x, control2_y, end_x, end_y, 10000)

    turtle.onkeypress(resetScreen, 'space')
    turtle.listen()

    font = ("Arial", 14, "bold")
    tr.goto(0, sc.window_height() / 2 - 30)
    tr.write("Press space to clear", align="center", font=font)


def clickHandler(x, y):
    global click_number
    click_number += 1
    if click_number == 1:
        global start_x, start_y
        start_x = x
        start_y = y
        tr.goto(start_x, start_y)
        tr.dot(20, "red")
    elif click_number == 2:
        global end_x, end_y
        end_x = x
        end_y = y
        tr.goto(end_x, end_y)
        tr.dot(20, "red")
    elif click_number == 3:
        global control1_x, control1_y
        control1_x = x
        control1_y = y
        tr.goto(control1_x, control1_y)
        tr.dot(20, "red")
    elif click_number == 4:
        global control2_x, control2_y
        control2_x = x
        control2_y = y
        tr.goto(control2_x, control2_y)
        tr.dot(20, "red")
        draw()


if __name__ == "__main__":
    click_number = 0

    tr = BezierTurtle()
    sc = turtle.Screen()

    tr.shape("arrow")
    tr.speed(0)
    turtle.delay(0)
    tr.hideturtle()
    tr.pensize(2)
    sc.tracer(0)
    tr.penup()

    turtle.title("Bézier Curve Maker")
    turtle.onscreenclick(clickHandler)

    turtle.done()
