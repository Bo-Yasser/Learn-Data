
def selection_sort(arr, reverse=False):
    for i in range(len(arr) - 1):
        minidx = i
        for j in range(i + 1, len(arr)):
            if arr[minidx] > arr[j]:
                arr[minidx], arr[j] = arr[j], arr[minidx]




def bubble_sort(arr, reverse=False):
    if reverse:
        for i in range(len(arr) - 1):
            for j in range(i,len(arr)-1):
                if arr[j] < arr[j + 1]:
                    arr[j], arr[j+1] = arr[j + 1] ,arr[j] 
    
    
    for i in range(len(arr) - 1):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1] ,arr[j] 



l = [20,10,40,70,100,80]
# selection_sort(l)
bubble_sort(l, reverse= True)

print(l)