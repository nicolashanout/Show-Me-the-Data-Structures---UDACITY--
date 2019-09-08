## Finding Files

### Reasoning

A file structure is a tree, so I used inorder DFS to traverse the structure and find the files that contain that right suffix

### Efficiency <sup>1</sup>

- Time Complexity: time complexity for a tree of n nodes is O(n) and for each node that is a file we have to check if the filename ends with the suffix which is of time complexity O(l) where l is the length of the suffix.
  so the time complexity is `O(n*l)`

- Space Complexity: `O(b*m + n*l)` where m is the longest path and b is the number of sibling nodes along the path, and where n is the number of file nodes and l is the length of the longest file path.

<sup>1</sup>[source](https://stackoverflow.com/questions/36479640/time-space-complexity-of-depth-first-search)
