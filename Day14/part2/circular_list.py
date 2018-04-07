class circular_list:
        def __init__(self, size):
            self.list = []
            idx = 0
            while(idx < size):
                self.list.append(idx)
                idx += 1

        def get_list(self):
            return self.list



        def perform_looped_hask_knot(self,lengths, iterations):
            start_index = 0
            skip_size = 0
            idx = 0
            while(idx < iterations):
                return_variables = self.hash_knot(lengths,start_index,skip_size)
                start_index = return_variables[0]
                skip_size = return_variables[1]
                idx += 1

        def create_dense_hash(self):
            indexes = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
            sparse_hases = []
            count = 0
            while(count < 16):
                block =(self.list[indexes[0]] ^ self.list[indexes[1]] ^ self.list[indexes[2]] ^ self.list[indexes[3]]
                         ^ self.list[indexes[4]] ^ self.list[indexes[5]] ^ self.list[indexes[6]]
                         ^ self.list[indexes[7]] ^ self.list[indexes[8]] ^ self.list[indexes[9]]
                         ^ self.list[indexes[10]] ^ self.list[indexes[11]] ^ self.list[indexes[12]]
                         ^ self.list[indexes[13]] ^ self.list[indexes[14]] ^ self.list[indexes[15]])
                sparse_hases.append(block)
                count += 1
                for idx, item in enumerate(indexes):
                    indexes[idx]+= 16

            return sparse_hases



        def hash_knot(self, lengths, start_index, skip_size):
            for idx, length in enumerate(lengths):
                self.reverse_subsection(start_index, length)
                start_index = length + skip_size + start_index
                skip_size += 1
                if (start_index >= len(self.list)):
                    minus_mult = int((start_index / (len(self.list))))
                    start_index = start_index - (len(self.list) * minus_mult)
            return [start_index,skip_size]




        def reverse_subsection(self,start_index,length):
            reversed_section = self.get_subsection_in_reverse(start_index, length)
            #print(reversed_section)
            if(not reversed_section == False):
                count = 0
                idx = start_index
                while(count < length):
                    self.list[idx] = reversed_section[count]
                    idx += 1
                    if(idx == len(self.list)):
                        idx = 0
                    count +=1



        def get_subsection_in_reverse(self, start_index, length):
            if(length > len(self.list)):
                return False
            else:
                sub_section = []
                count = 0
                idx = start_index
                while(count < length):
                    #print(self.list[idx])
                    sub_section.append(self.list[idx])
                    idx += 1
                    if(idx == len(self.list)):
                        idx = 0
                    count +=1
                sub_section.reverse()
                return sub_section



