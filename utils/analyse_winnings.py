from collections import Counter

def get_winning_counts(winnings) :
    counts = [0 for i in range(1, 61)]
    numbers = [i for i in range(1, 61)]
    for winning in winnings:
        for number in winning["numbers"]:
            counts[number - 1] += 1

    return counts, numbers


def get_bonus_ball_counts(winnings, bonus_index=6):
    """
    Returns the counts of bonus balls. Specify bonus_index:
    - For Lotto: bonus_index=6 (7th number)
    - For Powerball: bonus_index=5 (6th number)
    """
    bonus_counts = [0 for i in range(1, 61)]
    numbers = [i for i in range(1, 61)]
    for winning in winnings:
        if len(winning["numbers"]) > bonus_index:
            bonus_counts[winning["numbers"][bonus_index] - 1] += 1
    return bonus_counts, numbers


def is_sorted(lst):
    for i in range(len(lst) - 1):
        if lst[i] < lst[i + 1]:
            return False
    return True

def sort_counts_and_numbers(counts, numbers):
    # Sorts counts and numbers in descending order of counts using the original logic
    counts = counts[:]
    numbers = numbers[:]
    def is_sorted_local(lst):
        for i in range(len(lst) - 1):
            if lst[i] < lst[i + 1]:
                return False
        return True
    while not is_sorted_local(counts):
        for i in range(len(counts) - 1):
            if counts[i] < counts[i + 1]:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                counts[i], counts[i + 1] = counts[i + 1], counts[i]
    return counts, numbers

