def catcher(lst, index, value):
    if index >= len(lst):
        raise IndexError("Dont try buffer overflow attacks in python")
    lst[index] = value 
        
        
catcher([1,2],3,4)