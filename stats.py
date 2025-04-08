def find_num_words(contents):    
    words = contents.split()
    counter = 0
    for word in words:
        counter += 1   

    return counter

def char_count(contents):
    lwr_case_cntnt = contents.lower()
    char_dict = {}
    counter = 0
    for char in lwr_case_cntnt:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    #print (char_dict)   
    return char_dict