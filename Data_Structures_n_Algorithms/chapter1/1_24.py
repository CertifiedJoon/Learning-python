small_vowels = ('a','e','i','o','u')
big_vowels = [chr(ord(k) - 32) for k in small_vowels]
print (big_vowels)
string = input('input  character sequence: ')
print(len([j for j in string if j in small_vowels or j in big_vowels]))