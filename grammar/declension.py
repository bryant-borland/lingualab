# For 1st declension feminine nouns
def decline_first_declension(base, case, number):
    endings = {
        "nominative": {"singular": "a", "plural": "ae"},
        "accusative": {"singular": "am", "plural": "as"},
        # add more cases as you go
    }
    return base + endings[case][number]