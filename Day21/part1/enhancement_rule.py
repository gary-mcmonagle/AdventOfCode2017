from collections import deque
class enhancement_rule:
    def __init__(self, rules):
        self.rules = rules

    def get_out_pattern(self, input_pattern):
        possible_solution_patterns = self.get_possible_patterns(input_pattern)
        for idx, sol in enumerate(possible_solution_patterns):
            if(self.check_pattern(input_pattern,sol[0])):
                return sol[1]
        raise Exception("No match found")


    def check_pattern(self, input_pattern, rule):
        for idx, pixel in enumerate(input_pattern):
            test_pattern = deque(list(input_pattern))
            test_pattern.rotate(idx)
            if list(test_pattern) == list(rule):
                return True
        return False

    def get_possible_patterns(self, input_pattern):
        possible_patterns = []
        for idx, rule in enumerate(self.rules):
            if len(input_pattern) == len(rule[0]):
                if input_pattern.count('#') == rule[0].count('#'):
                    possible_patterns.append(rule)
        return possible_patterns

