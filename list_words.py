import string
import sys


def read_as_list(file_path):
    """
    Opens a file and outputs a list of the words contained in the file.
    The words are converted using the clean function.
    """
    with open(sys.argv[1], 'r', encoding = 'ISO-8859-1') as file:
                
        lines = file.readlines()
        list_of_words = []
        for line in lines:
            for word in line.split():
                clean_word = clean(word)
                list_of_words.append(clean_word)
    return list_of_words

def clean(word):
    """
    Cleans a word: remove punctuation and whitespace and convert to
    lower case.
    """
    return word.lower().strip(string.punctuation + string.whitespace + string.whitespace)

def main():
# Check command line args
    if len(sys.argv) < 2:
        print("No arguments provided.", \
              "Please specifiy the file you want to use.")
        sys.exit()
        
    # Open both text files and convert to list of words
    list1 = read_as_list(sys.argv[1])
    
print(read_as_list(sys.argv[1]))
