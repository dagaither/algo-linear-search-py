bananas_list = list('bananas')

def linear_search(char, arr):
    for i in range(len(arr)):
        if arr[i] == char:
            return i
    return None
    

def linear_search_global(char, arr):
    result = []
    for i in range(len(arr)):
        if arr[i] == char:
            result.append(i)
    return result

print(linear_search(3, [1,2,3]))