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