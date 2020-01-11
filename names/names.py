import time
 
from binary_search_tree import BinarySearchTree

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []
#runtime ~11s
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# runtime ~ 0.2s
# binary_search = BinarySearchTree(names_1[0])
# for i in range(1, len(names_1)):
#     binary_search.insert(names_1[i])
# for i in range(1, len(names_2)):
#     if binary_search.contains(names_2[i]):
#         duplicates.append(names_2[i])

# runtime ~ 0.02s
cache = {}
for names_1 in names_1:
    cache[names_1] = names_1
for names_2 in names_2:
    if names_2 in cache:
        duplicates.append(names_2)
        
end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish with no restrictions on techniques or data
# structures?

# O(n log n)