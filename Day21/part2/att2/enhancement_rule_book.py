from enhancement_rule import enhancement_rule
class enhancement_rule_book:
    def __init__(self, rules):
        self.rules = []
        for idx, rule in enumerate(rules):
            self.rules.append(enhancement_rule(rule[0], rule[1]))

    def get_output(self, input_grid):
        for idx, rule in enumerate(self.rules):
            if rule.does_match(input_grid):
                return rule.get_output_grid()
        raise Exception("Bad input {}".format(input_grid))


