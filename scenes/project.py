from manim import *
from manim_slides import Slide

from util import text, coordinates

class Project(Slide):
    def __init__(self):
        super().__init__()
        self.title = "Prepared Template"


    def construct(self, render):
        url = text.tex(r"Starting Point: https://github.com/aannleax/manim-template").next_to(coordinates.UPPER_LEFT).shift(0.25*DOWN)
        render.add(url)

        github = ImageMobject("images/github.png").scale_to_fit_height(5).shift(0.25*DOWN)
        render.add(github)

        render.wait()