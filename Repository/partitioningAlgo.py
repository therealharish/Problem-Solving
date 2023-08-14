# function to segregate positive and negative numbers in an array in o(n) time
def partitioningAlgo(arr, target):
    neg = 0
    for i in range(len(arr)):
        if arr[i] < target:
            arr[i], arr[neg] = arr[neg], arr[i]
            neg += 1
    return arr
            
        
    
    
    

arr = [-1, 2, -3, 4, -6, -7]    
print(partitioningAlgo(arr, 0))