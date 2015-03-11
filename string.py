def suffix_array(string):
    """ Takes a string as input and returns its suffix array"""
    suffixes=[]
    suffix_array=[]
    for i in range(len(string)-1):
        suffixes.append(string[i:])
    
    for i in sorted(suffixes):
        suffix_array.append(suffixes.index(i))
    return suffix_array


class KnuthMorrisPratt():
    def computeShifts(pattern):
        shifts = [None] * (len(pattern) + 1)
        shift = 1
        for pos in range(len(pattern) + 1):
            while shift < pos and pattern[pos-1] != pattern[pos-shift-1]:
                shift += shifts[pos-shift-1]
            shifts[pos] = shift
        return shifts

    def kmpAllMatches(pattern, text):
        shift = computeShifts(pattern)
        startPos = 0
        matchLen = 0
        for c in text:
            while matchLen >= 0 and pattern[matchLen] != c:
                startPos += shift[matchLen]
                matchLen -= shift[matchLen]
            matchLen += 1
            if matchLen == len(pattern):
                yield startPos
                startPos += shift[matchLen]
                matchLen -= shift[matchLen]

