from manim import *
import numpy as np

class StarryBackground(VGroup):  # Inherit from VGroup instead of ThreeDScene
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        # Create stars
        for _ in range(100):
            x = np.random.uniform(-10, 10)
            y = np.random.uniform(-10, 10)
            star = Dot(np.array([x, y, 0]), color=WHITE, radius=0.05)
            self.add(star)
        
        # Add a galactic center (a bright star)
        galactic_center = Dot(np.array([0, 0, 0]), color=YELLOW, radius=0.1)
        self.add(galactic_center)
