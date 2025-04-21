def kth_smallest_linear(matrix, k):
    arr = []
    for i in matrix:
        arr.extend(i)
    return arr[k-1]



# read input
n, k = map(int, input().split())
matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))

# output
print(kth_smallest_linear(matrix, k))