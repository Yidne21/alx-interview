#!/usr/bin/python3
'''
prime_game solution module
'''


def isWinner(x, nums):
    '''
    Helper function to check if a number is prime
    '''

    def is_prime(num):
        '''
        A  Eratosthenes function to check if a number is prime
        '''

        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def play_game(n):
        '''
        Create a set of all prime numbers up to n
        '''

        prime_set = set()
        for i in range(2, n + 1):
            if is_prime(i):
                prime_set.add(i)
        maria_turn = True
        while prime_set:
            can_remove = set()
            for prime in prime_set:
                if n % prime == 0:
                    can_remove.add(prime)
                    can_remove |= set(range(prime, n + 1, prime))
            if not can_remove:
                break
            if maria_turn:
                prime = max(can_remove)
                prime_set.discard(prime)
            else:
                prime = min(can_remove)
                prime_set -= set(range(prime, n + 1, prime))
            n -= prime
            maria_turn = not maria_turn
        return "Maria" if maria_turn else "Ben"

    maria_wins = 0
    ben_wins = 0
    for n in nums:
        winner = play_game(n)
        if winner == "Maria":
            maria_wins += 1
        elif winner == "Ben":
            ben_wins += 1
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
