from stats import get_book_text, get_caracters_count
import sys

def main():

    text = get_book_text(sys.argv[1])
    text_list = text.split()
    word_counter = len(text_list)
    caracters_counts = get_caracters_count(text.replace(" ", ""))
    def resulte ():
        result = ""
        for key, x in sorted(caracters_counts.items(), key =lambda x: x[1], reverse = True):
             result += key + ":" + str(x) + "\n"
        return result

    print(f"============ BOOKBOT ============\nAnalyzing book found at books/frankenstein.txt...\n----------- Word Count ----------\nFound {word_counter} total words\n--------- Character Count -------\n{resulte()}\n============= END ===============")
    

main ()

