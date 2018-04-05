class particle:
    def __init__(self,position,velocity,acceleration):
        self.position = position
        self.velocity = velocity
        self.acceleration = acceleration
        self.distance_from_origin = abs(self.position[0]) + abs(self.position[1]) + abs(self.position[2])

    def get_position(self):
        return self.position

    def tick(self):
        self.velocity[0] += self.acceleration[0]
        self.velocity[1] += self.acceleration[1]
        self.velocity[2] += self.acceleration[2]
        self.position[0] += self.velocity[0]
        self.position[1] += self.velocity[1]
        self.position[2] += self.velocity[2]
        self.distance_from_origin = abs(self.position[0]) + abs(self.position[1]) + abs(self.position[2])

    def get_distance_from_origin(self):
        return self.distance_from_origin