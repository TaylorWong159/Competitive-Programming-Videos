from manim import *

from intro import IntroductionScene
from problem import ProblemStatement
from precompute import PrecomputeScene

class RangeQuery(Scene):

    def construct(self) -> None:
        IntroductionScene.construct(self)
        self.wait(2)
        self.clear()
        ProblemStatement.construct(self)
        self.wait(2)
        self.clear()
        PrecomputeScene.construct(self)
        self.wait(2)
