def FindPair(nums, k, sofar = []):
    if not nums or len(sofar) == 2:
        if sum(sofar) == k:
            print (sofar)
        return
    
    FindPair(nums[1:], k, sofar)
    FindPair(nums[1:], k, sofar + [nums[0],])
    
lst = [2,7,9,10,13,14]
FindPair(lst, 16)