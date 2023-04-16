class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def middleNode(head):
    # While slow moves one step forward, fast moves two steps forward.
    # Finally, when fast reaches the end, slow happens to be in the middle of the linked list.
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

def printList(head):
    while head:
        print(head.val)
        head = head.next


if __name__ == "__main__":


    # print(l[0: 3])
    # head = ListNode(1, next=None)
    # second = ListNode(2, next=None)
    # third = ListNode(3, next=None)
    # head.next = second
    # second.next = third
    # printList(middleNode(head))

    # mat = [[1, 2], [3, 4]]
    #
    # arr = []
    # col = []
    #
    # j = 0
    # for u in range(len(mat)):
    #     for v in range(len(mat[u])):
    #         col.append(mat[u][v])
    #         j += 1
    #         if j == 2:
    #             arr.append(col)
    #             col = []
    #             j = 0
    # print(arr)

    x = 1
    y = 0
    z = 1
    t = 4

    if x//3 == z//3 and y // 3 == t // 3:
        print(False)
    else:
        print(True)








