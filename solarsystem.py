from manim import *
from sun import Sun
from mercury import Mercury
from jupiter import Jupiter
from venus import Venus
from planet import Planet

class SolarSystem(VGroup):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Add the Sun
        sun = Sun()
        self.add(sun)

        mercury = Mercury()
        self.add(mercury)

        jupiter = Jupiter()
        self.add(jupiter)

        venus = Venus()
        self.add(venus)

        # Add planets
        planets = [
            Planet(radius=0.1, color=RED, distance=2),  # Mercury
            Planet(radius=0.2, color=ORANGE, distance=3),  # Venus
            Planet(radius=0.25, color=BLUE, distance=4),  # Earth
            Planet(radius=0.2, color=RED_B, distance=5),  # Mars
            Planet(radius=0.5, color=YELLOW, distance=7),  # Jupiter
            Planet(radius=0.4, color=LIGHT_BROWN, distance=9),  # Saturn
            Planet(radius=0.3, color=TEAL, distance=11),  # Uranus
            Planet(radius=0.35, color=PURPLE, distance=13),  # Neptune
        ]

        for planet in planets:
            self.add(planet)
            planet.add_orbit(self)
