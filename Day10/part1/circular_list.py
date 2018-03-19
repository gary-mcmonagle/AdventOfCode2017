class circular_list:
        def __init__(self, size):
            self.list = []
            idx = 0
            while(idx < size):
                self.list.append(idx)
                idx += 1
        def get_list(self):
            return self.list



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



