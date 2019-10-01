import abc  # Python's built-in abstract class library

# Person class
class Person(object):
    def __init__(self,credit_score,state):
        self.credit_score = credit_score
        self.state = state

# Product class
class Product(object):
    def __init__(self,name,interest_rate=5.0,disqualified=False):
        self.name=name
        self.interest_rate = interest_rate
        self.disqualified = disqualified

# Abstract rule class; all rule classes are derived from this class
class RuleAbstract(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self, condition_input, condition_action, rule_description):
        self.condition_input = condition_input
        self.condition_action = condition_action
        self.rule_description = rule_description
        super().__init__()

    @abc.abstractmethod
    def evaluate(self, person, product):
        """Required Method"""

class PenalizeLowCreditScoreRule(RuleAbstract):
    def evaluate(self, person, product):
        if ((isinstance(person.credit_score, int) == False) or (isinstance(self.condition_input, int) == False)):
            return
        if (person.credit_score < self.condition_input):
            product.interest_rate+=self.condition_action
            print(self.rule_description)
        return

class RewardHighCreditScoreRule(RuleAbstract):
    def evaluate(self, person, product):
        if ((isinstance(person.credit_score, int) == False) or (isinstance(self.condition_input, int) == False)):
            return
        if (person.credit_score >= self.condition_input):
            product.interest_rate-=self.condition_action
            print(self.rule_description)
        return

class DisqualifySpecificStateRule(RuleAbstract):
    def evaluate(self, person, product):
        if ((isinstance(person.state, str) == False) or (isinstance(self.condition_input, str) == False)):
            return
        if (person.state == self.condition_input):
            product.disqualified=True
            print(self.rule_description)
        return

class UpdateInitialRateRule(RuleAbstract):
    def evaluate(self, person, product):
        if ((isinstance(product.name, str) == False) or (isinstance(self.condition_input, str) == False)):
            return
        if (product.name == self.condition_input):
            product.interest_rate+=self.condition_action
            print(self.rule_description)
        return

# rule engine definition
class RulesEngine(object):

    def add_rule(self,rule_type,rule_input,rule_action,rule_description):
        rule = None
        if(rule_type == 0):
            try:
                int(rule_input)
            except ValueError:
                return rule
            rule_input=int(rule_input)

            try:
                float(rule_action)
            except ValueError:
                return rule
            rule_action=float(rule_action)

            rule = PenalizeLowCreditScoreRule(rule_input,rule_action,rule_description)

        elif(rule_type == 1):
            try:
                int(rule_input)
            except ValueError:
                return rule
            rule_input=int(rule_input)

            try:
                float(rule_action)
            except ValueError:
                return rule
            rule_action=float(rule_action)

            rule = RewardHighCreditScoreRule(rule_input,rule_action,rule_description)

        elif(rule_type == 2):
            rule = DisqualifySpecificStateRule(rule_input,rule_action,rule_description)

        elif(rule_type == 3):

            try:
                float(rule_action)
            except ValueError:
                return rule
            rule_action=float(rule_action)

            rule = UpdateInitialRateRule(rule_input,rule_action,rule_description)

        return rule

    def run_rules(self,person,product,rules):
        for rule in rules:
            current_rule = self.add_rule(rule.rule_type,rule.rule_input,rule.rule_action,rule.rule_description)
            if current_rule:
                current_rule.evaluate(person, product)

# rule data object class: created to hold rule data as rules are read from external source
class Rule(object):
    def __init__(self,rule_type,rule_input,rule_action,rule_description):
        self.rule_type =rule_type
        self.rule_input = rule_input
        self.rule_action = rule_action
        self.rule_description = rule_description


"""
TESTING
"""

# read rules line by line from file; assume csv input with columns mapping to rule inputs
def loadRules():
    rules = []

    rule_file = open("Rule_definitions.txt", "r")
    for current_line in rule_file:
        current_line_word_list = current_line.split(',')
        rules.append(Rule(int(current_line_word_list[0]),current_line_word_list[1],current_line_word_list[2],current_line_word_list[3]))
    rule_file.close()

    return rules

rules = loadRules()
rules_engine = RulesEngine()


# Test 1: run rules on provided input
person = Person(720,"Florida")
product = Product("7-1 ARM")
print("Credit score = " + str(person.credit_score) + "; state = " + person.state)
print("Product = " + product.name)
rules_engine.run_rules(person,product,rules)
print("Final interest rate is "+ str(product.interest_rate))
print("Product disqualified is "+ str(product.disqualified)+"\n")

# Test 2: run rules on custom input
person = Person(720,"Georgia")
product = Product("7-1 ARM")
print("Credit score = " + str(person.credit_score) + "; state = " + person.state)
print("Product = " + product.name)
rules_engine.run_rules(person,product,rules)
print("Final interest rate is "+ str(product.interest_rate))
print("Product disqualified is "+ str(product.disqualified)+"\n")

# Test 3: run rules on custom input; trigger added rule
person = Person(719,"Florida")
product = Product("5-1 ARM")
print("Credit score = " + str(person.credit_score) + "; state = " + person.state)
print("Product = " + product.name)
rules_engine.run_rules(person,product,rules)
print("Final interest rate is "+ str(product.interest_rate))
print("Product disqualified is "+ str(product.disqualified)+"\n")







