# Task 2 - A
# Custom Hash Table Implementation per requirements,
# Uses a list of bucket lists to handle collisions with chaining.


class HashTable:
    # Creates hash table
    def __init__(self, size=10):
        self.size = size
        self.table = []
        for i in range(self.size):
            self.table.append([])  # Initialize each bucket as an empty list

    # Hash function to convert a key (Package ID) into an index using modulo
    def get_hash_index(self, key):
        return key % self.size

    # Function to insert a key and value (Package object) into the corresponding bucket in the hash table
    # If there is a collision, it will be handled through chaining by appending the new package to the list.
    def insert(self, key, value):
        bucket_index = self.get_hash_index(key)
        bucket = self.table[bucket_index]

        # Check if the key already exists in the bucket
        for item in bucket:
            if item[0] == key:
                item[1] = value  # update the package if the key already exists.
                return

        # if the key doesn't exist,  add a new key value pair to the bucket.
        # This is where chaining happens if there's a collision.
        bucket.append([key, value])

    # Function to retrieve a value (Package object) from the hash table using its key
    # The same hash function identifies the bucket, then we search for the key
    def get_package(self, key):
        bucket_index = self.get_hash_index(key)
        bucket = self.table[bucket_index]

        for item in bucket:
            if item[0] == key:
                return item[1]  # Return the package object (value) if found

        return None
