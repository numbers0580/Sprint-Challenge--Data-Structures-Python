import time
from binarytree import BSTNode

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

# I ran the code above on my computer, and it took 6.418457984924316 seconds to find 64 duplicates

# So I mathematically calculated that the above nested for-loop will run a total of 100 million times to populate duplicates
# Obviously, we're looking for a better method to populate duplicates. I also noticed neither names_1 or 2 are sorted, at all. Ughh...
nomen = BSTNode(names_1[0])

# This loop runs exactly 9,999 times + 1 time in the nomen declaration above = 10,000 times
for n in names_1[1:]: # Start with the 2nd position since we manually put the first position in the nomen declaration
    nomen.insert(n)

# This loop runs exactly 10,000 times, and the contains function runs at most 14 times to search all 10,000 = max total of 140,000 times
for n in names_2:
    if nomen.contains(n):
        duplicates.append(n)
# New max grand total iterations = 150,000 which is <<< than 100,000,000 iterations
# Running my code, it took 0.08975982676015625 seconds

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
