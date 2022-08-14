# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    
    def dfs(self, l):
        s = ''
        if l.next:
            s = self.dfs(l.next) + str(l.val) 
            return s
        else:
            return str(l.val)
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l1_num = self.dfs(l1)
        l2_num = self.dfs(l2)
        l3_nums = int(l1_num) + int(l2_num)
        l3_sum = str(l3_nums)
        root = None
        for num in l3_sum:
            if not root:
                root = ListNode(num)
            else:
                r2 = ListNode(num, root)
                root = r2
        return root
        
        