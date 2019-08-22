import pygame # for visualization
import random # for boid starting positions/velocities
from boid import Boid

class environment:

    def __init__(self):
        """constructor

        Init a flock of 1000 boids with random velocities and positions
        """
        pygame.init()

    def create_flock(self):

        w, h = pygame.display.get_surface().get_size()

        # create the flock
        num_boids = 3
        self.flock = [None] * num_boids
        for i in range(num_boids):
            x_vel = random.randrange(-1,1)
            y_vel = random.randrange(-1,1)
            x_pos = int(random.random()*w)
            y_pos = int(random.random()*h)
            self.flock[i] = Boid(x_vel, y_vel, x_pos, y_pos)

    def show_flock(self, s):
        screen = s
        background_color = (0,0,0)
        boid_color = (200,200,200)
        radius = 5

    def run(self):
        """ Main entry point into the program.

         Renders the gui
        (Should be able to handle user inputs.)
        Can customize: screen size and flock inputs here
        """
        # Setup of the screen
        background_color = (0,0,0)
        screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        screen.fill(background_color)

        # initalize and show flock
        self.create_flock()

        # Execution of the program.
        running = True
        while running:

            # Logic of the flock here
            screen.fill(background_color)
            self.update(screen)
            pygame.display.update()

            # event handling
            for event in pygame.event.get():
               # exit on pressing the down key
                if event.type == pygame.KEYDOWN:
                    running = False
                if event.type == pygame.MOUSEBUTTONUP:
                    x, y = pygame.mouse.get_pos()
                    self.add_boid(x, y)
                # Quit the game
                if event.type == pygame.QUIT:
                    running = False

    def add_boid(self, x, y):
        """Add a boid

        Adds a boid at the position of the click
        """
        x_vel = random.randrange(-1,1)
        y_vel = random.randrange(-1,1)
        x_pos = x
        y_pos = y
        boid = Boid(x_vel, y_vel, x_pos, y_pos)
        self.flock.append(boid)

    def update(self, screen):
        """
        There are 3 rules to the update function:
         1) Separation - steering to avoid collisions
         2) Alignment - steer to the average direction of local boids
         3) Cohesion - steer to move to the vaerage positon of local boids
        """
        # upate the each boids position and velocity based on its
        # neighbords

        radius = 5
        boid_color = (200, 200, 200)
        background_color = (0,0,0)
        max_x, max_y = pygame.display.get_surface().get_size()

        for b in self.flock:
            x_pos, y_pos = b.get_position()
            pygame.draw.circle(screen, background_color, (x_pos, y_pos), radius)
            b.move(self.flock)

            # Edge detection
            x_pos, y_pos = b.get_position()
            if x_pos >= max_x:
                b.set_position(0, y_pos)
            elif x_pos <= 0:
                b.set_position(max_x, y_pos)
            elif y_pos >= max_y:
                b.set_position(x_pos, 0)
            elif y_pos <= 0:
                b.set_position(x_pos, max_y)


            pygame.draw.circle(screen, boid_color, (x_pos, y_pos), radius)


if __name__ == "__main__":

    # create and run environment
    env = environment()
    env.run()
