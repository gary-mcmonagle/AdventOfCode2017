from layer import layer
class firewall:
    layers = []
    packet_index = -1
    severity = 0

    def add_layer(self,firewall_layer):
        self.layers.append(layer(firewall_layer))

    def move_layers_scanners(self):
        for idx, layer in enumerate(self.layers):
            layer.move_snanner()

    def move_pincosecond(self):
        self.packet_index += 1
        if(self.layers[self.packet_index].get_scanner_index() == 0):
            self.severity += (self.layers[self.packet_index].get_depth() * self.layers[self.packet_index].get_layer_range())
        self.move_layers_scanners()

    def get_layers(self):
        return self.layers

    def move_packet_through_firewall(self):
        idx = 0
        while(idx < len(self.layers)):
            self.move_pincosecond()
            idx += 1

    def get_severity(self):
        return self.severity