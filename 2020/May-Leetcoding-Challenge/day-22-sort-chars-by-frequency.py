class Solution:
    def frequencySort(self, s: str) -> str:
        from collections import Counter


        c = Counter(s)

        print(c)

        ans = ""

        for i in sorted(c,key=c.get,reverse = True):
            ans += i*c[i]

        return ans