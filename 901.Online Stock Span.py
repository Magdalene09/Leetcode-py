class StockSpanner:

    def __init__(self): 
        self.stack = []
        self.index = 0
        

    def next(self, price: int) -> int:
        while self.stack and self.stack[-1][1] <= price :
            self.stack.pop()

        prevGreaterEle = self.stack[-1][0] if self.stack else -1 
        consecutiveDays = self.index - prevGreaterEle
        self.stack.append((self.index,price))
        self.index += 1

        return consecutiveDays

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
