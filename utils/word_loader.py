import csv
from collections import defaultdict

def load_words(filepath):
    words_by_type = defaultdict(dict)

    with open(filepath, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            word_type = row["type"]
            word = row["word"]
            entry = {
                "base": row["base"],
                "meaning": row["meaning"],
                "declension": int(row["declension"]) if row["declension"] else None,
                "conjugation": int(row["conjugation"]) if row["conjugation"] else None,
                "gender": row["gender"],
                "person": row["pos"],
                "number": row["number"],
                "notes": row["notes"], 
            }
            words_by_type[word_type][word] = entry

    return words_by_type