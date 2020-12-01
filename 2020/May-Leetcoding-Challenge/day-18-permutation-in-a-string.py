class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter



        s1_count = Counter(s1)

        s1_len = len(s1)

        s2_count = Counter(s2)

        d = Counter()

        for i,val in enumerate(s2):

            d[val] += 1

            if(i >= s1_len):
                d[s2[i-s1_len]] -= 1
                if(d[s2[i-s1_len]] == 0):
                    d.pop(s2[i-s1_len])
            if(d == s1_count):
                return True
                

        return False



