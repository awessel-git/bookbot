from stats import count_words, count_characters

def get_book_text(filepath):
    with open(filepath) as f:
        book_text = f.read()
        return book_text
    
def main():
    frankenstein_text = get_book_text("books/frankenstein.txt")
    print(frankenstein_text)
    words_count = count_words(frankenstein_text)
    print(f"{words_count} words found in the document")
    characters_count = count_characters(frankenstein_text)
    print(characters_count)

main()