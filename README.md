# Rules_Engine_Example

This project includes an implementation of a simple rule engine that determines whether a person qualifies for a given product and sets an interest rate for the person based on predefined rules. The rulebase is designed to be easily updated, with rules defined and implemented separately from the code that executes them.

The code can be run fron the command line using the command **python RulesEngine.py**. The rules are declared as rows in a csv file with the columns defined as follows:
- 1: rule index (unique identifier)
- 2: rule condition input (value of property that triggers rule)
- 3: rule action (adjustment made to a specific property when rule fires)
- 4: rule description (text description of rule)
