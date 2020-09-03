import time
from binary_search_tree import BSTNode

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

bst_names = BSTNode(names_1.pop())
for name_1 in names_1:
    bst_names.insert(name_1)
for name_2 in names_2:
    if bst_names.contains(name_2):
        duplicates.append(name_2)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print("Binary search tree")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.

t_start = time.time()
hash_duplicates = []

hash_names = {names_1.pop(): True}
for name_1 in names_1:
    hash_names[name_1] = True
for name_2 in names_2:
    if name_2 in hash_names:
        hash_duplicates.append(name_2)

t_finished = time.time()
print(f"{len(hash_duplicates)} duplicates:\n\n{', '.join(hash_duplicates)}\n\n")
print("hash table")
print(f"runtime: {t_finished - t_start} seconds")