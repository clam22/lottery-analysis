from datetime import datetime

def get_winnings_draws(file_path : str) -> list:
    print(f"Reading winning draws from {file_path}...")
    winning_draws = []
    with open(file_path, "r") as file:
        next(file)  # Skip the header line
        for line in file:
            winning_draw = line.strip().split()
            if len(winning_draw) == 3:
                day, draw, numbers = winning_draw
                winning_draws.append({
                    "day": datetime.strptime(day, "%Y-%m-%d").date(),
                    "draw": str(draw),
                    "numbers": [int(num) for num in numbers.split(",")]
                })
    print(f"Done reading winning draws from {file_path}.")
    return winning_draws 