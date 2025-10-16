def get_book_text (path):
    with open(path) as f:
        return f.read()

def get_caracters_count (text) :
    char_dictionary ={}
    text_lowercase = text.lower()
    charachters = list(text_lowercase)        
    for  charachter in charachters:
        char_dictionary[charachter] = char_dictionary.get(charachter,0) +1

    return char_dictionary
