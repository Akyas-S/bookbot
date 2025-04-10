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
    
def get_input():
    parser = argparse.ArgumentParser(
                    prog='BookBot',
                    description='Parses through books to return the word count and individual character count',
                    epilog='Boot.dev')

    parser.add_argument('filepath', help='Enter the file path to book eg: books/"bookname"')

    args = parser.parse_args()

    return args
    
def main():
    #prints instructions if wrong
    print(get_input())
    
    
    path = sys.argv[1]
    cmplt_path = "/home/eksudee/workspaces/github.com/Akyas-S/bookbot/" + path

    
    contents = get_book_text(cmplt_path)

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

main()

