import time

def GCD(m,n):
    counter = 0 
    while n != 0:
        counter = counter + 1
        r = m % n
        m = n
        n = r
    return [counter, m]

def gcdizer(gcd_to_number=10):
    print 'starting to calculate GCD from all pairs of integers from 2 to {}'.format(gcd_to_number)
    counter = 0
    for m in range(2, gcd_to_number): # outer loop, m will be slow
        for n in range(2, gcd_to_number): # inner loop, n will be fast
            # combinations of n < m have already been calculated
            if n >=m:
                # I expect there is another way to speed this up by tracking multiples
                counter = counter + 1
                print 'GCD of {0} and {1} is {3} and took {2}'.format(m,n,*GCD(m,n))
       
    print 'finished in {} loops to find all combinations from 2 to {}'.format(counter, gcd_to_number)



def better_gcdizer(gcd_to_num=10):
#    print 'starting to calculate GCD from all pairs of integers between 2 and {}'.format(gcd_to_num)
    counter = 0
    m=gcd_to_num
    output ={}
    start_time = time.time()

    # count from high to low, seems to be 1 fewer eval per execution for GCD(m,n) when n > m 
    while m > 1:
        n = gcd_to_num
        while n > 1:
            counter = counter + 1
            val = GCD(m,n)
            if 'loop_count' not in output or val[0] > output['loop_count']: 
                output['loop_count'], output['GCD'] = val # 0: number of loops, 1: the GCD
                output['m_value'] = m # .append(m) # 2: outer value being processed
                output['n_value'] = n # .append(n) # 3: inner value being processed
                # 4: amount of time it took to get to the answer
                now_time = time.time()
#                print 'current GCD pair for {}: {}  at {} seconds'.format(gcd_to_num, val[0], now_time-start_time)
                output['time_for_answer'] = now_time - start_time
            n = n - 1
            if n < m: break # avoid duplicating effort since 3,5 is the same as 5,3
        m = m - 1

    output['time_to_run'] = time.time() - start_time

    return output


if __name__ == '__main__':
    import matplotlib.pyplot as plt
    all_results = []
    for x in range(0,10000,100)[1:]:
        val = x 
        all_results.append( better_gcdizer(val) )
#        print all_results
        all_results[-1]['N'] = x
#        print 'For an N of {0}: GCD of {3} and {4} is {2} found in {5} seconds in {1} loops that ran a for {6} seconds'.format(val, *better_gcdizer(val))


    for x in all_results: print x

    plt.plot([a['N'] for a in all_results],[a['time_for_answer'] for a in all_results],[a['N'] for a in all_results],[a['time_to_run'] for a in all_results], 'r')
    plt.xlabel('N')
    plt.ylabel('time')
    plt.show()







