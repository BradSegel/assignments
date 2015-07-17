
def merge_sort(unsorted_list):
#    print "{}".format(unsorted_list)
    l = len(unsorted_list)
    if l == 1:
        return unsorted_list

    a = merge_sort(unsorted_list[:(l/2)])
    b = merge_sort(unsorted_list[(l/2):])

    print '{}:{}'.format(a,b)


    for x,y in enumerate(b):
        print "{}".format(y)
        if a[0] > x:
            b[y:y] = a
        return b


if __name__ == '__main__':
    print merge_sort([5,2,8,3,7,1,4,6,9,0])
