def isIsomorphic(s, t):
    dict1 = dict()
    dict2 = dict()
    for i in range(len(t)):
        if t[i] in dict1:
            a = dict1[t[i]]
            if s[i] != s[a]:
                return False
        else:
            dict1[t[i]] = i
        if s[i] in dict2:
            b = dict2[s[i]]
            if t[i] != t[b]:
                return False
        else:
            dict2[s[i]] = i
    return True


def isSubsequence(s, t):
    if len(s) == 0:
        return True
    j = 0
    for i in range(len(t)):
        if t[i] == s[j]:
            j += 1
        if j == len(s):
            return True
    return False

s = ""
t = "ahbgdc"

print(isSubsequence(s, t))