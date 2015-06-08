

def euclid_gcd(numbers=(0,0)):
    """takes a collection of 2 numbers, returns the GCD as determined by euclid's algorithm"""

    while min(numbers) > 0: 
        numbers = (min(numbers), max(numbers)-min(numbers))

    return max(numbers)


def euclid_line_per_step(numbers):
    """does the same thing, but in many more lines of code"""

    while min(numbers) > 0:
        high = max(numbers)
        low = min(numbers)
        new = high - low
        numbers = (low, new)

    return max(numbers)

if __name__ == '__main__':
    print '50,10, gcd: %s' % euclid_gcd([50,10])
    print '252, 105, gcd: %s' % euclid_gcd((252,105))    
    print '567890, 123450, gcd: %s' % euclid_gcd((567890, 123450))
    print '50, 10, steps: %s' % euclid_line_per_step((50,10))
    print '252, 105, steps: %s' % euclid_line_per_step((252,105))
    print '567890, 123450, steps: %s' % euclid_line_per_step((567890, 123450))



