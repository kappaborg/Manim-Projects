from manim import *

class Jupiter(Sphere):
    def __init__(self, **kwargs):
        super().__init__(radius=1, **kwargs)
        self.set_color(ORANGE)
        self.set_gloss(1)  # Make it appear glowing
        self.set_opacity(0.7)  # Slight transparency for a glowing effect
