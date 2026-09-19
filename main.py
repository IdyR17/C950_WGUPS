#Student ID: 010585953

from package import Package
from hash_table import HashTable

print("WGUPS Routing Program")

package_test1= Package(
    1,
    "1 abc st",
    "Bergenfield",
    "NJ",
    "07621",
    "8:00 AM",
    "7",
    "Nothing"
)

print(package_test1)

test_hash_table = HashTable()
#Testing hash function to see if it returns the same bucket.
print(test_hash_table.get_hash_index(2))
print(test_hash_table.get_hash_index(22))
test_hash_table.insert(2, "Package test for collision")
test_hash_table.insert(22, "Another package test for collision")
print(test_hash_table.table)
print(test_hash_table.get_package(2))