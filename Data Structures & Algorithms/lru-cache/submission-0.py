class ListNode:
    def __init__(self,key = 0, val = 0, next = None, prev = None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.dummyFirst = ListNode()
        self.dummyLast = ListNode()
        self.dummyFirst.next = self.dummyLast
        self.dummyLast.prev = self.dummyFirst

    def deleteNode(self, Node):
        prv = Node.prev
        nxt = Node.next
        prv.next = nxt
        nxt.prev = prv

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.deleteNode(node)
            self.insertToLeft(node)  #Left = most recent
            return node.val
        return -1     

    

    def insertToLeft(self,Node):
        prv = self.dummyFirst
        nxt = self.dummyFirst.next
        Node.prev = prv
        Node.next = nxt
        prv.next = Node
        nxt.prev = Node

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            self.deleteNode( node) #delete old node from list
            new_node = ListNode(key, value, None, None)
            self.cache[key] = new_node #replace old node from cache
            self.insertToLeft(new_node) #add new node to list

        else: #not in cache so need to add
            if len(self.cache) >= self.capacity: #if full remove
                lru = self.dummyLast.prev
                self.deleteNode(lru) #deleted node
                del self.cache[lru.key]
            #adding the new node to list and cache
            new_node = ListNode(key, value, None, None)
            self.cache[key] = new_node
            self.insertToLeft(new_node)



        
