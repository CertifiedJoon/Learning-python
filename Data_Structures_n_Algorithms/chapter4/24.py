class Puzzle:
    def __init__(self, first, second, result): # takes three strings as input
        self._letters = [c for c in first] + [c for c in second] + [c for c in result] # stores all three sgrings into one list
        self._map = {k : -1 for k in self._letters}
        self._len1 = len(first)
        self._len2 = len(second)
        self._len3 = len(result)

        
    def _ltoi(self, lst): #converts a list to integer
        ret = 0
        for i in lst:
            ret = ret * 10 + int(i)
        return ret
    
    def assign_letter(self, letter, num): #assigns a 'num'
        if (num in self._map.values()):
            return False
        self._map[letter] = num
        
        return True
        
    def unassign_letter(self, letter):
        self._map[letter] = -1
        
    def is_solved(self):
        temp = [k for k in range(len(self._letters))]
        for i in range (len(self._letters)):
            temp[i] = self._map[self._letters[i]]
        print(temp)
        if (self._ltoi(temp[:self._len1]) + self._ltoi(temp[self._len1:self._len1+self._len2])) == self._ltoi(temp[self._len1+self._len2:]):
            self._letters = temp
            return True
        return False

    def print_letters(self):
        print(self._letters[:self._len1])
        print(self._letters[self._len1:self._len1+self._len2])
        print(self._letters[self._len1+self._len2:])
    
def Cryptarithmetic(p, letters_to_assign):
    if (letters_to_assign == ''):
        if (p.is_solved()):
            return True
        return False
    
    for i in range (1, 10):
        if p.assign_letter(letters_to_assign[0], i):
            if (Cryptarithmetic(p, letters_to_assign[1:])):
                return True
            else:
                p.unassign_letter(letters_to_assign[0])
    return False

p = Puzzle('dog', 'cat', 'pig')
Cryptarithmetic(p, 'dogcatpi')
p.print_letters()