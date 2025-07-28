def most_spread_out_with_custom(pool, draw_size, bonus_pool, n_draws, custom_draw):
    """
    Generate the most spread out unique draws, ensuring custom_draw is included as one of them.
    pool: main number pool (iterable)
    draw_size: number of main numbers
    bonus_pool: bonus number pool (iterable)
    n_draws: number of draws to return
    custom_draw: list of main numbers (length draw_size) + [bonus]
    """
    draws = set()
    # Add the custom draw first
    draws.add(tuple(sorted(custom_draw[:-1]) + [custom_draw[-1]]))
    # Now fill the rest with spread out draws
    spread_draws = spread_out_draws(pool, draw_size, bonus_pool, 1, n_draws*3)
    for draw in spread_draws:
        tdraw = tuple(draw)
        if tdraw not in draws:
            draws.add(tdraw)
        if len(draws) == n_draws:
            break
    # If not enough, fill with random unique draws
    from random import sample
    while len(draws) < n_draws:
        main = sorted(sample(list(pool), draw_size))
        bonus = sample(list(bonus_pool), 1)[0]
        tdraw = tuple(main + [bonus])
        if tdraw not in draws:
            draws.add(tdraw)
    return [list(draw) for draw in sorted(draws)]
from math import floor
def spread_out_draws(pool, draw_size, bonus_pool, bonus_count, n_draws):
    # Spread out: select numbers as evenly as possible from the pool, all draws unique
    pool = sorted(pool)
    bonus_pool = sorted(bonus_pool)
    draws = set()
    pool_len = len(pool)
    bonus_len = len(bonus_pool)
    for i in range(n_draws * 3):  # Try more times to ensure uniqueness
        # Pick indices spaced out across the pool, offset by i
        main_indices = [(j * pool_len // draw_size + i) % pool_len for j in range(draw_size)]
        main = [pool[idx] for idx in main_indices]
        bonus_idx = (i * bonus_len // n_draws) % bonus_len
        bonus = bonus_pool[bonus_idx]
        draw = tuple(sorted(main) + [bonus])
        draws.add(draw)
        if len(draws) == n_draws:
            break
    # If not enough, fill with random unique draws
    from random import sample
    while len(draws) < n_draws:
        main = sorted(sample(pool, draw_size))
        bonus = sample(bonus_pool, 1)[0]
        draw = tuple(main + [bonus])
        draws.add(draw)
    return [list(draw) for draw in sorted(draws)]
from utils.get_winnings import get_winnings_draws
from utils.add_winnings import add_winning
from utils.analyse_winnings import get_winning_counts
from utils.analyse_winnings import get_bonus_ball_counts
from utils.analyse_winnings import sort_counts_and_numbers


lotto_winnings = get_winnings_draws("./data/lotto_winnings.txt")
powerball_winnings = get_winnings_draws("./data/powerball_winnings.txt")


# lotto_winnings = lotto_winnings[::-1]
# powerball_winnings = powerball_winnings[::-1]

# print("Lottery winnings loaded successfully.")

# if (len(lotto_winnings) == 0):
#     print("No Lotto winnings found.")
# else:
#     print("These are the latest lotto winings: " + str(lotto_winnings));
    
# if (len(powerball_winnings) == 0):
#     print("No Powerball winnings found.")
# else:
#     print("These are the latest powerball winings: " + str(lotto_winnings));  

# print("Let's get this week's Lotto winnings")
# winning = str(input("Enter a winning"))
# while winning != "nah":
#     add_winning(winning, "lotto");
#     print(winning + " added to lotto winnings.")
#     winning = str(input("Enter a winning"))

# print("Let's get this week's Powerball winnings")
# winning = str(input("Enter a winning"))
# while winning != "nah":
#     add_winning(winning, "powerball");
#     print(winning + " added to powerball winnings.")
#     winning = str(input("Enter a winning"))

# print("All winnings have been added successfully.")
print("Calculating winning counts...")
lotto_counts, lotto_numbers = get_winning_counts(lotto_winnings)
powerball_counts, powerball_numbers = get_winning_counts(powerball_winnings)



# Sort the counts and numbers in descending order
lotto_counts, lotto_numbers = sort_counts_and_numbers(lotto_counts, lotto_numbers)
powerball_counts, powerball_numbers = sort_counts_and_numbers(powerball_counts, powerball_numbers)

for i in range(len(lotto_counts)):
    print(f"Number {lotto_numbers[i]} has been drawn {lotto_counts[i]} times in Lotto. \n")


for i in range(len(powerball_counts)):
    print(f"Number {powerball_numbers[i]} has been drawn {powerball_counts[i]} times in Powerball. \n")

# --- Bonus Ball Counts ---
print("\nGet bonus ball counts...")
lotto_bonus_counts, lotto_bonus_numbers = get_bonus_ball_counts(lotto_winnings, bonus_index=6)
powerball_bonus_counts, powerball_bonus_numbers = get_bonus_ball_counts(powerball_winnings, bonus_index=5)

print("Lotto Bonus Ball Counts:")
for i in range(len(lotto_bonus_counts)):
    print(f"Bonus Ball {lotto_bonus_numbers[i]} has been drawn {lotto_bonus_counts[i]} times in Lotto.")

print("Powerball Bonus Ball Counts:")
for i in range(len(powerball_bonus_counts)):
    print(f"Bonus Ball {powerball_bonus_numbers[i]} has been drawn {powerball_bonus_counts[i]} times in Powerball.")

# --- Suggest Most Probable 20 Draws ---
from itertools import combinations



# For Lotto: 6 main + 1 bonus (7th ball is bonus)
from itertools import combinations
from random import sample



# Deterministic: Use only the most selected numbers, generate all combinations, pick first 20
lotto_main_counts, lotto_main_numbers = sort_counts_and_numbers(lotto_counts, lotto_numbers)
lotto_bonus_counts, lotto_bonus_numbers = sort_counts_and_numbers(lotto_bonus_counts, lotto_bonus_numbers)
lotto_top_main = [n for n, c in zip(lotto_main_numbers, lotto_main_counts) if c > 0][:8]  # Shorter range, most frequent
lotto_top_bonus = [n for n, c in zip(lotto_bonus_numbers, lotto_bonus_counts) if c > 0][:2]  # Most frequent bonus balls

from itertools import combinations
lotto_draws = []
for bonus in lotto_top_bonus:
    for combo in combinations(lotto_top_main, 6):
        draw = sorted(list(combo)) + [bonus]
        lotto_draws.append(draw)
        if len(lotto_draws) == 20:
            break
    if len(lotto_draws) == 20:
        break


print("\nSuggested Most Probable 20 Lotto Draws:")
for draw in lotto_draws:
    print(draw)

# --- Statistically Most Probable 20 Lotto Draws ---
from itertools import combinations
import heapq
def draw_score(draw, bonus, main_counts, bonus_counts, main_numbers, bonus_numbers):
    # Score: sum of frequencies for main numbers and bonus
    score = sum(main_counts[main_numbers.index(n)] for n in draw)
    score += bonus_counts[bonus_numbers.index(bonus)]
    return score

all_lotto_draws = []
for bonus in lotto_top_bonus:
    for combo in combinations(lotto_top_main, 6):
        all_lotto_draws.append((list(combo), bonus))

scored_lotto_draws = [
    (draw_score(draw, bonus, lotto_main_counts, lotto_bonus_counts, lotto_main_numbers, lotto_bonus_numbers), sorted(list(draw)) + [bonus])
    for draw, bonus in all_lotto_draws
]
top20_lotto_stat = heapq.nlargest(20, scored_lotto_draws, key=lambda x: x[0])


print("\nStatistically Most Probable 20 Lotto Draws:")
for i, (_, draw) in enumerate(top20_lotto_stat, 1):
    print(f"Draw {i}: {draw}")

# --- Most Spread Out 20 Lotto Draws (with custom) ---
custom_lotto_draw = [2, 3, 7, 9, 22, 27, 49, 1]  # 6 main + 1 bonus
spread_lotto_draws = most_spread_out_with_custom(range(1, 61), 6, range(1, 61), 20, custom_lotto_draw)
print("\nMost Spread Out 20 Lotto Draws (with custom):")
for i, draw in enumerate(spread_lotto_draws, 1):
    print(f"Draw {i}: {draw}")



# Deterministic: Use only the most selected numbers, generate all combinations, pick first 20
powerball_main_counts, powerball_main_numbers = sort_counts_and_numbers(powerball_counts, powerball_numbers)
powerball_bonus_counts, powerball_bonus_numbers = sort_counts_and_numbers(powerball_bonus_counts, powerball_bonus_numbers)
powerball_top_main = [n for n, c in zip(powerball_main_numbers, powerball_main_counts) if c > 0][:7]
powerball_top_bonus = [n for n, c in zip(powerball_bonus_numbers, powerball_bonus_counts) if c > 0][:2]

powerball_draws = []
for bonus in powerball_top_bonus:
    for combo in combinations(powerball_top_main, 5):
        draw = sorted(list(combo)) + [bonus]
        powerball_draws.append(draw)
        if len(powerball_draws) == 20:
            break
    if len(powerball_draws) == 20:
        break


print("\nSuggested Most Probable 20 Powerball Draws:")
for i, draw in enumerate(powerball_draws, 1):
    print(f"Draw {i}: {draw}")

# --- Statistically Most Probable 20 Powerball Draws ---
all_powerball_draws = []
for bonus in powerball_top_bonus:
    for combo in combinations(powerball_top_main, 5):
        all_powerball_draws.append((list(combo), bonus))

scored_powerball_draws = [
    (draw_score(draw, bonus, powerball_main_counts, powerball_bonus_counts, powerball_main_numbers, powerball_bonus_numbers), sorted(list(draw)) + [bonus])
    for draw, bonus in all_powerball_draws
]
top20_powerball_stat = heapq.nlargest(20, scored_powerball_draws, key=lambda x: x[0])


print("\nStatistically Most Probable 20 Powerball Draws:")
for i, (_, draw) in enumerate(top20_powerball_stat, 1):
    print(f"Draw {i}: {draw}")

# --- Most Spread Out 20 Powerball Draws (with custom) ---
custom_powerball_draw = [2, 3, 7, 9, 22, 1]  # 5 main + 1 bonus
spread_powerball_draws = most_spread_out_with_custom(range(1, 61), 5, range(1, 61), 20, custom_powerball_draw)
print("\nMost Spread Out 20 Powerball Draws (with custom):")
for i, draw in enumerate(spread_powerball_draws, 1):
    print(f"Draw {i}: {draw}")



