from manim import *

class IntroductionScene(Scene):
    def construct(self) -> None:
        title = Text('Range Query Problems', font_size=48).to_edge(UP)
        sections = [
            'General Structure',
            'Prefix Arrays',
            'Square Root Decomposition',
            'Fenwick Trees',
            'Sparse Tables',
            'Segment Trees',
        ]
        section_titles = [Text(f'- {section}', font_size=30) for section in sections]
        for i, section_title in enumerate(section_titles):
            if i == 0:
                section_title \
                    .next_to(title, DOWN, buff=0.5, aligned_edge=LEFT) \
                    .shift(RIGHT * 0.4)
            else:
                section_title \
                    .next_to(section_titles[i - 1], DOWN, buff=0.5, aligned_edge=LEFT)

        self.play(Write(title))
        self.wait(1)
        for section_title in section_titles:
            self.play(Write(section_title))
            self.wait(1)