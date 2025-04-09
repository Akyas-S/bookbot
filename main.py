#imports
from stats import find_num_words
from stats import char_count
from stats import sort_char_count

def get_book_text(path):
    with open(path) as f:
        contents = f.read()
        return contents
    
def main():
    path = "/home/eksudee/workspaces/github.com/Akyas-S/bookbot/books/frankenstein.txt"

    # reads the book
    contents = get_book_text(path)

    num_words = find_num_words(contents)

    # dict of the number of times each character occurs
    num_char = char_count(contents)

    #n.char sorted by decending order 
    sorted_num_char = sort_char_count(num_char)

    # sylised print
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for key, value in sorted_num_char:
        print(f"{key}: {value}")
    print("============= END ===============")

main()

