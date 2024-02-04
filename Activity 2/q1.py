
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def getPrimeNumbers(n):
    return [num for num in range(2, n + 1) if is_prime(num)]

# Example usage:
n = 20
prime_numbers = getPrimeNumbers(n)
print(f"Prime numbers between 2 and {n}: {prime_numbers}")
