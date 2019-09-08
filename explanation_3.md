## Huffman Coding

### Reasoning

to encode the data first I counted the frequency of each charachter, then built heapafied tree where the leaf nodes were the charachters the depth of each charachter in the tree is determined by their frequency in the data.

### Efficiency

- Time Complexity:

  - encoding: `O(n^2)` for:

    - finding the frequency of each charachter is `O(n)` (loop once through the input)
    - from building the tree and since i'm storing the nodes in a dictionary, then it takes in the worst case 2 loops through the dictionary to find the 2 nodes with the lowest weight, in the dectionary to replace 2 nodes with 1 `O(n)`, and we need to repeat this until we have 1 node left `O(n-1)` this gives us `O(n^2-n)`. -(note: using a heap it could have been O(nlogn) since finding the lowest weight and inserting and heapifingO(logn) for n nodes)-
    - generating the code: O(nlogn) where in the the number of unique charachters in the data (the number of leafes in the tree)
    - replacing the charachters in the string (encode), takes O(n^2) because here we are replacing charachters in the string.

  - decoding: also `O(n^2)`
    - generating the reverse code: `O(nlogn)` where in the the number of unique charachters in the data (the number of leafes in the tree)
    - `O(n^2)` where n is the length of the encoded data for building the string, loops over all charachters in the encoded data, and for each match with the reverse_code dictionary, it bulds a new string `O(n)`

- Space Complexity:
  - `O(u*log(u))` from the tree for encoding
  - decoding `O(n)` where n is the length of the string.

#### External Sources:

(https://brilliant.org/wiki/huffman-encoding/)
[huffman coding visualizer](https://people.ok.ubc.ca/ylucet/DS/Huffman.html)
