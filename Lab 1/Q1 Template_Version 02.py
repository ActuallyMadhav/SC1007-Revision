class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data, index):
        new_node = Node(data)

        if self.head is None or index == 0:
            new_node.next = self.head
            self.head = new_node
            return 1
    
        current = self.head
        count = 0
    
        while current and count < index - 1:
            current = current.next
            count += 1
    
        if not current:
            print("Index out of range")
            return 0
        
        new_node.next = current.next
        current.next = new_node
        return 1

    def remove(self, index):
        # Write your code here #
        if self.head is None:
            print("List is empty")
            return True
        
        if index == 0:
            self.haed = self.head.next
            return True
        cur = self.head
        prev = None
        count = 0
        while cur and count < index:
            prev = cur
            cur = cur.next
            count += 1
        if cur is None:
            print("Index out of range")
            return False
        prev.next = cur.next
        return True

        
    def printList(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

# Test the implementation
if __name__ == "__main__":
    linked_list = LinkedList()
    size = 0
    
    print("Enter one number per line (press Enter after each number).")
    print("Enter any non-digit character to finish input:")
    while True:
        try:
            item = int(input())
            if linked_list.insert(item, size) == 1:
                size += 1
                print("Node successfully inserted")
            else:
                print("Insertion failed")
            print("Current List:", end=" ")
            linked_list.printList()
        except ValueError:
            break
    
    while True:
        try:
            index = int(input("Enter the index of the node to be removed: "))
            if linked_list.remove(index) == 1:
                size -= 1
                print("Node successfully removed")
            else:
                print("Removal failed")
            print("After the removal operation:")
            linked_list.printList()
        except ValueError:
            break
    
    print("Final List:", end=" ")
    linked_list.printList()