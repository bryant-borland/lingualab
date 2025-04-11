from utils.word_loader import load_words
from translator.quiz import start_declension_quiz # adjust path if needed

def main():
    words = load_words("data/chapter_01_words.csv")
    nouns = words["noun"]

    print("Welcome to LinguaLab!")
    print("1. Start declension quiz")
    print("2. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        start_declension_quiz(nouns)
    else:
        print("Goodbye!")

if __name__ == "__main__":
    main()