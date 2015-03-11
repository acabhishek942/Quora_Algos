def suffix_array(string):
    """ Takes a string as input and returns its suffix array"""
    suffixes=[]
    suffix_array=[]
    for i in range(len(string)-1):
        suffixes.append(string[i:])
    
    for i in sorted(suffixes):
        suffix_array.append(suffixes.index(i)
    return suffix_array



