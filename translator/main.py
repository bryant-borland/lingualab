import json
from grammar.declension import decline_noun

# Load dictionary
with open("data/latin_dict.json") as f:
    latin_dict = json.load(f)

# Choose a word to test
noun_entry = latin_dict["puella"] 

# Choose the case and number
case = "accusative"
number = "plural"

# Decline it using the dispatcher
form = decline_noun(noun_entry, case, number)

print(f"The {case} {number} form of '{noun_entry['base']}' is: {form}")