class gpu:

    def __init__(self, particles):
        self.particles = particles
        self.closest_to_origin = 0

    def tick_particles(self):
        for idx,particle in enumerate(self.particles):
            particle.tick()
            if(particle.get_distance_from_origin() < self.particles[self.closest_to_origin].get_distance_from_origin()):
                self.closest_to_origin = idx

    def get_remaining_particles(self):
        return len(self.particles)

    def paricles_colide(self, particle1,particle2):
        p1pos = particle1.get_position()
        p2pos = particle2.get_position()
        return p1pos[0] == p2pos[0] and p1pos[1] == p2pos[1] and p1pos[2] == p2pos[2]

    def remove_colided_particles(self):
        i = 0
        while i < len(self.particles):
            if not self.find_single_particle_colisions(i):
                i -= 1
            i += 1


    def find_single_particle_colisions(self,particle_index):
        i = particle_index+1
        colisions = []
        while i < len(self.particles):
            #print("{} {}".format(particle_index,i))
            if(self.paricles_colide(self.particles[particle_index], self.particles[i])):
                if(len(colisions) == 0):
                    colisions.append(particle_index)
                colisions.append(i)
            i+=1

        for idx, colision in enumerate(colisions):
            print("removing {}".format(colision-idx))
            self.particles.pop(colision-idx)
        #print(len(colisions) == 0)
        return len(colisions) == 0

    def get_closest_to_origin(self):
        return self.closest_to_origin