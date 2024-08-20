from manim import *
from manim_slides import Slide

from util import text, coordinates

class AnimationB(Slide):
    def __init__(self):
        super().__init__()
        self.title = "Example (1)"

    RECT_COLOR=RED
    CURSOR_COLOR=GREEN
    CURSOR_WIDTH=0.5
    CURSOR_HEIGHT=0.6

    def create_cursor(self, render):
        cursor = Rectangle(stroke_width=0, fill_opacity=0.6, fill_color=self.CURSOR_COLOR, width=self.CURSOR_WIDTH, height=self.CURSOR_HEIGHT)
        render.add(cursor)

        return cursor

    def create_cover(self, render, width, height, x, y):
        cover = Rectangle(stroke_width=0, color=BLUE, fill_opacity=1.0, fill_color=WHITE, width=width, height=height).move_to(np.array([x, y, 0]))
        render.add(cover)
        
        return cover

    def construct(self, render):
        img = ImageMobject("images/TrieJoin.png")
        render.add(img)

        cover_135 = self.create_cover(render, 1.5, 1.8, 4.6, 1.55)
        cover_35 = self.create_cover(render, 1.0, 2.9, 3.8, -0.85)
        cover_3 = self.create_cover(render, 0.6, 1.5, 3.75, -1.6)
        cover_2 = self.create_cover(render, 1.0, 2.9, 5.8, 0.5)
        cover_928 = self.create_cover(render, 1.2, 3.0, 4.9, -0.85)

        render.wait()
        render.next_slide()

        render.wait(0.5)

        rect_left = Rectangle(color=self.RECT_COLOR, width=0.1, height=0.1).move_to(np.array([-4.1, 1.1, -1.0]))
        render.add(rect_left)
       
        rect_left_x = Rectangle(color=self.RECT_COLOR, width=2.8, height=0.6).move_to(np.array([-4, -0.15, 0]))

        render.play(Transform(rect_left, rect_left_x))

        render.wait(0.5)

        cursor_left_x = self.create_cursor(render).move_to(np.array([-5, -0.15, 0]))
        render.play(FadeIn(cursor_left_x))

        render.wait(0.5)

        render.play(FadeOut(cover_135))

        render.wait(0.5)

        rect_right = Rectangle(color=self.RECT_COLOR, width=0.1, height=0.1).move_to(np.array([-0.1, 1.1, -1.0]))
        render.add(rect_right)

        rect_left_y = Rectangle(color=self.RECT_COLOR, width=2.2, height=0.6).move_to(np.array([-5, -1.65, 0]))
        rect_right_y = Rectangle(color=self.RECT_COLOR, width=2.8, height=0.6).move_to(np.array([-0.1, -0.15, 0]))

        render.play(
            Transform(rect_left, rect_left_y),
            Transform(rect_right, rect_right_y)
        )

        render.wait(0.5)

        cursor_left_y = self.create_cursor(render).move_to(np.array([-5.65, -1.65, 0]))
        cursor_right_y = self.create_cursor(render).move_to(np.array([-1.0, -0.15, 0]))
        
        # render.play(
        #     FadeIn(cursor_left_y), 
        #     cursor_right_y.animate.move_to(np.array([-0.15, -0.15, 0]))
        # )       
        
        # render.wait(0.5)

        # render.play(FadeOut(cover_35))

        # render.wait(0.5)

        # rect_right_z = Rectangle(color=self.RECT_COLOR, width=0.55, height=0.6).move_to(np.array([-0.15, -1.65, 0]))
      
        # render.play(
        #     Transform(rect_right, rect_right_z),
        #     FadeOut(cover_3)
        # )

        # render.wait(0.5)

        # render.play(
        #     Transform(rect_right, rect_right_y)
        # )

        # render.wait(0.5)

        # render.play(
        #     cursor_left_y.animate.move_to(np.array([-4.35, -1.65, 0])),
        #     cursor_right_y.animate.move_to(np.array([0.85, -0.15, 0]))
        # )

        # render.wait(0.5)

        # render.play(FadeOut(cover_928))

        # render.wait(0.5)

        # rect_right_start = Rectangle(stroke_width=0, color=self.RECT_COLOR, width=0.1, height=0.1).move_to(np.array([-0.1, 1.1, -1.0]))
        # render.play(
        #     Transform(rect_right, rect_right_start),
        #     Transform(rect_left, rect_left_x),
        #     FadeOut(cursor_right_y),
        #     FadeOut(cursor_left_y)
        # )

        # render.wait(0.5)

        # render.play(
        #     cursor_left_x.animate.move_to([-3, -0.15, 0])
        # )

        # render.wait(0.5)

        # rect_left_y_2 = Rectangle(color=self.RECT_COLOR, width=2.2, height=0.6).move_to(np.array([-3, -1.65, 0]))
        # render.play(
        #     Transform(rect_left, rect_left_y_2),
        #     Transform(rect_right, rect_right_y)
        # )

        # render.wait(0.5)

        # render.play(FadeOut(cover_2))

        render.wait()