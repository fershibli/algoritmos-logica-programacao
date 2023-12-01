def isPrime(number):
    for n in range(2, number//2):
        if number % n == 0:
            return False
    return True


def getPrimes(number):
    prime_numbers = 0
    for n in range(number+1):
        if isPrime(n):
            prime_numbers += 1
    return prime_numbers


def sumPrimes(number):
    total = 0
    for n in range(number+1):
        if isPrime(n):
            total += n
    return total


entrada = int(input('Digite quantos numeros você quer testar:\n>>>'))
print(f'De 0 até {entrada} existem {getPrimes(entrada)} números primos.')
print(f'A soma desses números primos é: {sumPrimes(entrada)}')
