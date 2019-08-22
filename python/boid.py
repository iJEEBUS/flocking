"""
A boid is what creates a flock.
Each one contains a position and velocity.

Logic to handle position changes are handled in the get_position()
and get_velocity()
"""
import math

class Boid:
    def __init__(self, x_vel, y_vel, x_pos, y_pos):
        self.perception = 5
        self.x_velocity = int(x_vel)
        self.y_velocity = int(y_vel)
        self.x_position = int(x_pos)
        self.y_position = int(y_pos)

    def move(self, flock):
        # execute rules to find velocities
        x_vel_1, y_vel_1 = self.rule_one(flock)
        x_vel_2, y_vel_2 = self.rule_two(flock)
        x_vel_3, y_vel_3 = self.rule_three(flock)

        # add new velocities to current velocities
        self.x_velocity = self.x_velocity + x_vel_1 + x_vel_2 + x_vel_3
        self.y_velocity = self.y_velocity + y_vel_1 + y_vel_2 + y_vel_3

        # limit the velocity of the boid
        self.limit_velocity()

        # move the boids
        self.x_position += self.x_velocity
        self.y_position += self.y_velocity

    def euclidean_distance(self, boid):
        distance = abs(((boid.x_position-self.x_position)**2)-((boid.y_position-self.y_position)**2))**0.5
        return int(distance)


    def limit_velocity(self):
        """Limits boid velocity

        If the boid is going to fast then the velocity needs
        to be lowered to stay within the flock.
        """
        v_limit = 2

        if abs(self.x_velocity) > v_limit:
            self.x_velocity = int((self.x_velocity / abs(self.x_velocity)) * v_limit)
        if abs(self.y_velocity) > v_limit:
            self.y_velocity = int((self.y_velocity / abs(self.y_velocity)) * v_limit)

    def rule_one(self, flock):
        """Center of mass

        Each boid tries to fly towards the CoM of the neighboring boids
        """
        # center of mass values
        x_com = 0
        y_com = 0

        # find the center of mass of the entire flock
        for b in flock:
            if b is not self:
                x_com += b.x_position
                y_com += b.y_position
        x_com /= (len(flock)-1)
        y_com /= (len(flock)-1)

        # move the boid 1% of the way towards the center of mass
        x_vel = (x_com - self.x_position) / 100
        y_vel = (y_com - self.y_position) / 100
        return int(x_vel), int(y_vel)

    def rule_two(self, flock):
        """Avoidance

        Boids need to keep a small distance away from other boids.
        """
        x_vel = 0
        y_vel = 0
        distance = 0
        for b in flock:
            if b is not self:
                distance = self.euclidean_distance(b)
                if distance <= self.perception:
                    x_vel -= (b.x_position - self.x_position)
                    y_vel -= (b.y_position - self.x_position)
        return x_vel, y_vel

    def rule_three(self, flock):
        """Cohesion

        Each boid attempts to move to the average position of the nearby boids
        """
        x_vel = 0
        y_vel = 0

        for b in flock:
            if b is not self:
                x_vel += b.x_velocity
                y_vel += b.y_velocity

        x_vel /= (len(flock)-1)
        y_vel /= (len(flock)-1)

        x_vel = (x_vel - self.x_velocity) / 8
        y_vel = (y_vel - self.y_velocity) / 8
        return int(x_vel), int(y_vel)

    def set_position(self, x, y):
        self.x_position = x
        self.y_position = y

    def get_position(self):
        return (self.x_position, self.y_position)

    def get_velocity(self):
        return (self.x_velocity, self.y_velocity)
