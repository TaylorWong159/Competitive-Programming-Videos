from manim import *

class BruteForce(Scene):

    def construct(self) -> None:
        title = Text('Brute Force', font_size=56)

        # Show Title
        self.wait(4)
        self.play(Create(title))
        self.wait(1)

        # Transition into definition
        self.play(title.animate.move_to((0, 3, 0)))
        definition = Text(
            'Try all possible "solutions" until a "valid" solution is found',
            font_size=24,
        ).next_to(title, DOWN)
        self.play(Create(definition))
        self.wait(1)
