class spin_lock:
    def __init__(self,step_size):
        self.lock = [0]
        self.current_position = 0
        self.step_size = step_size
        self.current_size = 1
        self.first_index = None

    def validate_first_element(self, no):
        is_valid = False
        start_index = self.step_size + self.current_position
        while(not is_valid):
            if(start_index >= self.current_size):
                start_index -= self.current_size
            else:
                start_index += 1
                is_valid = True
                self.current_position = start_index
                self.current_size += 1
                if(start_index == 1):
                    self.first_index = no


    def get_first_index(self):
        return self.first_index
