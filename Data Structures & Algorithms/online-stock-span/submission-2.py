class StockSpanner:

    def __init__(self):
        self.stack = []
        

    def next(self, price: int) -> int:
        if not self.stack:
            self.stack.append(price)
            return 1
        else:
            count = 1
            curr = -1
            while True:
                if abs(curr) > len(self.stack) or price < self.stack[curr]:
                    self.stack.append(price)
                    return count
                else:
                    curr -= 1
                    count += 1
                

        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)