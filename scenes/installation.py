from manim import *
from manim_slides import Slide

from util import text, coordinates

class Installation(Slide):
    def __init__(self):
        super().__init__()
        self.title = "Installation"


    def construct(self, render):
        text_linux = text.tex("Install dependencies on Linux:").next_to(coordinates.UPPER_LEFT, RIGHT).shift(0.25*DOWN)
        render.add(text_linux)

        dependency_linux = Code(code=r"""
sudo apt install build-essential python3-dev libcairo2-dev libpango1.0-dev ffmpeg
""", language="sh", font_size=160).next_to(text_linux, DOWN).set_x(0)
        render.add(dependency_linux)

        text_macos = text.tex("Install dependencies on MacOS:").next_to(dependency_linux, DOWN, buff=0.5).align_to(text_linux, LEFT)
        render.add(text_macos)

        dependency_macos = Code(code=r"""
brew install py3cairo ffmpeg
brew install pango pkg-config scipy
""", language="sh", font_size=160).next_to(text_macos, DOWN).set_x(0)
        render.add(dependency_macos)

        text_manim_slides = text.tex("Install manim-slides:").next_to(dependency_macos, DOWN, buff=0.5).align_to(text_linux, LEFT)
        render.add(text_manim_slides)

        install_slides = Code(code=r"""
pip install manim-slides[manim]
""", language="sh", font_size=160).next_to(text_manim_slides, DOWN).set_x(0)
        render.add(install_slides)

        render.wait()