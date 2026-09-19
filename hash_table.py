#Custom Hash Table Implementation per requirements, 
# Uses a table of lists to handle collissions with chaining.

class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = []
        for i in range(self.size):
            self.table.append([])  # Initialize each bucket as an empty list

    # Hash function to convert a key into an index
    def get_hash_index(self, key):
        return key % self.size
    #Function to insert a key and value (package object) into the corresponding bucket in the hash table
    #If there is a collision, it will be handled through chaining by appending the new package to the list.
    def insert(self, key, value):
        bucket_index = self.get_hash_index(key)
        bucket = self.table[bucket_index]

        # Check if the key already exists in the bucket
        for item in bucket:
            if item[0]==key: 
                item[1] = value #update the package if the key already exists.
                return

        # if the key doesn't exist,  add a new key value pair to the bucket. 
        # This is where chaining happens if there's a collision.
        bucket.append([key, value])
