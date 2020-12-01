class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        


        stack = []
        if(k == len(num)):
            return "0"

        for i in range(len(num)):
            # print(num[i],stack)
            while True:
                if(k == 0 or len(stack) == 0):
                    break

                if(stack[-1] > num[i]):
                    k -= 1
                    stack.pop()

                else:
                    break

            stack.append(num[i])

        # print(stack)
        while(k != 0):
            # print(stack,k)
            stack.pop()
            k -= 1



        return str(int(''.join(stack)))
	    



