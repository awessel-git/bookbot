from stats import count_words, count_characters, sort_characters

def get_book_text(filepath):
    with open(filepath) as f:
        book_text = f.read()
        return book_text
    
def main():
    filepath = "books/frankenstein.txt"
    frankenstein_text = get_book_text(filepath)
    words_count = count_words(frankenstein_text)
    characters_count = count_characters(frankenstein_text)
    sorted_characters = sort_characters(characters_count)

    print("------ BOOKBOT ------")
    print(f"Analyzing book found at {filepath}...")
    print("////// Word Count //////")
    print(f"Found {words_count} total words")
    print("****** Character Count ******")
    for item in sorted_characters:
        print(f"{item["char"]}: {item["count"]}")
    print("^^^^^^ END ^^^^^^")

main()