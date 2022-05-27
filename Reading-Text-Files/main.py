# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

#Author : Karabo Modika

def read_file_content(filename):
    file = open("Reading-Text-Files/story.txt")
    return file.read()


def count_words():
    text = read_file_content("./story.txt")
    listed_text = text.split()

    text_occurences = {}
    for word in range(len(listed_text)):
        text_occurences[listed_text[word]] = listed_text.count(listed_text[word])
    return text_occurences

print(count_words())
