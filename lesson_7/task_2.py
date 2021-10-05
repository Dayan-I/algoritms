# 2.	Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на
# промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.
import random
a = [random.randint(0, 49) for i in range(10)]
print(a)
def merge_sort(A):
    if len(A) == 1 or len(A) == 0:
        return A
    L, R = A[:len(A) // 2], A[len(A) // 2:]
    merge_sort(L)
    merge_sort(R)
    n = m = k = 0
    C = [0] * (len(L) + len(R))
    while n < len(L) and m < len(R):
        if L[n] <= R[m]:
            C[k] = L[n]
            n += 1
        else:
            C[k] = R[m]
            m += 1
        k += 1
    while n < len(L):
        C[k] = L[n]
        n += 1
        k += 1
    while m < len(R):
        C[k] = R[m]
        m += 1
        k += 1
    for i in range(len(A)):
        A[i] = C[i]
    return A

print(merge_sort(a))