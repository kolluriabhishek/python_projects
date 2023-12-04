def lengthOfLongestSubstring(self, s: str) -> int:
    c = 1
    maxc = 0
    if (len(s) == 0):
        return 0
    for i in range(1, len(s)):
        if (s[i] not in s[i - c:i]):
            c = c + 1
            if (maxc < c):
                maxc = c
                print(s[i],end='----')
                print(s[i-c:i],end='----')
                print(maxc)
        else:
            c = 1
    if (maxc == 0):
        maxc = 1
    return maxc
lengthOfLongestSubstring("dvdf")