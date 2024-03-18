#!/usr/bin/python3
"""Given a number n, write a method that calculates the fewest
number of operations needed to result in exactly n H
characters in the file."""
from collections import deque


def isPrime(n: int) -> bool:
    """check if n is prime"""
    primes = [2, 3, 5, 7]
    return all(n % x != 0 for x in primes if n > x)


def primeNumbers(n: int) -> deque:
    """return list of prime numbers ranging from 1 to n"""
    que = deque()
    for i in range(2, n + 1):
        if isPrime(i):
            que.append(i)
    return que


def minOperations(n: int) -> int:
    """calculates the fewest number of operations needed to
    result in exactly n H characters in the file"""
    if isinstance(n, int) and n > 0:
        if n == 1:
            return 0
        que = primeNumbers(n)
        _dict = {}
        num = n
        i = 0
        while True:
            if num % que[i] == 0:
                num /= que[i]
                _dict.setdefault(que[i], 0)
                _dict[que[i]] += 1
                if isPrime(num):
                    if num == 1:
                        break
                    _dict.setdefault(num, 0)
                    _dict[num] += 1
                    break
                i = 0
            i += 1
        print(_dict, que)
        return sum([pow(k, v) for k, v in _dict.items()])
