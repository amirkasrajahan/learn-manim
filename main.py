from manim import *
import math
numbers = [i for i in range(10)]
print(numbers)
print
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


class LinearSearch(Scene):
    def construct(self):
        values = [4, 8, 15, 16, 23, 42]
        target = 23

        leftcells = VGroup(*[
            VGroup(Square(side_length=1), Text(str(values[i]), font_size=36))
            for i in range(int(math.ceil(len(values)/2)))
        ])

        rightcells = VGroup(*[
            VGroup(Square(side_length=1), Text(str(values[i]), font_size=36))
            for i in range(int(math.ceil(len(values)/2)), len(values))
        ])
        # for cell in cells:
        #     cell[1].move_to(cell[0].get_center())
        leftcells.arrange(RIGHT, buff=0)
        rightcells.arrange(RIGHT, buff=0)

        rightcells.next_to(leftcells, RIGHT, buff=0)
        self.play(Create(leftcells), Create(rightcells))

        cells = VGroup(*leftcells, *rightcells)
        for cell, v in zip(cells, values):
            box = cell[0]
            self.play(box.animate.set_fill(YELLOW, opacity=0.7), run_time=0.3)
            if v == target:
                self.play(box.animate.set_fill(GREEN, opacity=0.7))
                self.play(Indicate(cell))
                break
            self.play(box.animate.set_fill(WHITE, opacity=0), run_time=0.3)
