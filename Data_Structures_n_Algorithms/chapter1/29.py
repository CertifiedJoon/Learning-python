def RecPermute(rest, so_far):
    if (rest == ''):
        print(so_far)
    for i in range (len(rest)):
        nexti = so_far + rest[i]
        remainging = rest[:i] + rest[i+1:]
        RecPermute(remainging, nexti)
        
def Permute(s):
    RecPermute(s, str())
    
Permute('catdog')