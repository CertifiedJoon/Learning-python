import os 

def walk(path):
    for name in os.listdir(path):
        dirpath = os.path.join(path, name)
        if os.path.isdir(dirpath):
            dirnames = list()
            filenames = list()
            for sub_name in os.listdir(dirpath):
                if os.path.isdir(os.path.join(dirpath, sub_name)):
                    dirnames.append(sub_name)
                else: 
                    filenames.append(sub_name)
            yield dirpath, dirnames, filenames
            
print([c for c in walk('/workspace/Learning-python')])