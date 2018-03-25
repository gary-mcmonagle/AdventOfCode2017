from layer import layer
from packet import packet
class firewall:
    layers = []
    packets = []
    count = 0
    severity = 0

    def add_layer(self,firewall_layer):
        self.layers.append(layer(firewall_layer))

    def move_layers_scanners(self):
        for idx, layer in enumerate(self.layers):
            layer.move_snanner()

    def move_packets(self):
        #print("Packets length: {}".format(len(self.packets)))
        for idx, packet in enumerate(self.packets):
            packet.set_index(packet.get_index() + 1)

    def catch_packets(self):
        for idx, packet in enumerate(self.packets):
            #print(packet.get_index())
            if(self.layers[packet.get_index()].get_scanner_index() == 0):
                #print("Caught packet {}".format(packet.get_delay()))
                packet.set_caught()

    def check_for_not_caught(self):
        for idx,packet in enumerate(self.packets):
            if(packet.get_index() ==  len(self.layers) -1):
                print(packet.get_delay())
                return True
        return False

    def remove_caught_packets(self):
        is_clean = False
        while(not is_clean):
            remove_index = -1
            for idx, packet in enumerate(self.packets):
                if(packet.get_caught()):
                    remove_index = idx
            if(remove_index == -1):
                is_clean = True
            else:
                #print("removing")
                self.packets.pop(remove_index)
    def move_pincosecond(self):
        #print(self.count)
        self.packets.insert(0,packet(self.count))
        self.move_packets()
        self.catch_packets()
        self.remove_caught_packets()
        self.count += 1
        self.move_layers_scanners()
        return self.check_for_not_caught()





    def get_layers(self):
        return self.layers
