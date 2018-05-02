from component import component
class bridge_maker:
    def __init__(self, component_list):
        self.component_list = []
        self.largest_bridge = 0
        self.longest_bridge = 0
        for idx, com in enumerate(component_list):
            self.component_list.append(component(com[0], com[1]))

    def generate_bridges(self, available_components, required_node, current_size, current_length):
        for idx, com in enumerate(available_components):
            if(not com.does_match(required_node) == False):
                current_length += 1
                new_list = available_components.copy()
                new_list.pop(idx)
                self.generate_bridges(new_list, com.does_match(required_node), current_size+com.get_value(), current_length)
        if(current_length >= self.longest_bridge):
            self.longest_bridge = current_length
            if(current_size > self.largest_bridge):
                self.largest_bridge = current_size

    def get_component_list(self):
        return self.component_list

    def get_largest_bridge(self):
        return self.largest_bridge


