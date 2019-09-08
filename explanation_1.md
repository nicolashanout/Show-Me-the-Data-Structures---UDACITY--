## Least Recently Used Cache

### Reasoning

Since all operations need to be O(1) time, then to access and set data we would need to be using a hashtable, so I decided to use python dectionary.
we also need to keep track of the first and last element so we have to use a deque structure, and to be able rearange the elements in the deque in O(1) time I used a doubly linked list to represent the deque.
the `LRU_Cashe` keeps track of the head and tail of the deque, as well as a dectionary that points directly to the Node associated to each value

### Efficiency

- Time Complexity: All operations take O(1) time because:

  - accessing and setting the values through a dictionary takes constant time.
  - accessing the first and last element is constant time as well using the head and tail of the deque.
  - rearranging the elements when we want to move something to the top or drop an element is also constant time because we are using a doubly linked list

- Space Complexity: :
  - set: O(n) where n is the size of the data, because we create a node containing the data.
  - get: O(1) we use the same ammount of memory regardles of the input.
