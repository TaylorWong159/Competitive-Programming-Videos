from manim import *

class PrecomputeScene(Scene):
    def construct(self) -> None:
        array = [2, 4, 1, 7, 3, 5, 8]
        box_size = 0.8
        boxes = VGroup(*[
            Square(side_length=box_size)
                .set_fill(WHITE, opacity=0.125)
                .set_stroke(WHITE, width=2)
                .move_to((box_size * i - box_size * ((len(array) - 1) // 2), 3, 0))
            for i in range(len(array))
        ])
        numbers = VGroup(*[
            Text(str(array[i]), font_size=36)
                .move_to(boxes[i].get_center())
            for i in range(len(array))
        ])
        indices = VGroup(*[
            Text(str(i), font_size=24)
                .move_to((boxes[i].get_center()[0], boxes[i].get_center()[1] - box_size, 0))
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
        table_row_indices = VGroup(*[
            Text(str(i), font_size=24)
                .move_to((
                    -box_size * ((len(array) + 1) // 2),
                    box_size * (len(array) - i - 2) - 2.75,
                    0
                ))
            for i in range(len(array))
        ])

        # Animate the array
        self.play(Create(boxes))
        self.play(Write(numbers))
        self.play(Write(indices))

        self.wait(2)

        self.play(Create(table))
        self.play(Write(table_row_indices))

        self.wait(1)

        # Fill in the table
        for i in range(len(array)):
            for j in range(i, len(array)):
                sum_value = sum(array[i:j+1])
                sum_text = Text(str(sum_value), font_size=24) \
                    .move_to(table[i * len(array) + j].get_center())
                self.play(Write(sum_text), run_time=0.3)

        self.wait(1)


