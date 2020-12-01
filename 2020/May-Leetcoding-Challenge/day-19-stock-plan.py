class StockSpanner:

    def __init__(self):
        self.stocks = []
        

    def next(self, price: int) -> int:
        c = 1
        if(self.stocks):
            index = len(self.stocks) - 1
            while(index >-1 and self.stocks[index][0] <= price):
                c += self.stocks[index][1]
                self.stocks.pop()
                index -= 1
        
        self.stocks.append((price,c))
        
        return c


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)