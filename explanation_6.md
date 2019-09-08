## Union and Intersection of Two Linked Lists

\*PS: a python set is implemented using hash tables and technically has a worst case time complexity of O(n) for adding and geting values but in practice it is O(1) so we'll be using that for our analysis.

### Reasoning

we'll use pythons built-in set class to perform the intersection and union.
in the case of union we'll add the values from both lists to a set, which ill give us a union, then iterate over the set and add the values to a linked list
in the case of intersection we'll add the values from each lists to a set,then intersect them, then iterate over the resulting set and add the values to a linked list

### Efficiency

- Time Complexity:

  - union: `O(s1+s2)` where s1 is the number of elements in the first set and s2 is the number of elements in the second set -basically O(n) where n is the size of the input-
  - intersection: `O(n)` where n is the longer of the 2 lists.

- Space Complexity:
  - union and intersection: `O(n)` where n is the size of the input (llist_1 + llist_2)
