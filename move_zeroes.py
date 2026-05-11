# Question: Move all 0s in the array to the end without changing the order of non-zero elements. The operation should be done in-place.
# Example 1: Input: [0,1,0,3,12] Output: [1,3,12,0,0]
# Example 2: Input: [0,0,1] Output: [1,0,0]

ls = list(map(int, input("Enter space separated list of numbers: ").split()))
# print(ls)
pos = 0 # assume, this is position of non-zero element
for i in range(len(ls)):
    if ls[i] != 0:
        ls[pos], ls[i] = ls[i], ls[pos]
        pos += 1
print(ls)
