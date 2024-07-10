class PrimeFactor:

    def get_prime_numbers_from_2_to_number(self, number):
        is_prime = [True] * (number + 1)
        is_prime[0], is_prime[1] = False, False
        for i in range(2, int(number ** (1 / 2)) + 1):
            if is_prime[i]:
                for j in range(i * i, number + 1, i):
                    is_prime[j] = False
        return [num for num, prime in enumerate(is_prime) if prime]
    def get_prime_factors(self, number) -> []:
        prime_numbers = self.get_prime_numbers_from_2_to_number(number)
        return [prime_number for prime_number in prime_numbers if number % prime_number == 0]

