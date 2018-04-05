from particle import particle
from gpu import  gpu
with open("input.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content]
particles = []
for idx, part in enumerate(content):
    vals = ['p', 'v', 'a']
    my_particle = []
    for i in range(0,3):
        start = part.index(vals[i])+3
        end = part.index(">",start)
        props = part[start:end].split(',')
        my_particle.append([int(props[0]),int(props[1]),int(props[2])])
    particles.append(particle(my_particle[0],my_particle[1],my_particle[2]))

my_gpu = gpu(particles)
collision = True
i = 0
while(1 < 100):
    my_gpu.tick_particles()
    collision = my_gpu.remove_colided_particles()
    i += 1
    if(i % 100 == 0):
        print("LEN = {}".format(my_gpu.get_remaining_particles()))
    #print(i)
print(my_gpu.get_closest_to_origin())