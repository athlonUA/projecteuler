import math;
import itertools;

# Fast prime generator from python cookbook
def erat2():
    D = {}
    yield 2
    for q in itertools.islice(itertools.count(3), 0, None, 2):
        p = D.pop(q, None)
        if p is None:
            D[q*q] = q
            yield q
        else:
            x = p + q
            while x in D or not (x&1):
                x += p
            D[x] = p

def get_primes_erat(n):
  return list(itertools.takewhile(lambda p: p<n, erat2()))            

def find_prime_factors(n):
    primeFactors = []
    for i in get_primes_erat(n):
        fmodule = math.fmod(initialNumber, i)
        if fmodule == 0:
            primeFactors.append(i)

    return primeFactors

initialNumber = 600851475143
n = 10
prime_factors_full = []
while initialNumber != 1:
    prime_factors = find_prime_factors(n)
    
    if len(prime_factors) == 0: 
        n = n*10
    else:
        prime_factors_full = prime_factors_full + prime_factors
        initialNumber = initialNumber/reduce(lambda x, y: x*y, prime_factors)
            

print max(prime_factors_full)
