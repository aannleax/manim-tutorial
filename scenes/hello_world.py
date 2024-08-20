from manim import *
from manim_slides import Slide

from util import text, coordinates

class HelloWorld(Slide):
    def __init__(self):
        super().__init__()
        self.title = None


    def construct(self, render):
        black = Rectangle(color=BLACK, fill_color=BLACK, fill_opacity=1.0, height=render.camera.frame_height, width=render.camera.frame_width)
        render.add(black)

        circle = Circle() 
        circle.set_fill(PINK, opacity=0.5) 
        render.play(Create(circle))

        render.wait()