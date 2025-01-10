from manim import *

class Mercury(Sphere):
    def __init__(self, **kwargs):
        super().__init__(radius=3, **kwargs)
        self.set_color(GRAY)
        self.set_gloss(1)
        self.set_opacity(0.9)   