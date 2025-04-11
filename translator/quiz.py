import random
from grammar.declension import decline_noun

def start_declension_quiz(nouns: dict):
    """
    Runs a declension quiz for 1st/2nd declension nouns.
    Prompts user to give the correct declined form of a word. 
    """
    print("Latin Declension Quiz - Chapter 1")
    print("Type 'exit' to quit the quiz.\n")

    cases = ["nominative", "accusative"]
    numbers = ["singular", "plural"]
    words = list(nouns.items())
    random.shuffle(words)  # Shuffle the words for randomness

    for word, entry in words:
        if not entry["declension"]:
            continue

        case = random.choice(cases)
        number = random.choice(numbers)

        try:
            correct = decline_noun(entry, case, number)
        except ValueError:
            continue

        print(f"What is the {case} {number} form of '{word}'?  ({entry['meaning']})")
        answer = input("Your answer: ").strip()

        if answer.lower() == "exit":
            break
        elif answer == correct:
            print("Correct!")
        else:
            print(f"Wrong! The correct answer is '{correct}'.")