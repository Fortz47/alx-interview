#!/usr/bin/python3
"""Module to solve prime game"""


def isWinner(x, nums):
    def sieve(max_n):
        """
        Create a list of boolean values indicating prime numbers up to max_n.
        is_prime[i] is True if i is a prime number, False otherwise.
        """
        is_prime = [True] * (max_n + 1)
        is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime numbers
        p = 2
        while p * p <= max_n:
            if is_prime[p]:
                # Mark all multiples of p as non-prime
                for multiple in range(p * p, max_n + 1, p):
                    is_prime[multiple] = False
            p += 1
        return is_prime

    # Determine the maximum value of n to create the sieve up to that point
    max_n = max(nums)
    # Get the list of prime indicators up to max_n
    is_prime = sieve(max_n)

    def prime_count_up_to(n):
        """
        Count the number of prime numbers up to and including n.
        """
        return sum(is_prime[:n + 1])

    # Initialize win counters for Maria and Ben
    maria_wins = 0
    ben_wins = 0

    # Simulate each round of the game
    for n in nums:
        # Count the primes up to the current n
        primes_up_to_n = prime_count_up_to(n)
        # If the count of primes is odd, Maria wins this round
        if primes_up_to_n % 2 == 1:
            maria_wins += 1
        else:
            # If the count of primes is even, Ben wins this round
            ben_wins += 1

    # Determine the overall winner based on the win counts
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
