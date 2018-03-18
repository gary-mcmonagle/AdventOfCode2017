class stream_parser:
    def __init__(self, stream):
        self.garbage_count = 0
        self.stream = stream
        self.filer_garbage()

    def filer_garbage(self):
        is_clean = False
        while(not is_clean):
            is_clean = self.filter_garbage_element()

    def get_garbage_count(self):
        return self.garbage_count

    def filter_garbage_element(self):
        try:
            start_index = self.stream.index("<")
        except:
            return True
        iterator = start_index
        to_ignore = False
        while(iterator < len(self.stream)):
            if(self.stream[iterator-1] == "!"):
                if(to_ignore):
                    to_ignore = False
                else:
                    to_ignore = True
            else:
                to_ignore = False
            if(not to_ignore):
                if(self.stream[iterator] == ">"):
                    self.garbage_count += self.count_garbage_chars(self.stream[start_index:iterator+1])
                    #print(self.stream[start_index:iterator+1])
                    self.stream = self.stream[0:start_index]+self.stream[iterator+1:]
                    return False
            iterator += 1

    def get_stream(self):
        return self.stream
    def count_garbage_chars(self,garbage_string):
        to_ignore = False
        count = -2
        for idx,char in enumerate(garbage_string):
            if(garbage_string[idx-1] == "!"):
                if (to_ignore):
                    to_ignore = False
                else:
                    to_ignore = True
            else:
                to_ignore = False

            if(not to_ignore):
                if(not garbage_string[idx] == "!"):
                    count +=1
        return count







