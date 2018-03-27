import copy
class dance_troup:
    def __init__(self):
        self.init_troup = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p"]
        self.troup = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p"]

    def get_move_set(self):
        return self.move_set

    def reset_troup(self):
        self.troup = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p"]
        #lself.init_troup = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p"]

    def apply_move_set(self):
        list = []
        for idx , move in enumerate(self.move_set):
            list.append(self.troup[move[1]])
        self.troup = list

    def create_move_set(self):
        moves = []
        print(self.troup)
        print(self.init_troup)
        for idx, move in enumerate(self.troup):
            for i_idx, i in enumerate(self.init_troup):
                if(move == i):
                    moves.append([idx,i_idx])
        self.move_set = moves
        self.init_troup = self.troup[:]
        print(self.init_troup)

    def dance(self,move):
        if(move.startswith("s")):
            self.spin(move)
        if(move.startswith("x")):
            self.exchange(move)
        if(move.startswith("p")):
            self.partner(move)

    def spin(self,move):
        move = self.format_move(move)
        head = self.troup[0:(len(self.troup)-int(move))]
        tail = self.troup[len(self.troup)-int(move):len(self.troup)]
        self.troup = tail+head

    def exchange(self,move):
        move = self.format_move(move)
        num_1 = self.troup[int(move[0])]
        num_2 = self.troup[int(move[1])]
        self.troup[int(move[0])] = num_2
        self.troup[int(move[1])] = num_1

    def get_letter_index(self,letter):
        idx = 0
        while(True):
            if(self.troup[idx] == letter):
                return idx
            idx += 1

    def get_troup(self):
        return self.troup

    def partner(self,move):
        move = self.format_move(move)
        idx_1 = self.get_letter_index(move[0])
        idx_2 = self.get_letter_index(move[1])
        num_1 = self.troup[idx_1]
        num_2 = self.troup[idx_2]
        self.troup[idx_1] = num_2
        self.troup[idx_2] = num_1
        return self.troup

    def format_move(self,move):
        if "/" in move:
            return move[1:].split("/")
        else:
            return move[1:]

