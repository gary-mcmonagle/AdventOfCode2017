import copy
class debugger:
    memmory_banks = None
    seen_combinations = []
    match_block = []

    def __init__(self, memmory_banks):
        self.memmory_banks = memmory_banks

    def redistribute(self, largest_index):
        self.seen_combinations.append(copy.copy(self.memmory_banks))
        i = self.memmory_banks[largest_index]
        self.memmory_banks[largest_index] = 0
        count_index = largest_index+1
        while(i > 0):
            if(count_index == len(self.memmory_banks)):
                count_index = 0
            self.memmory_banks[count_index] = self.memmory_banks[count_index]+1
            count_index += 1
            i -= 1

    def validate_bank_match(self, bank_1, bank_2):
        for block_index, block in enumerate(bank_1):
            if(not bank_1[block_index] == bank_2[block_index]):
                return False
        return True

    def validate_unique(self):
        for block_index, seen_block in enumerate(self.seen_combinations):
            if((self.validate_bank_match(self.memmory_banks,seen_block))):
                return True
        return False


    def get_largest(self):
        largest = 0
        for current_index, block in enumerate(self.memmory_banks):
            if(self.memmory_banks[current_index] > self.memmory_banks[largest]):
                largest = current_index
        return largest

    def get_next_match(self):
        count = 0
        match = False
        while(not match):
            self.redistribute(self.get_largest())
            count += 1
            if(self.validate_bank_match(self.match_block, self.memmory_banks)):
                match = True
        return count

    def get_needed_redis_for_known(self):
        match = False
        count = 0
        is_init = True
        while(not match):
            print(self.memmory_banks)
            self.redistribute(self.get_largest())
            count += 1
            if(self.validate_unique()):
                print("Known config found!")
                print(self.memmory_banks)
                self.match_block = copy.copy(self.memmory_banks)
                match = True
        return count

    def __getattr__(self, memmory_banks):
        return self.memmory_banks

    def __getattr__(self, seen_combinations):
        return seen_combinations

#de = debugger([0,2,7,0])
de = debugger([11,11,13,7,0,15,5,5,4,4,1,1,7,1,15,11])
de.get_needed_redis_for_known()
print(de.get_next_match())


