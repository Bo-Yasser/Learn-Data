def brute_force_max_sum(arr, k):
    max_sum = float("-inf")
    for i in range(len(arr) -k + 1):
        curr_sum = 0 
        for j in range(i, i +k):
            curr_sum += arr[j]

        max_sum = max(max_sum, curr_sum)
    return max_sum


def brute_force_max_sum(arr, k):
    max_sum = float("-inf")
    for i in range(len(arr) -k + 1):
        curr_sum = sum(arr[i:i+k])
        max_sum = max(max_sum, curr_sum)
    return max_sum


arr = [1,30,22,10,20,15,2,4]

k = 4

print(brute_force_max_sum(arr,k))

