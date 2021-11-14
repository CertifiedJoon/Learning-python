VOWELS = ['a', 'e', 'i', 'o', 'u']

def VowelConsonant(s, index):
    a = -1 if s[index] in VOWELS else 1
    if index == len(s):
        return a
    else:
        return a + VowelConsonant(s, index + 1);