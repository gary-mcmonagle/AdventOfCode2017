class assemb:
    def __init__(self):
        self.value_map = {
            "a": 0,
            "b": 0,
            "c": 0,
            "d": 0,
            "e": 0,
            "f": 0,
            "g": 0,
            "h": 0
        }

    def section_1_2(self):
        self.value_map["b"] = 99
        self.value_map["c"] = self.value_map["b"]
        if( self.value_map["a"] !=  0):
            self.section_5_14(0)
        else:
            self.section_5_14(5)


    def section_5_14(self, entry_point):
        if entry_point == 0:
            self.value_map["b"] = self.value_map["b"]*100
            self.value_map["b"] = self.value_map["b"] - (-100000)
            self.value_map["c"] = self.value_map["b"]
            self.value_map["c"] = self.value_map["c"] - (-17000)
        if entry_point > 4:
            self.value_map["f"] = 1
            self.value_map["d"] = 2
            self.value_map["e"] = 2
            if entry_point > 7:
                self.value_map["g"] = self.value_map["d"]
                if entry_point > 8:
                    self.value_map["g"] = self.value_map["g"] * self.value_map["e"]
                    self.value_map["g"] = self.value_map["g"] - self.value_map["b"]
        if(self.value_map["g"] != 0):
            self.section_16_19(1)
        else:
            self.section_16_19(0)

    def section_16_19(self, entry_point):
        if(entry_point == 0):
            self.value_map["f"] = 0
        self.value_map["e"] = self.value_map["e"]-1
        self.value_map["g"] = self.value_map["e"]
        self.value_map["g"] = self.value_map["g"] - self.value_map["b"]
        if (self.value_map["g"] != 0):
            self.section_5_14(8)
        else:
            self.section_21_23(0)
    def section_21_23(self,entry_point):
        if entry_point == 0:
            self.value_map["d"] = self.value_map["d"] - (-1)
            self.value_map["g"] = self.value_map["d"]
            self.value_map["g"] = self.value_map["g"] - self.value_map["b"]
        if (self.value_map["g"] != 0):
            self.section_5_14(9)
        elif (self.value_map["f"] != 0):
            self.section_26_28(1)
        else: self.section_26_28(0)

    def section_26_28(self, entry_point):
        if entry_point < 1:
            self.value_map["h"] = self.value_map["h"] - (-1)
        self.value_map["g"] = self.value_map["b"]
        self.value_map["g"] = self.value_map["g"] - self.value_map["c"]
        if (self.value_map["g"] != 0):
            self.value_map["e"] = self.value_map["e"] - -17
            self.section_5_14(5)
        else:
            print("Exited")


