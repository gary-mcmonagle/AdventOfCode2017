from firewall import firewall
from layer import layer
with open('input.txt','r') as f:
    known_layers = f.readlines()
known_layers = [x.strip() for x in known_layers]
layers = []
my_firewall = firewall()
for idx, lay in enumerate(known_layers):
    depth = int(lay.split(":")[0].strip())
    layer_range = int(lay.split(":")[1].strip())
    is_next_layer = False
    while(not is_next_layer):
        if(depth == len(layers)):
            is_next_layer = True
        else:
            my_firewall.add_layer([len(layers)])
            layers.append([len(layers)])
    my_firewall.add_layer([depth,layer_range])
    layers.append([depth,layer_range])


found = False
while(not found):
    found = my_firewall.move_pincosecond()