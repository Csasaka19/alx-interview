#!/usr/bin/python3
"""Prime game module"""
# Prototype: def isWinner(x, nums)
# where x is the number of rounds and nums is an array of n
# Return: name of the player that won the most rounds
# If the winner cannot be determined, return None
# You can assume n and x will not be larger than 10000
# You cannot import any packages in this task


def isWinner(x : int, nums : list) -> str:
    """Prime game function"""
    if x <= 0 or nums is None:
        if x > 10000 or nums > 10000:
            print("n and x cannot be larger than 10000.Please try again.")
            return None
        return None
    Maria = 0
    Ben = 0
    n = max(nums)
    primes = [True for i in range(n + 1)]
    p = 2
    while (p * p <= n):
        if (primes[p] == True):
            for i in range(p * 2, n + 1, p):
                primes[i] = False
        p += 1
    primes[0] = False
    primes[1] = False
    c = 0
    for i in range(len(primes)):
        if (primes[i]):
            c += 1
        if (c in nums):
            if (c % 2 == 0):
                Maria += 1
            else:
                Ben += 1
      
    if (Maria > Ben):
        return "Maria"
    elif (Ben > Maria):
        return "Ben"
    else:
        return None
