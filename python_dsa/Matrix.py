nums = [[5, 10, 8], [7, 6, 3], [2, 1, 9]]
rows = len(nums)
cols = len(nums[0])

for i in range(rows - 1, -1, -1):       # Loop from last row to first
    for j in range(cols - 1, -1, -1):   # Loop from last col to first
        if i + j == rows - 1:
            print(nums[i][j])

nums = [[5, 10, 8], [7, 6, 3]]
rows = len(nums)
cols = len(nums[0])
result=[[0]*rows for _ in range(cols)]

for i in range(0,rows):       
    for j in range(0,cols):
        result[j][i]=nums[i][j]

print(nums)        
print(result)  