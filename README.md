# BookBot

BookBot is a small Python program that reads a `.txt` file (like a book) and shows simple stats:

- Total word count
- Letter frequency (a–z)

## How to use

1. Download this project:
   git clone https://github.com/awessel-git/bookbot.git
   cd bookbot

2. Create a `books` folder inside the project (next to `main.py`).
   Put any `.txt` file in there (for example: `frankenstein.txt`).

3. Run the program and point it to your file:
   python main.py books/frankenstein.txt

## Example output

------ BOOKBOT ------
Analyzing book found at books/frankenstein.txt...
////// Word Count //////
Found 74483 total words
****** Character Count ******
e: 5000
t: 4000
a: 3500
...
^^^^^^ END ^^^^^^
