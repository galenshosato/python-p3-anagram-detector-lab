

class Anagram:
    def __init__(self, word):
        self.word = word

    
    def match(self, list):
        arr = [letter for letter in self.word]
        new_arr = []
        for word in list:
            if sorted(arr) == sorted([ltr for ltr in word]):
                new_arr.append(word)
        return new_arr
