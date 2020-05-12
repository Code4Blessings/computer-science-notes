# Hash Tables
--------------

## Concepts
------------

- Privides data lookup by key rather than by index
- Behaves like a dictionary or an associative array (PHP)
- Internally still uses a flat array
- Static chaining - collisions are handled by creating a linked list where there are multiple matches
- Each index in the internal flat array is referred to as a "bucket"

### There are 4 methods found in a hash table 

1. Hash 
2. Insert
3. Find
4. Remove

#### Hash Method

- The hash method will take a string of characters as input.
- The hsh function converts this to an integer representing its position in the internal array. In other words, the key must be converted to the index in the buckets array.
- At minimum: we need uniformity.  

#### Insert Method
1. Increment size of the hashtable
2. Compute index of key using hash function
3. If the bucket at the index is empty, create a new node and add it there.
4. Otherwise, a collision occurred: there is already a linked list of at least one node at this index. Iterate to the end of the list and add a new node there.

#### Find Method
1. Compute the index for the provided key using the hash function.
2. Go to the bucket for that index.
3. Iterate the nodes in that linked list until the key is found, or the end of the list is reached
4. Return the value of the node, or None if not found.

#### Remove Method
1. Compute hash for the key to determine the index.
2. Iterate linked list of nodes. Continue until the end of the list is reached or until the key is found.
3. If the key is not found, return None.
4. Otherwiase, remove the node from the linked list and return the node value.




