
from hashTable import HashTable

tab = HashTable()

tab["Hello"] = "Hello1"
tab["Hello"] = "Hello2"
tab["World"] = "World"

print(tab["Hello"])
print(tab["World"])

