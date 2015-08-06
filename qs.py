from random import randint

# global space is evil, but this lets the functions act as though it
# were pass-by-reference
A = [6,2,8,4,0,5,7,9,1,3]

def parter(A,L,R):
    print 'starting {},{}'.format(L,R)
    pivot = A[L] # leftmost elem in bounds
    K = L + 1
    for J in range(L+1,R+1):
        if A[J] < pivot:
            swap(A, K,J)
            K = K + 1

    swap(A,L, K-1)


    print A
    return K-1


def swap(A,from_idx, to_idx):
    temp = A[to_idx]
    A[to_idx] = A[from_idx]
    A[from_idx]= temp
    return A


def quicksort(A,L,R):

        part_idx = parter(A,L,R)

        print '{}:\t{},\t{}'.format(part_idx, A[0:part_idx], A[part_idx+1:R+1])

        if len(A[0:part_idx]) > 1: quicksort(A,0,part_idx)
        if len(A[part_idx+1:R+1]) > 1: quicksort(A,part_idx+1,R+1)

        return A


if __name__ == '__main__':
    print quicksort(A,0,9)
