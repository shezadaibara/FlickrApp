'''
1. The FizzBuzz test.
Write a program that prints the integers from 1 to 100. But for multiples of
three print "Fizz" instead of the number and for the multiples of five print
"Buzz". For numbers which are multiples of both three and five print "FizzBuzz".
'''


def main(limit):

    for i in xrange(1, limit + 1):
        _str = ''
        if i % 3 == 0:
            _str += 'Fizz'
        if i % 5 == 0:
            _str += 'Buzz'
            
        print _str or i


if __name__ == '__main__':
    main(100)
