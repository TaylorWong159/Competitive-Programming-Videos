from typing import Callable

from manim import *

class PrecomputeScene(Scene):
    def construct(self) -> None:
        array = [2, 4, 1, 7, 3, 5, 8]
        box_size = 0.8
        boxes = VGroup(*[
            Square(side_length=box_size)
                .set_fill(WHITE, opacity=0.125)
                .set_stroke(WHITE, width=2)
                .move_to((box_size * i - box_size * ((len(array) - 1) // 2), 2.9, 0))
            for i in range(len(array))
        ])
        numbers = VGroup(*[
            Text(str(array[i]), font_size=36).move_to(boxes[i])
            for i in range(len(array))
        ])
        indices = VGroup(*[
            Text(str(i), font_size=24)
                .next_to(boxes[i], UP)
            for i in range(len(array))
        ])

        table = VGroup(
            *[
                Square(side_length=box_size)
                    .set_fill(WHITE, opacity=0.125)
                    .set_stroke(WHITE, width=2)
                    .move_to((
                        box_size * j - box_size * ((len(array) - 1) // 2),
                        box_size * (len(array) - i - 2) - 2.75,
                        0
                    ))
                for i in range(len(array))
                for j in range(len(array))
            ]
        )
        table_col_indices = VGroup(*[
            Text(str(j), font_size=24)
                .next_to(table[j], UP)
            for j in range(len(array))
        ])
        table_row_indices = VGroup(*[
            Text(str(i), font_size=24)
                .next_to(table[i * len(array)], LEFT)
            for i in range(len(array))
        ])

        # Animate the array
        self.play(Create(boxes))
        self.play(Write(numbers))
        self.play(Write(indices))

        self.wait(2)

        self.play(Create(table))
        self.play(Write(table_col_indices))
        self.play(Write(table_row_indices))

        self.wait(1)

        # Fill in the table
        instant_fill = VGroup()
        for i in range(len(array)):
            for j in range(i, len(array)):
                if i < 2:
                    if i == j:
                        sum_value = array[i]
                        sum_text = Text(str(sum_value), font_size=24) \
                            .move_to(table[i * len(array) + j].get_center())
                        original_stroke = boxes[i].get_stroke_width()
                        original_color = boxes[i].get_stroke_color()
                        self.play(
                            boxes[i].animate.set_stroke(color=WHITE, width=6),
                            run_time=0.6
                        )
                        self.play(Write(sum_text), run_time=0.6)
                        self.play(
                            boxes[i].animate.set_stroke(original_color, width=original_stroke),
                            run_time=0.6
                        )
                    else:
                        sum_value = sum(array[i:j + 1])
                        sum_text = Text(str(sum_value), font_size=24) \
                            .move_to(table[i * len(array) + j].get_center())
                        original_stroke_1 = boxes[j].get_stroke_width()
                        original_color_1 = boxes[j].get_stroke_color()
                        original_color_2 = table[i * len(array) + j - 1].get_stroke_color()
                        original_stroke_2 = table[i * len(array) + j - 1].get_stroke_width()
                        self.play(
                            boxes[j].animate.set_stroke(color=WHITE, width=6),
                            table[i * len(array) + j - 1].animate.set_stroke(color=WHITE, width=6),
                            run_time=0.6
                        )
                        self.play(Write(sum_text), run_time=0.6)
                        self.play(
                            boxes[j].animate.set_stroke(original_color_1, width=original_stroke_1),
                            table[i * len(array) + j - 1].animate.set_stroke(original_color_2, width=original_stroke_2),
                            run_time=0.6
                        )
                    self.wait(0.5)
                else:
                    sum_value = sum(array[i:j + 1])
                    sum_text = Text(str(sum_value), font_size=24) \
                        .move_to(table[i * len(array) + j].get_center())
                    # self.play(Write(sum_text), run_time=0.15)
                    instant_fill.add(sum_text)
        self.play(Write(instant_fill), run_time=2)
        self.wait(1)


