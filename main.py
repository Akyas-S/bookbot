def get_book_text(path):
    with open(path) as f:
        contents = f.read()
        return contents
    
def find_words(contents):    
    words = contents.split()
    counter = 0
    for word in words:
        counter += 1   

    return counter


def main():
    path = "/home/eksudee/workspaces/github.com/Akyas-S/bookbot/books/frankenstein.txt"

    contents = get_book_text(path)
    num_words = find_words(contents)

    print(f"{num_words} words found in the document")



main()

