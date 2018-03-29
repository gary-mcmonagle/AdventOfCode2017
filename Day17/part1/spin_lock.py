class spin_lock:
    def __init__(self,step_size):
        self.lock = [0]
        self.current_position = 0
        self.step_size = step_size


    def get_lock(self):
        return self.lock
    def insert_value(self, value):
        i = 0
        while(i<self.step_size):
            self.current_position += 1
            if(self.current_position == len(self.lock)):
                self.current_position = 0
            i+=1

        self.lock.insert(self.current_position+1,value)
        self.current_position += 1
        try:
            return self.lock[0]
        except:
            return None