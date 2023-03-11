class Node:

    def __init__(self, data, next_node=None)
        self.data = data
        self.next_node = next_node



class LinkedList:

    # head is the first node in the linked list
    # will point to the next node once start adding more elements
    def __init__(self, head=None):
        self.head = head

    
    def append(self, node):
        # Add element to the beginning of the list if the list is empty
        if self.head == None:
            self.head = node
            return
        
        # Otherwise, traverse the list to find the last node
        last_node = self.head
        while last_node.next_node:  # => Node("Bulldog").next_node
            last_node = last_node.next_node
        
        # and add the node to the end
        last_node.next_node = node



# ===================not using append()======================
# # create nodes
# bulldog = Node("bulldog")
# chihuahua = Node("Chihuahua")

# # the first node points to next node
# bulldog.next_node = chihuahua
# # Bulldog -> Chihuahua

# german_shepard = Node("German Shepard")
# chihuahua.next_node = german_shepard
# # Bulldog -> Chihuahua -> German Shepard

# ==========================================================
ls = LinkedList()
ls.append(Node("Bulldog"))

print(ls.head.data)  # => Bulldog
print(ls.head.next_node)   #=>None

ls.append(Node("Chihuahua"))
print(ls.head.data)  # => Bulldog
print(ls.head.next_node.data) #=>Chihuahua

ls.append(Node("German Shepard"))
print(ls.head.next_node.data)  # => Chihuahua
print(ls.head.next_node.next_node.data) #=>German Shepard
