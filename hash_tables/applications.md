# Applications

## Speed of Search
--------------------

#### Indexing
-------------
Alice: 30
Bob: 40
Charlie: 20
Dave: 20


Problem:
"Show me all the people who are age 30."

Solution:
What do I want to look up by?  <-- that's the key

30: [Alice]
40: [Bob]
20: [Charlie, Dave, Robin]

Given a list of records, need to convert into a hashtable first
THEN we can do quick lookups

#### Removing Duplicates
------------------------
h = {}
for i in data:
    # Have we seen this data before?
    if h[i]:
        continue

    #We've seen it now:
    h[i] = True # same as adding to a set

    print(i)

for i in data: 0(n)
    for j in data: 0(n)
        replace with hashtable 0(1)

Counting Elements
-----------------
1

Aside
-----
The key ina dict can be any immutable type, including tuples.

h = {
    (1, 2): "value1",
    (3, 4): "value2"
}





