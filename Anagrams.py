first = input()
second = input()

def is_anagram(first, second):
    if len(first) != len(second):
        return False
    l1 = [x for x in first]
    l2 = [x for x in second]

    l1.sort()
    l2.sort()

    for i in range(len(l1)):
        if l1[i] != l2[i]:
            return False
    return True

print(int(is_anagram(first, second)))