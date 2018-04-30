from enhancement_rule import enhancement_rule
class enhancement_rule_book:
    def __init__(self, rules):
        self.enhacement_rules = []
        for idx, rule in enumerate(rules):
            self.enhacement_rules.append(enhancement_rule(rule[0],rule[1]))

    def get_rule_book(self):
        return self.enhacement_rules

    def get_grid_transform(self, input_keys):
        for r_idx, rule in enumerate(self.enhacement_rules):
            for k_idx, key in enumerate(input_keys):
                if rule.match(key):
                    return rule.get_output()
        raise Exception("Not found")

