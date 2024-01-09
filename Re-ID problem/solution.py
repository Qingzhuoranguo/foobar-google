import math

def is_prime (n):
    if n == 2:
        return True;
    for i in range (2, int(math.sqrt(n))+1 ):
        if ( n%i == 0 ):
            return False
   
    return True;
 

def solution(i):
    # Your code here
    primes = ''
    tailindex = 0;
    for num in range (2, 21000):
        if is_prime(num):
            primes += str(num)
            tailindex += len ( str(num) ) - 1
            if ( tailindex-5 >= i):
                break;
                
    result = primes[i:i+5:1]
    return result


print (solution (10000))
