# Instructions

# Implement prime_list(n). Return a list of all prime numbers from 2 to n inclusive. 
# A prime number has exactly two positive divisors. 
# Students may need to research a simple primality test or the Sieve of Eratosthenes.


def prime_list(n):
    primes = []

    for num in range(2, n + 1):
        is_prime = True

        for divisor in range(2, num):
            if num % divisor == 0:
                is_prime = False
                break

        if is_prime:
            primes.append(num)

    return primes