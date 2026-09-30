from manim import *


class CircleToSquare(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency
        mySquare = Square()
        mySquare.set_fill(WHITE)
        mySquare.rotate(PI / 4)

        self.play(Create(mySquare))
        self.play(Transform(mySquare, circle))
        self.play(FadeOut(mySquare))


class SquareNextToCircle(Scene):
    def construct(self):
        circle = Circle()
        square = Square()

        circle.set_fill(BLUE, opacity=0.5)
        square.set_fill(RED, opacity=0.5)

        circle.next_to(square, LEFT, 0.5)

        self.play(Create(circle), Create(square))


class SquareUpToCircle(Scene):
    def construct(self):
        circle = Circle()
        square = Square()

        circle.set_fill(BLUE, opacity=0.5)
        square.set_fill(RED, opacity=0.5)

        circle.next_to(square, UP, 0.5)

        self.play(Create(circle), Create(square))


class SquareToCircleAnimation(Scene):
    def construct(self):
        circle = Circle()
        square = Square()

        self.play(Create(square))
        self.play(square.animate.rotate(PI / 4))
        self.play(Transform(square, circle))
        self.play(
            circle.animate.set_fill(RED, opacity=0.5)
        )
