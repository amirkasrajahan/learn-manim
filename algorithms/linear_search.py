from manim import *


class LinearSearch(Scene):
    def construct(self):
        values = [4, 8, 15, 16, 23, 42]
        target = 23

        title = Text("Linear Search", font_size=40).to_edge(UP)
        target_label = Text(f"target = {target}", font_size=28, color=YELLOW)
        target_label.next_to(title, DOWN, buff=0.3)
        complexity_label = Text("Time Complexity: O(n)", font_size=28)
        complexity_label.to_edge(DOWN)
        self.play(Write(title), Write(target_label), Write(complexity_label))

        cells = VGroup(*[
            VGroup(Square(side_length=1), Text(str(v), font_size=36))
            for v in values
        ])
        cells.arrange(RIGHT, buff=0.15)
        cells.move_to(ORIGIN)
        self.play(Create(cells))
        self.wait(0.3)

        for cell, v in zip(cells, values):
            box = cell[0]
            self.play(box.animate.set_fill(YELLOW, opacity=0.7), run_time=0.4)
            if v == target:
                self.play(box.animate.set_fill(GREEN, opacity=0.8), run_time=0.4)
                self.play(Indicate(cell, scale_factor=1.3))
                break
            self.play(box.animate.set_fill(WHITE, opacity=0), run_time=0.3)

        self.wait(1)
