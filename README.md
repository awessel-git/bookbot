# BookBot

BookBot is a small Python program that reads a `.txt` file (like a book) and shows simple stats:

- Total word count
- Most common words
- Letter frequency (a–z)

## How to use

1. Download this project:
   git clone https://github.com/awessel-git/bookbot.git
   cd bookbot

2. Make a folder called `books` **inside the project folder** (next to `main.py`).  
   Put any `.txt` file in there (for example: `frankenstein.txt`).

3. Run the program and point it to your file:
   python main.py books/frankenstein.txt

## Example output

Total words: 74,483

Top 10 words:
1. the - 4,831
2. and - 3,902
...

Letter frequency:
a: 8204
b: 1603
...
