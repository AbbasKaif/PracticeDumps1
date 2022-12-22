def findSubstring(s):
    Str = s
    n = len(Str)
    ans = 0
    cnt = 26 * [0]
    i, j = 0, 0
 
    while (i < n):
        if (j < n and (cnt[ord(Str[j]) - ord('a')] == 0)):
            cnt[ord(Str[j]) - ord('a')] += 1
            ans += (j - i + 1)
            j += 1
        else:
 
            cnt[ord(Str[i]) - ord('a')] -= 1
            i += 1
    return ans
 
# Driver code
print(findSubstring("abba"))    