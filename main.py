def get_book_text(path):
    with open(path) as f:
        contents = f.read()
        return contents
    
def find_words(contents):

    pass


def main():
    path = "/home/eksudee/workspaces/github.com/Akyas-S/bookbot/books/frankenstein.txt"

    contents = get_book_text(path)

    print(contents)



main()

