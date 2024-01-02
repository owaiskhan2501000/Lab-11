class PrimeNumberIterator:
    def __init__(self, limit):
        self.limit = limit
        self.current = 2

    def is_prime(self, num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def __iter__(self):
        return self

    def __next__(self):
        while self.current <= self.limit:
            if self.is_prime(self.current):
                result = self.current
                self.current += 1
                return result
            else:
                self.current += 1
        raise StopIteration
    
prime_iterator = PrimeNumberIterator(20)

for prime in prime_iterator:
    print(prime)
