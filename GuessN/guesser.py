import random

def number_guesser(guess, answer, min_bound, max_bound):
    if guess == answer:
        guess = True
    elif guess < answer:
        min_bound = guess
    elif guess > answer:
        max_bound = guess
    return guess, answer, min_bound, max_bound