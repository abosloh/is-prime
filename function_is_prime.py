

def isprime(n):
    '''check if integer n is a prime'''
    # range starts with 2 and only needs to go up the squareroot of n
    for x in range(2, int(n**0.5)+1):
        if n % x == 0:
            return False
    return True
  
if isprime(10) == True:
  print "is prime"
else:
  print "is not prime"

# the outcome will be "is not prime"
