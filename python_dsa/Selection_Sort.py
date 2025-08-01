arr=[2,3,5,6,33,52,8]
i=0
n=len(arr)

while i<n:
    j=i+1
    while j<n:
        if arr[i]>arr[j]:
            arr[i],arr[j]=arr[j],arr[i]
        j=j+1
    i=i+1        


print(arr)

