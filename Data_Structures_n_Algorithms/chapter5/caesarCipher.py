class CaesarCipher:
    def __init__(self, shift):
        encoder = [None] * 52
        decoder = [None] * 52
        
        alphabets = tuple() # alphabets all of them
        
        for k in range(52):
            encoder[k] = alphabets[(k + shift) % 52]
            decoder[k] = alphabets[(k - shift) % 52]
            
        self._forward = ''.join(encoder)
        self._backward = ''.join(decoder) #efficient construction of string
        
    def encrypt(self, message):
        return self._transform(message, self._forward)
    
    def decrypt(self, secret):
        return self._transform(secret, self._backward)
    
    def transform(self, original, code):
        msg = list(original)
        
        for k in range(len(msg)):
            if msg[k].isupper():
                j = ord(msg[k] - ord('A'))
            elif msg[k].islower():
                j = ord(msg[k] - ord('a'))
            msg[k] = code[k]
            
        return ''.join(msg)
        
class Substitution_Cipher(CaesarCipher):
    def __init__(self, subs, shift):
        encoder = [None] * 26
        decoer = [None] * 26
        
        for k in range(26):
            encoder[k] = subs[(k + shift) % 26]
            decoder[k] = subs[(k - shift) % 26]
            
        self._forward = ''.join(encoder)
        self._backward = ''.join(decoder)
        
class RandomCipher(Substitution_Cipher):
    import random
    def __init__(self, shift):
        rand = [None] * 26
        
        for k in range(26):
            rand[k] = k + ord('A'):
        randdom.shuffle(rand)
        super().__init__(shift, rand)