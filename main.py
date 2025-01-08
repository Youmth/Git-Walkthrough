import pygame
import pygame.gfxdraw
import random
import math
# Define a Particle class to represent individual particles
class Particle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = random.randint(4, 6)  # Random size between 4 and 6
        self.color = (255, 255, 255)  # White color

        # Random speed in both x and y directions
        angle = random.uniform(-0.25, 0.25) * 3.14  # Random angle between -45 and 45 degrees in radians
        speed = random.uniform(2, 4)  # Random speed magnitude
        self.speed = [speed * math.sin(angle), -speed * math.cos(angle)]

    # Method to move the particle based on its speed
    def move(self):
        self.x += self.speed[0]
        self.y += self.speed[1]

    # Method to apply a force to the particle
    def applyforce(self, mag, dir):
        self.speed[0] += mag * dir[0]
        self.speed[1] += mag * dir[1]

    # Method to draw the particle on the screen
    def draw(self, screen):
        pygame.gfxdraw.aacircle(screen, int(self.x), int(self.y), self.size, self.color)
        pygame.gfxdraw.filled_circle(screen, int(self.x), int(self.y), self.size, self.color)

# Define a Particles class to manage multiple particles
class Particles:
    def __init__(self):
        self.particles = []

    # Method to add a new particle at a given position
    def add_particle(self, x, y):
        self.particles.append(Particle(x, y))

    # Method to update all particles
    def update(self):
        gravity = [0, 1]  # Gravity force
        for particle in self.particles:
            particle.applyforce(0.1, gravity)  # Apply gravity to each particle
        for particle in self.particles:
            particle.move()  # Move each particle

    # Method to draw all particles on the screen
    def draw(self, screen):
        for particle in self.particles:
            particle.draw(screen)

# Define an App class to manage the application
class App:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))  # Set screen size
        pygame.display.set_caption("Particle System")  # Set window title
        self.clock = pygame.time.Clock()  # Create a clock object
        self.particles = Particles()  # Create a Particles object
        self.running = True  # Set running flag to True

    # Method to run the application
    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False  # Exit the loop if the window is closed
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()  # Get mouse position
                    for _ in range(10):
                        self.particles.add_particle(x, y)  # Add 10 particles at the mouse position

            self.screen.fill((0, 0, 0))  # Clear the screen with black color
            self.particles.update()  # Update particles
            self.particles.draw(self.screen)  # Draw particles
            pygame.display.flip()  # Update the display
            self.clock.tick(60)  # Cap the frame rate at 60 FPS

        pygame.quit()  # Quit pygame when the loop ends

# Run the application if this file is executed as a script
if __name__ == "__main__":
    app = App()
    app.run()