def findSubstring(s):
    P = s
    N = len(s)
    s = dict()
    for i in range(N):
        freq = [False]*26
        k = ""
 
        for j in range(i,N):
            pos = ord(P[j]) - ord('a')
            if (freq[pos] == True):
                break
 
            freq[pos] = True
            k += P[j]
            s[k] = 1
 
    return len(s)
 
print(findSubstring("abba"))