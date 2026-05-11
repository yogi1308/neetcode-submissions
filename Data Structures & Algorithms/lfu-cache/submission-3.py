class ListNode:
    def __init__(self, key, value, freq = 1, next = None, prev = None):
        self.key, self.val, self.freq, self.next, self.prev = key, value, freq, next, prev
    

class LFUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.cap = capacity

        self.left = self.right = ListNode(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    def __str__(self):
        curr = self.left.next
        return_str = ""
        if curr and curr.next:
            return_str += f"({curr.key}, {curr.val})"
            curr = curr.next
        return return_str

    def remove(self, node):
        next, prev = node.next, node.prev
        prev.next, next.prev = next, prev

    def insert(self, node):
        prev, next = self.right.prev, self.right
        prev.next = next.prev = node
        node.prev, node.next = prev, next
        
    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            self.cache[key].freq = self.cache[key].freq + 1
            print(self.cache.keys())
            return self.cache[key].val
        print(self.cache.keys())
        return -1

        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            self.cache[key].freq = self.cache[key].freq + 1
            self.cache[key].val = value
            print(self.cache.keys())
            return
        else:
            if len(self.cache) == self.cap:
                lfu_keys = [self.left.next.key]
                min_use = self.left.next.freq
                for keys in self.cache:
                    if self.cache[keys].freq < min_use:
                        min_use = self.cache[keys].freq
                        lfu_keys.append(keys)
                for keys in lfu_keys:
                    if self.cache[keys].freq != min_use:
                        lfu_keys.remove(keys)
                if len(lfu_keys) == 1:
                    self.remove(self.cache[lfu_keys[0]])
                    self.cache.pop(lfu_keys[0])
                else:
                    curr = self.left.next
                    while curr:
                        if curr.key in lfu_keys:
                            self.remove(curr)
                            self.cache.pop(curr.key)
                            break

            node = ListNode(key, value)
            self.insert(node)
            self.cache[key] = node
            print(self.cache.keys())
            return
    


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)