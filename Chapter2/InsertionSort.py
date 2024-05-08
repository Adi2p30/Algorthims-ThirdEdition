A = [4, 35, 25, 1, 34, 155, 1, 2, 5, 253252, 354, 3, 5, 4]
for i in range(0, len(A)):
    key = A[i]
    j = i - 1
    while j >= 0 and key < A[j]:
        A[j+1] = A[j]
        j -= 1
        print(A)
        print(key)
    A[j+1] = key
    print(key)


