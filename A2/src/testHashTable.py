
from hashTable import HashTable

tab = HashTable()

tab["Hello"] = "Hello1"
tab["Hello"] = "Hello2"
tab["World"] = "World"

print(tab["Hello"])
print(tab["World"])

print("\n\nKey-Value Pairs:")
for k,v in tab.items():
    print(k,v)

print("\n\nKeys:")
for i in tab.keys():
    print(i)

print("\n\nValues:")
for i in tab:
    print(i)


