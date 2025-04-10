"""
declension.py

Contains functions for declining Latin nouns based on their grammatical case,
number (singular/plural), and declension class (1st or 2nd, currently supported).

This module uses dictionary-based noun entries that include:
- base: the noun stem (e.g., 'puell' for 'puella')
- declension: integer (1 or 2)
- gender: 'm', 'f', or 'n'

Supported cases:
- nominative: subject of the sentence (e.g., 'puella' → "the girl")
- accusative: direct object (e.g., 'puellam' → "the girl" being acted upon)
- genitive: possession (e.g., 'puellae' → "of the girl")
- dative: indirect object (e.g., 'puellae' → "to/for the girl")
- ablative: means, manner, or separation (e.g., 'puella' → "by/with/from the girl")

Note: Vocative and locative cases are not yet implemented.
"""


def decline_noun(noun_data: dict, case: str, number: str) -> str:
    """
    Dispatcher function to decline any Latin noun using the correct declension logic.
    """
    decl = noun_data["declension"]
    base = noun_data["base"]
    gender = noun_data.get("gender", "f") # defualt to 'f' if not provided

    if decl == 1:
        return decline_first_declension(base, case, number)
    elif decl == 2:
        return decline_second_declension(base, case, number, gender)
    else:
        raise ValueError(f"Unsupported declension: {decl}")

# For 1st declension feminine nouns
def decline_first_declension(base: str, case: str, number: str) -> str:
    """
    Declines a 1st declension Latin noun based on grammatical case and number.

    Parameters:
    - base (str): The stem of the noun (e.g., 'puell' for 'puella')
    - case (str): The grammatical case ('nominative', 'accusative', ect.)
    - number (str): Either 'singular' or 'plural'

    Returns:
    - str: The fully declined noun (e.g., 'puellam', 'puellae')

    Raises:
    - ValueError: If the case or number is not supported.

    Notes: 
    - This function supports 1st declension nouns only, which typically end in '-a' in the nominative singular.
    - Gender is not considered, as 1st declension nouns follow the same endings regardless of gender.

    """
    endings = {
        "nominative": {"singular": "a", "plural": "ae"},
        "accusative": {"singular": "am", "plural": "as"},
    }

    if case not in endings or number not in endings[case]:
        raise ValueError(f"Unsupported case/number combo: {case}, {number}")
    # Combine the base with the correct case/number ending
    return base + endings[case][number]

# for 2nd declension masculine and neuter nouns
def decline_second_declension(base, case, number, gender):
    """
    Declines a 2nd declension Latin noun based on case, number, and gender.

    Parameters:
    - base (str): The stem of the noun (e.g., 'serv' for 'servus', 'bell' for 'bellum')
    - case (str): The grammatical case ('nominative', 'accusative', etc.)
    - number (str): Either 'singular' or 'plural'
    - gender (str): 'm' for masculine, 'n' for neuter

    Returns:
    - str: The fully declined noun (e.g., 'servus', 'bellum', 'servōs', 'bella')

    Raises:
    - ValueError: If the case, number, or gender is unsupported.
    """
    if gender == "m":
        endings = {
            "nominative": {"singular": "us", "plural": "ī"},
            "accusative": {"singular": "um", "plural": "ōs"},
        }
    else: # neuter
        endings = {
            "nominative": {"singular": "um", "plural": "a"},
            "accusative": {"singular": "um", "plural": "a"},
        }

    if case not in endings or number not in endings[case]:
        raise ValueError(f"Unsupoorted case/number combo: {case}, {number}")
    
    return base + endings[case][number]