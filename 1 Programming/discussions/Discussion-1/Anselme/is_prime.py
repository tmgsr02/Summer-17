def is_prime(n):
    divisors = [x for x in range(2,n) if n % x == 0]
    if len(divisors) == 0:
        return True
    else:
        return False
