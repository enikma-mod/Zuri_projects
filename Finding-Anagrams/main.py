
# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True
from collections import Counter

# Name: Karabo Modika

def find_anagram(word, anagram):
    # [assignment] Add your code here
    if(Counter(word) == Counter(anagram)):
        return True
    else:
        return False


print(find_anagram("hello", "check"))
print(find_anagram("below", "elbow"))
print(find_anagram("good", "nice"))
print(find_anagram("run", "urn"))
print(find_anagram("brush", "shrub"))
