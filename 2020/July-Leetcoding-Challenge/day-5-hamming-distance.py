class Solution:
    def hammingDistance(self, x: int, y: int) -> int:

        x_bin = bin(x)[2:]

        y_bin = bin(y)[2:]

        # print(x_bin,y_bin)

        diff = abs(len(y_bin) - len(x_bin))

        # print(diff)

        if(len(x_bin) < len(y_bin)):
            x_bin = '0'*diff + x_bin

        else:
            y_bin = '0'*diff + y_bin

        # print(x_bin,y_bin)

        ans = 0

        for i in range(len(x_bin)):
            ans += int(x_bin[i]) ^ int(y_bin[i])

        return(ans)  