from manim import *
from background import StarryBackground
from solarsystem import SolarSystem

class FullAnimation(ThreeDScene):
    def construct(self):
        # Set the initial 3D camera orientation
        self.set_camera_orientation(phi=75 * DEGREES, theta=45 * DEGREES)

        # Create the starry background
        starry_background = StarryBackground()
        self.add(starry_background)  # Add the background to the scene

        # Create the Solar System
        solar_system = SolarSystem()
        self.add(solar_system)  # Add the solar system to the scene

        # Begin ambient camera rotation
        self.begin_ambient_camera_rotation(rate=0.1)

        # Move the camera to observe the Solar System
        self.move_camera(phi=60 * DEGREES, theta=90 * DEGREES, run_time=3)

        # Add animations for planet rotations
        planets = solar_system[1:]  # Exclude the Sun
        for planet in planets:
            self.play(Rotate(planet, angle=TAU, about_point=ORIGIN, run_time=10), run_time=10, rate_func=linear)

        self.wait(5)
