def count_words(book_text):
    return len(book_text.split())

def count_characters(book_text):
    characters = {}
    for letter in book_text:
        lowercase_letter = letter.lower()
        if lowercase_letter in characters:
            characters[lowercase_letter] += 1
        else:
            characters[lowercase_letter] = 1
    return characters

def sort_characters(characters):
    sorted_characters = []
    for k, v in characters.items():
        if k.isalpha():
            new_entry = {}
            new_entry["char"] = k
            new_entry["count"] = v
            sorted_characters.append(new_entry)
    sorted_characters.sort(reverse=True, key=sort_on)
    return sorted_characters

def sort_on(items):
    return items["count"]