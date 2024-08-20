from manim import *
from manim_slides import Slide

from util import text, coordinates

class Outline(Slide):
    def __init__(self):
        super().__init__()
        self.title = "Outline"

    def static(self, render, position):
        my_text = text.tex(r"Some text with math: ${a \over b} = c$").next_to(coordinates.UPPER_LEFT)
      
        flowers = ImageMobject(
            "images/flowers.png"
        ).scale_to_fit_height(3).next_to(
            my_text, DOWN, aligned_edge=LEFT, buff=1.0
        ).shift(RIGHT)
      
        buildings= ImageMobject(
            "images/buildings.jpg"
        ).scale_to_fit_height(3).next_to(flowers, RIGHT).set_x(-flowers.get_x())
      
        group = Group(my_text, flowers, buildings).scale_to_fit_width(4.25).next_to(position, DOWN, buff=2.0)
        render.add(group)

        box = Rectangle(width=5, height=3, color=BLACK).move_to(group)
        render.add(box)

    

    def animated(self, render, position):
        circle = Circle(fill_color=RED, fill_opacity=1.0).move_to(4*LEFT)
        triangle = Triangle(color=GREEN)
        rectangle = Rectangle(width=2.0, height=2.0, color=BLUE).move_to(4*RIGHT)

        group = VGroup(circle, triangle, rectangle).scale_to_fit_width(4.25).next_to(position, DOWN, buff=3.0)
        render.add(group)

        box = Rectangle(width=5, height=3, color=BLACK).move_to(group).shift(0.5*UP)
        render.add(box)

        render.wait()
        render.next_slide(loop=True)

        render.play(circle.animate.set_fill(BLUE))
        render.play(triangle.animate.shift(1*UP), run_time=2.0)
        render.play(rectangle.animate.scale(1.5))

    def construct(self, render):
        part_a = text.tex("Part 1", font_size=46).next_to(2.5*UP, LEFT, buff=3.0)
        part_b = text.tex("Part 2", font_size=46).next_to(2.5*UP, RIGHT, buff=3.0)
        render.add(part_a)
        render.add(part_b)

        self.static(render, part_a)
        self.animated(render, part_b)

        render.wait()