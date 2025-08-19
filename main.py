from stats import count_words, count_characters, sort_characters
import sys


def get_book_text(filepath):
    with open(filepath) as f:
        book_text = f.read()
        return book_text


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]

    try:
        book_text = get_book_text(filepath)
        words_count = count_words(book_text)
        characters_count = count_characters(book_text)
        sorted_characters = sort_characters(characters_count)
        print_report(filepath, words_count, sorted_characters)
    except FileNotFoundError:
        print("Couldn't find the book. Try again with the correct filepath and remember the file extension, e.g., 'python3 main.py books/crime_and_punishment.txt'")


def print_report(filepath, words_count, sorted_characters):
    print("------ BOOKBOT ------")
    print(f"Analyzing book found at {filepath}...")
    print("////// Word Count //////")
    print(f"Found {words_count} total words")
    print("****** Character Count ******")
    for item in sorted_characters:
        print(f"{item["char"]}: {item["count"]}")
    print("^^^^^^ END ^^^^^^")


main()
