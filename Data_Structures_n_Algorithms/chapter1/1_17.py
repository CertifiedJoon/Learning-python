def scale(data, factor):
    for val in data:
        val *= factor
print('Bad scaling')        
data = [1,2,3,4,5]; print (data)
scale(data, 5); print (data)

def realscale(data, factor):
    #data*=factor #This will concatenate the array with itself multiple times!  
    for i in range (len(data)):
        data[i]*=factor

print ('\nGood scaling')
data = [1,2,3,4,5]; print (data)
realscale(data, 5); print (data)