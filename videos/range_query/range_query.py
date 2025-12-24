from manim import *

class RangeQuery(Scene):

    def problem_statement(self) -> None:
        array = [2, 4, 1, 7, 3, 5, 9, 6, 8, 0, 1]
        box_size = 1.0
        boxes = VGroup(*[
            Square(side_length=box_size) \
                .set_fill(WHITE, opacity=0.125) \
                .set_stroke(WHITE, width=2) \
                .move_to((box_size * i - box_size * len(array) // 2, 3, 0))
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

        range_start = 2
        range_end = 7
        assert 0 <= range_start <= range_end < len(array)
        range_text = Text(f'[{range_start}, {range_end}]', font_size=36) \
            .move_to((0, 1, 0))


        # Animate the array
        self.play(Create(boxes))
        self.play(Write(numbers))
        self.play(Write(indices))

        self.wait(2)

        # Write range
        self.play(Write(range_text))

        self.wait(1)

        # Highlight range
        self.play(*[
            boxes[i].animate.set_fill(BLUE, opacity=0.5)
            for i in range(range_start, range_end + 1)
        ])

        self.wait(4)

        # Animate range sum query
        sum_value = 0
        sum_text_label = Text('Sum = ', font_size=36).move_to((-0.5, 0, 0))
        sum_text = Text(f'{sum_value}', font_size=36).next_to(sum_text_label, RIGHT)
        self.play(Write(sum_text_label), Write(sum_text))
        for i in range(range_start, range_end + 1):
            original_stroke = boxes[i].get_stroke_width()
            self.play(boxes[i].animate.set_stroke(WHITE, width=6), run_time=0.5)
            self.wait(1)
            sum_value += array[i]
            self.play(sum_text.animate.become(
                Text(f'{sum_value}', font_size=36).next_to(sum_text_label, RIGHT)
            ))
            self.play(boxes[i].animate.set_stroke(WHITE, width=original_stroke), run_time=0.5)

        self.wait(8)
        self.clear()

    def naive_approach(self) -> None:
        ...

    def precomputed_sums(self) -> None:
        ...

    def prefix_sums(self) -> None:
        ...

    def construct(self) -> None:
        self.problem_statement()
        # self.wait()
        # self.naive_approach()
        # self.wait()
        # self.precomputed_sums()
        # self.wait()
        # self.prefix_sums()
        # self.wait()

