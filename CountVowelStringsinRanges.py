import re

def isVowel(c):
    return c == 'u' or c == 'e' or c == 'o' or c == 'a' or c == 'i'

def vowelStrings(words, queries):
    ans = []
    l = [0] * (len(words) + 1)

    for i in range(1, len(l)):
        l[i] = l[i - 1] + (isVowel(words[i - 1][0]) and isVowel(words[i - 1][len(words[i - 1]) - 1]))


    for i in queries:
        first = i[0]
        second = i[1]
        ans.append(l[second + 1] - l[first])
    return ans


words = ["a","e","i"]
queries = [[0,2],[0,1],[2,2]]
print(vowelStrings(words, queries))
