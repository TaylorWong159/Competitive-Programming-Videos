from manim import *

class RangeQuery(Scene):

    def init(self) -> None:
        self.circle = Circle(radius=1, color=BLUE)
        self.square = Square(side_length=2, color=RED)
        self.triangle = Triangle(color=GREEN)
        self.circle2 = Circle(radius=1, color=BLUE)


    def construct(self) -> None:
        # Initialize variables
        self.init()

        # Animate Scene
        self.add(self.circle)
        self.play(ReplacementTransform(self.circle, self.square))
        self.wait(0.5)
        self.play(ReplacementTransform(self.square, self.triangle))
        self.wait(0.5)
        self.play(ReplacementTransform(self.triangle, self.circle2))
        self.wait(0.5)