import os

def FindFile(path, filename):
    if os.path.isdir(path):
        for fd in os.listdir(path):
            childpath = os.path.join(path, fd)
            if (os.path.isdir(childpath)):
                FindFile(childpath, filename)
            elif (fd == filename):
                print(childpath)
                
FindFile('/workspace/Learning-python/Data_Structures_n_Algorithms', '20.py')