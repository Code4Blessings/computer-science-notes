#Hash Tables

"""
 1. Get bytes for the key
 2. Make up a function that returns an index for those bytes
     * Adding the bytes
     * Modding with the hash table size

"""

hash_table_size = 8

hash_table = [None] * hash_table_size

def myhash(s):
    str_bytes = str(s).encode()
    
    total = 0

    for b in str_bytes:
        total += b
    return total

def hash_index(s):
    h = myhash(s)

    return h % hash_table_size

def put(key, value):
    index = hash_index(key)
    hash_table[index] = value

def get(key):
    index = hash_index(key)
    return hash_table[index]

def delete(key):
    index = hash_index(key)
    hash_table[index] = None


if __name__=="__main__":
    #If running from the command line
    print(hash_index("Hello")) #4
    print(hash_index("foobar"))# 1
    print(hash_index("cats"))
    print(hash_index("robin"))
    print(hash_index("foobaz"))
    print(hash_index("quz"))
    

    print(hash_table)
    put("Hello", 37)
    put("foobar", 128)
    put("cats", "dogs")
    print(hash_table)

    print(get("Hello"))




