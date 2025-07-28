def add_winning(winning:str, pot: str) -> None:
    day, draw, numbers = winning.strip().split()
    if pot == "lotto":
        with open("./data/lotto_winnings.txt", "a") as file:
            file.write(f"{day} {draw} {numbers}\n")
        print(f"Added winning draw: {day} {draw} {numbers} {pot}")
    elif pot == "powerball":
        with open("./data/powerball_winnings.txt", "a") as file:
            file.write(f"{day} {draw} {numbers}\n")
        print(f"Added winning draw: {day} {draw} {numbers} {pot}")

