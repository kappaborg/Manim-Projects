from manim import *

class Sun(Sphere):
    def __init__(self, **kwargs):
        super().__init__(radius=1, **kwargs)
        self.set_color(YELLOW)
        self.set_gloss(1)  # Make it appear glowing
        self.set_opacity(0.8)  # Slight transparency for a glowing effect
