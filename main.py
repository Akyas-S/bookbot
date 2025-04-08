#imports
from stats import find_num_words
from stats import char_count

def get_book_text(path):
    with open(path) as f:
        contents = f.read()
        return contents
    
def main():
    path = "/home/eksudee/workspaces/github.com/Akyas-S/bookbot/books/frankenstein.txt"
    # reads the book
    contents = get_book_text(path)

    num_words = find_num_words(contents)
    num_char = char_count(contents)

    print(f"{num_words} words found in the document")
    print (num_char)
    

main()

