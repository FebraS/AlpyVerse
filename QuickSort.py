def quicksort(arr):
    #Base case
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]

        leftChunk = [i for i in arr[1:] if i <= pivot]

        rightChunk =  [i for i in arr[1:] if i > pivot]

        return quicksort(leftChunk) + [pivot] + quicksort(rightChunk)
    
print(quicksort([14,3,2,12]))
