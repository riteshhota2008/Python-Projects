import random

count_heads = 0
count_tails = 0

while True:

    guess = random.choice([0, 1])  # Uses 0 and 1 as Heads and Tails
    play = str(input("Would you like to flip a coin? Yes or No: "))

    if play.lower() == "no":
        print("The coin has flipped {} Heads and {} Tails."
              .format(count_heads, count_tails))
        break

    if guess == 0:
        count_heads += 1
        print("Heads")

    else:
        count_tails += 1
        print("Tails")
