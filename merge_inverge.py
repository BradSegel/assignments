
def merge_sort(unsorted_list):
    print "split: {}".format(unsorted_list)
    l = len(unsorted_list)
    # here's our base case
    if l <= 2:
        # make sure it's ordered
        if l==2 and unsorted_list[0] > unsorted_list[1]:
            holder = unsorted_list[0]
            unsorted_list[0] = unsorted_list[1]
            unsorted_list[1] = holder
        return unsorted_list

    a = merge_sort(unsorted_list[:(l/2)])
    b = merge_sort(unsorted_list[(l/2):])

    print 'merging {} into {}'.format(b, a)

    while b:
        for idx, a_val in enumerate(a):
            print "------\na: {}\nb: {}\nidx: {}\na_val: {}\nb[0]: {}".format(a,b,idx,a_val,b[0])

            if a_val > b[0]: # when we get to a value in a bigger than b[0]
                a[idx:idx] = [b.pop(0)]

            if len(a) == idx: # b now contains larger values than a
                a.extend(b)
                b = None # we want out of this while loop

    print 'merged: {}'.format(a)

    return a


if __name__ == '__main__':
    print 'result: {}'.format(merge_sort([5,2,8,3,7,1,4,6,9,0]))
#    print 'result: {}'.format(merge_sort([2,3,4,1]))
