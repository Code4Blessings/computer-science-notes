#Hash Tables

"""
 1. Get bytes for the key
 2. Make up a function that returns an index for those bytes
     * Adding the bytes
     * Modding with the hash table size

"""

hash_table_size = 8

def myhash(s):
    str_bytes = str(s).encode()
    
    total = 0

    for b in str_bytes:
        total += b
    return total

def hash_index(s):
    h = myhash(s)

    return h % hash_table_size

if __name__=="__main__":
    #If running from the command line
    print(hash_index("Hello"))
    print(hash_index("foobar"))
    print(hash_index("cats"))
    print(hash_index("robin"))
