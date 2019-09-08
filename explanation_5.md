## Blockchain

### Reasoning

I created a linked list where each node has block and a next pointer, and everytime we append data it creates a new block with a time stamp a the prevoius nodes hash, and hashes all that information and appends the new block to the chain

### Efficiency

- Time Complexity: for appending new data it is `O(n)` (because even if we assume that the hash function takes constant time we are concatonating the `data` and `timestamp` and `previous_hash` before hashing them wich takes O(n) because python strings are immutable), for iterationg over the block chain it is also `O(n)`

- Space Complexity: `O(n)` because in order to create the hash we need to concatinate all the data in a string and encode it and then hash it, so the size of the encoded depends on the size of the data.
