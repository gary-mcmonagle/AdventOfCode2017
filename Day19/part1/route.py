class route:
    def __init__(self, routing_diagram):
        self.routing_diagram = routing_diagram
        self.packet_location = self.get_origin()
        self.letters = ""
        #D0 U1 L2 R3
        self.direction=0

    def get_origin(self):
        for idx, node in enumerate(self.routing_diagram[0]):
            if(node == "|"):
                return [0,idx]
    def is_change_charachter(self):
        if(self.routing_diagram[self.packet_location[0]][self.packet_location[1]] == "+"):
            return 1
        elif(self.routing_diagram[self.packet_location[0]][self.packet_location[1]] == " "):
            return 2
        else:
            return 0

    def get_char_at_location(self,location):
        return self.routing_diagram[location[0]][location[1]]

    def send_packet(self):
        is_sent = False
        while(not is_sent):
            is_sent = self.move_in_one_direcrtion()
        return self.letters

    def get_direction(self):
        return self.direction

    def move_in_one_direcrtion(self):
        if(self.direction == 0):
            axis,ab = 0,1
        if(self.direction == 1):
            axis,ab = 0,-1
        if(self.direction == 2):
            axis,ab = 1,-1
        if(self.direction == 3):
            axis,ab = 1,1
        while (self.is_change_charachter() == 0):
            if(self.get_char_at_location(self.packet_location).isalpha()):
                self.letters += self.get_char_at_location(self.packet_location)
            self.packet_location[axis] += ab
        if(self.is_change_charachter() == 1):
            self.change_direction()
        if(self.is_change_charachter() == 2):
            print(self.letters)
            exit()


    def change_direction(self):
        if(self.direction < 2):
            if(self.packet_location[1] == 0):
                print("Turning Right")
                self.direction = 3
                self.packet_location[1] += 1
            elif(self.packet_location[1] == (len(self.routing_diagram[self.packet_location[0]])-1)):
                print("Turning Left")
                self.direction = 2
                self.packet_location[1] -= 1
            else:
                if(not self.routing_diagram[self.packet_location[0]][self.packet_location[1]+1] == " "):
                    print("Turning Right")
                    self.direction = 3
                    self.packet_location[1] += 1
                else:
                    print("Turning Left")
                    self.direction = 2
                    self.packet_location[1] -= 1
        else:
            if(self.packet_location[0] == 0):
                print("Turning Down")
                self.direction = 0
                self.packet_location[0] += 1
            elif(self.packet_location[0] == len(self.routing_diagram)-1):
                print("Turning Up")
                self.direction = 1
                self.packet_location[0] -= 1
            else:
                if(not self.routing_diagram[self.packet_location[0]+1][self.packet_location[1]] == " "):
                    print("Turning Down")
                    self.direction = 0
                    self.packet_location[0] += 1
                else:
                    print("Turning Up")
                    self.direction = 1
                    self.packet_location[0] -= 1


    def get_packet_location(self):
        return self.packet_location

