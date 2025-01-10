from manim import *

class Planet(Sphere):
    def __init__(self, radius=0.3, color=BLUE, distance=3, **kwargs):
        super().__init__(radius=radius, **kwargs)
        self.set_color(color)
        self.distance = distance  # Distance from the Sun
        self.orbit_path = Circle(radius=distance, color=GRAY, stroke_width=1).rotate(PI/2)  # Orbit circle

    def add_orbit(self, scene):
        scene.add(self.orbit_path)  # Add the orbit to the scene
