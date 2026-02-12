# This program checks if two words or phrases are anagrams of each other.
def is_anagram(word1, word2):
    word1 = word1.upper().strip()
    word2 = word2.upper().strip()
    
    word1 = ''.join(word1.split())
    word2 = ''.join(word2.split())

    if len(word1) != len(word2):
        return False

    for ch in word1:
        if word1.count(ch) != word2.count(ch):
            return False
        if not ch in word2:
            return False
    return True

if __name__ == '__main__':

    w1 = input('Word/Phrase 1: ')
    w2 = input('Word/Phrase 2: ')

    if is_anagram(w1, w2):
        print('Anagrams')
    else:
        print('Not anagrams')
        