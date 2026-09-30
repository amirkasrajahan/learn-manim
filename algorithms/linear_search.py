import math

from manim import *


class LinearSearch(Scene):
    def construct(self):
        values = [4, 8, 15, 16, 23, 42]
        target = 23

        leftcells = VGroup(*[
            VGroup(Square(side_length=1), Text(str(values[i]), font_size=36))
            for i in range(int(math.ceil(len(values) / 2)))
        ])

        rightcells = VGroup(*[
            VGroup(Square(side_length=1), Text(str(values[i]), font_size=36))
            for i in range(int(math.ceil(len(values) / 2)), len(values))
        ])

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
