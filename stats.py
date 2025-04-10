#splits content, iterates through to find word count 
def find_num_words(contents):  
    words = contents.split()
    counter = 0
    for word in words:
        counter += 1   
    return counter

# lwr case text, creates new dict, adds new char to dic, if char already exist + 1
def char_count(contents):
    lwr_case_contents = contents.lower()
    char_dict = {}
    
    for char in lwr_case_contents:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

# decending order
def sort_char_count(dict):

    sorted_list = sorted(dict.items(), key= lambda x: x[1], reverse=True)
    return sorted_list
