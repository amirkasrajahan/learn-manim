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


