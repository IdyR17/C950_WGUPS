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