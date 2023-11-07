def isPrime(number):
    for k in range(2, number//2):
        if number % k == 0:
            return False
    return True