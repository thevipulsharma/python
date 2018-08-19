def search_for_vowels(phrase:str, letters:str='aeiou') -> set:
    return set(letters).intersection(set(phrase))