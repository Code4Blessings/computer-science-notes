Open Addressing: Linear Probing

 "foo" hashes to index 1
 "bar" hashes to index 2

put ("foo", 12)
put("bar", 30)
put("baz", 99)

0       1              2            3       <--index
[None, ("foo",12), ("bar",30), "baz", 99]

Put: 
Scan forward fro the hash index until we find either the key, or None 
If we find a deleted slot along the way, keep it mind 
Put the value there

Get:
Scan forward from the hash index until we find either the key, or None
Return that

Delete:
Scan forward from the hash index until we find either the key, or None
If we find the key, mark it as deleted


Collision Resilution by Chaining
-------------------------------------

Each slot of the hash table holds a linked list
Collsions are handled by handled by adding multiple items to the same linked list

Slot
Index Chain (linked list)
----- -------------------
0       -> None
1       -> ("foo", 12)
2       -> None
3       -> None

put("foo", 12) # hashes to index 1
put("bar", 30) # hashes to index 2
put("baz", 999) # hashes to index 2

Put:
Search the list for the key
If it's there, replace the value
If it's not, append a new record to the list

Get: 
Find the hash index
Search the list for the key
If found, return the value
Else return none

Delete:
Find the hash index
Search the list for the key
If found, delete the node from the list, (return the node or value?)
Else return None

### Resizing:

#### Step 1:
- Make a new bigger table/array/list

#### Step 2:
- Go through all the old elements and hash into the new list

#### Rule of Thumb:
- If you resize bigger, double the size.
-If you resize smaller, half the size