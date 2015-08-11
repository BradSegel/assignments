from random import randint, random

# global space is evil, but this lets the functions act as though it
# were pass-by-reference
#A = [6,2,8,4,0,5,7,9,1,3]
a =50
A = [int(a * random()) for i in xrange(a)]
count = 0
# with open("QuickSort.txt", 'r') as f:
#     A = [int(x) for x in f.read().split("\r\n") if x ]

def parter(A,L,R):
    print 'starting {}'.format(A[L:R])

    pivot = A[L] # leftmost elem in bounds
    K = L + 1
    for J in range(L+1,R+1):
        if A[J] < pivot:
            swap(A, K,J)
            K = K + 1
    swap(A,L, K-1)
    return K-1

def swap(A,from_idx, to_idx):
    temp = A[to_idx]
    A[to_idx] = A[from_idx]
    A[from_idx]= temp
    return A

def quicksort(A,L,R):
    part_idx = parter(A,L,R)

    print '{}: {}'.format(part_idx, A)

    count = count + 1

    if R > L and count < 10:
        print '({}, {}) {}: {}'.format(L, R, part_idx, A)

        quicksort(A,0,part_idx-1)
        quicksort(A,part_idx+1,R)


if __name__ == '__main__':
    quicksort(A,0,len(A)-1)
