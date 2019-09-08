class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            if cur_head.next:
                out_string += str(cur_head.value) + " -> "
            else:
                out_string += str(cur_head.value)
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def union(llist_1, llist_2):
    # Your Solution Here
    u_set = set()
    current_node = llist_1.head
    while current_node:
        u_set.add(current_node.value)
        current_node = current_node.next
    
    current_node = llist_2.head
    while current_node:
        u_set.add(current_node.value)
        current_node = current_node.next

    u_head = Node(None)
    u_current_node = u_head
    for element in u_set:
        u_current_node.next = Node(element)
        u_current_node = u_current_node.next
    u_head = u_head.next
    u_list = LinkedList()
    u_list.head = u_head
    return u_list

def intersection(llist_1, llist_2):
    # Your Solution Here
    i_set1 = set()
    current_node = llist_1.head
    while current_node:
        i_set1.add(current_node.value)
        current_node = current_node.next
    
    i_set2 = set()
    current_node = llist_2.head
    while current_node:
        i_set2.add(current_node.value)
        current_node = current_node.next
    i_head = Node(None)
    i_current_node = i_head

    i_set = i_set1.intersection(i_set2)
    for element in i_set:
        i_current_node.next = Node(element)
        i_current_node = i_current_node.next
    i_head = i_head.next
    i_list = LinkedList()
    i_list.head = i_head
    return i_list


print('\n---------------------------------------------\n')
# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))
#expected output (in some order): 32 -> 65 -> 2 -> 35 -> 3 -> 4 -> 6 -> 1 -> 9 -> 11 -> 21

print (intersection(linked_list_1,linked_list_2))
#expected output (in some order): 4 -> 21 -> 6

print('\n---------------------------------------------\n')
# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))
#expected output (in some order): 65 -> 2 -> 35 -> 3 -> 4 -> 6 -> 1 -> 7 -> 8 -> 9 -> 11 -> 21 -> 23

print (intersection(linked_list_3,linked_list_4))
#expected output: nothing


print('\n---------------------------------------------\n')
# Test case 3

linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

element_1 = []
element_2 = []

for i in element_1:
    linked_list_5.append(i)

for i in element_2:
    linked_list_6.append(i)

print (union(linked_list_5,linked_list_6))
#expected output nothing

print (intersection(linked_list_5,linked_list_6))
#expected output: nothing


print('\n---------------------------------------------\n')
# Test case 4

linked_list_7 = LinkedList()
linked_list_8 = LinkedList()

element_1 = [1,2,3,4]
element_2 = [1,2,3,4]

for i in element_1:
    linked_list_7.append(i)

for i in element_2:
    linked_list_8.append(i)

print (union(linked_list_7, linked_list_8))
#expected output (in some order): 1 -> 2 -> 3 -> 4

print (intersection(linked_list_7, linked_list_8))
#expected output (in some order): 1 -> 2 -> 3 -> 4


print('\n---------------------------------------------\n')
# Test case 5

linked_list_9 = LinkedList()
linked_list_10 = LinkedList()

element_1 = [17]
element_2 = [17]

for i in element_1:
    linked_list_9.append(i)

for i in element_2:
    linked_list_10.append(i)

print (union(linked_list_9, linked_list_10))
#expected output (in some order): 17

print (intersection(linked_list_9, linked_list_10))
#expected output (in some order): 17