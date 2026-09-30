from manim import *

class BinarySearch(Scene):
    def construct(self):
        values = [1,3,7,12,15,17,19]
        target = 12
        min = 0
        max = len(values) - 1
        mid = max // 2
        minText = Text("Min", font_size=24, color=RED)
        maxText = Text("Max", font_size=24, color=YELLOW)
        midText = Text("Mid", font_size=24, color=GREEN)


        cells = VGroup(*[
            VGroup(Square(side_length=1), Text(str(v), font_size=36))
            for v in values
        ])


        cells.arrange(RIGHT, buff=0.1)
        cells.move_to(ORIGIN)
        self.play(Create(cells))
        self.wait(0.3)

        minText.next_to(cells[min], DOWN)
        maxText.next_to(cells[max], DOWN)
        midText.next_to(cells[mid], DOWN)
        self.play(Create(minText), Create(maxText), Create(midText))

        while values[mid] != target:
            self.wait(2)

            if target < values[mid]:
                max = mid - 1
                mid = (min + max) // 2
            elif target > values[mid]:
                min = mid + 1
                mid = (min + max) // 2

            self.play(
                minText.animate.next_to(cells[min], DOWN),
                maxText.animate.next_to(cells[max], DOWN),
                midText.animate.next_to(cells[mid], DOWN),
            )
        self.play(cells[mid][0].animate.set_fill(GREEN, 0.5), run_time=0.3)

        self.wait(3)

