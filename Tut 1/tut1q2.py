class ListNode:
    def __init__(self, item):
        self.item = item
        self.next = None

class LinkedList:
    def __init__(self):
        self.size = 0
        self.head = None

    def findNode(self, index):
        if self.head is None:
            raise ValueError("List is empty")
        if index < 0 or index >= self.size:
            raise ValueError("Invalid position")
            
        cur = self.head
        while index > 0:
            cur = cur.next
            index -= 1
        return cur
  
    def insertNode(self, data, index):
        if index < 0 or index > self.size:
            raise ValueError("Invalid position")
            
        new_node = ListNode(data)
        
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            self.size += 1
            return True
        
        prev_node = self.findNode(index - 1)
        if prev_node is not None:
            new_node.next = prev_node.next
            prev_node.next = new_node
            self.size += 1
            return True
        return False

    def removeNode(self, index):
        if index < 0 or index >= self.size:
            raise ValueError("Invalid position")
            
        if self.head is None:
            return False
            
        if index == 0:
            cur = self.head
            self.head = cur.next
            self.size -= 1
            return True
            
        pre = self.findNode(index - 1)
        if pre is not None and pre.next is not None:
            cur = pre.next
            pre.next = cur.next
            self.size -= 1
            return True
        return False

    def printList(self):
        cur = self.head
        if cur is None:
            print("Empty")
            return
        while cur is not None:
            print(cur.item, end=" -> ")
            cur = cur.next
        print("None")

    def removeAllItems(self):
        self.head = None
        self.size = 0

def moveMaxToFront(ll):
    #TODO : Enter code here
    # if ll.size < 2:
    #     return 
    
    # cur = ll.head
    # maxNode = ll.head
    # preMax = None
    
    # while cur.next:
    #     if cur.next.item > maxNode.item:
    #         preMax = cur
    #         maxNode = cur.next
    #     cur = cur.next
    
    # if preMax is None:
    #     return 0
    
    # preMax.next = maxNode.next
    # maxNode.next = ll.head
    # ll.head = maxNode

    # return 0
    if ll.size < 2:
        return
    
    cur = ll.head
    maxNode = ll.head
    index = 0
    maxIndex = 0

    for _ in range(ll.size):
        if cur.item > maxNode.item:
            maxNode = cur
            maxIndex = index
        
        cur = cur.next
        index += 1
    
    ll.removeNode(maxIndex)
    ll.insertNode(maxNode.item, 0)
        

if __name__ == "__main__":
    ll = LinkedList()

    while True:
        print("1: Insert an integer to the linked list:")
        print("2: Move the largest stored value to the front of the list:")
        print("0: Quit:")

        choice = int(input("Please input your choice (1/2/0): "))

        if choice == 1:
            value = int(input("Input an integer that you want to add to the linked list: "))
            ll.insertNode(value, ll.size)  
            print("The resulting linked list is:")
            ll.printList()  
        elif choice == 2:
            moveMaxToFront(ll)
            print("The resulting linked list after moving the largest stored value to the front of the list is:")
            ll.printList()  
        elif choice == 0:
            ll.removeAllItems()  
            break
        else:
            print("Choice unknown.")