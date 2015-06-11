

def euclid_gcd(numbers=(0,0)):
    """takes a collection of 2 numbers, returns the GCD as determined by euclid's algorithm"""
    counter = 0

    while min(numbers) > 0: 
        counter = counter + 1
        numbers = (min(numbers), max(numbers)-min(numbers))

    print "counter: %s" % counter
    return max(numbers)



if __name__ == '__main__':
    print '50,10, gcd: %s' % euclid_gcd([50,10])
    print '252, 105, gcd: %s' % euclid_gcd((252,105))    
    print '567890, 123450, gcd: %s' % euclid_gcd((567890, 123450))



