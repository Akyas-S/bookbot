#imports
from stats import find_num_words
from stats import char_count
from stats import sort_char_count
import argparse
import sys

def get_book_text(path):
    with open(path) as f:
        contents = f.read()
        return contents
    
def main():
    
    path = sys.argv[1]
    contents = get_book_text(path)

    num_words = find_num_words(contents)

    num_char = char_count(contents)
 
    sorted_num_char = sort_char_count(num_char)

    # sylized print
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for key, value in sorted_num_char:
        print(f"{key}: {value}")
    print("============= END ===============")

    
if len(sys.argv) < 2 or len(sys.argv) > 2:
    print('Usage: python3 main.py <path_to_book>')
    (sys.exit(1))
else:
    main()