# arr = [1, 2, 2, 3, 4, 5, 32, 3, 4, 2, 3, 4, 2, 2, 1, 8]
# my_dict = {}

# for i in range(len(arr)):
#     my_dict[arr[i]] = my_dict.get(arr[i], 0) + 1

# print(my_dict[2])
# print(my_dict[1])

#Hashing

# arr = [1, 2, 2, 3, 4, 5, 32, 3, 4, 2, 3, 4, 2, 2, 1, 8]
# check=[1,4,7,11,4,9,3]

# dict={}
# for i in arr:
#  dict[i] =dict.get(i, 0) + 1

# print(dict)

#HAshing using list
arr = [1, 2, 3, 1, 2, 1]

# Find the maximum value in the list to define size of hash table
max_val = max(arr)

# Create a list of zeros of size max_val + 1
freq = [0] * (max_val + 1)

# Count frequency
for i in arr:
    freq[i] += 1

# Print frequencies
for i in range(len(freq)):
    # if freq[i] > 0:
        print(f"{i} occurs {freq[i]} times")
