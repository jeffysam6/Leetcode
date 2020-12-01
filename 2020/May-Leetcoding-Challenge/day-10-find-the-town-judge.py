class Solution:
    def findJudge(self, n: int, arr: List[List[int]]) -> int:
        from collections import defaultdict
        
        d = defaultdict(list)

        for i in arr:

            d[i[0]].append(i[1])


        head = -1
        for i in range(1,n+1):
            if(i not in d):
                head = i
        
        if(head == -1):
            return head

        # print(d,head)

        for i in d:

            if(head not in d[i]):
                return -1

        return head
