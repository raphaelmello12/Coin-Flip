import random
import os

def toss_coin():
    list0 = ["heads", "tails"]
    return random.choice(list0)

def main():
    while True:
        flag = False

        os.system("cls")

        answer = input("Pick a side for the coin toss (heads/tails): ")
        
        if answer.lower() not in ["heads", "tails"]:
            continue

        result = toss_coin()

        print(f"You got... {result}")

        if answer.lower() == result:
            print("Nice, you won the coin toss!!")
        else:
            print("Ohh, too bad. You lost this time.")

        while True:
            answer_y = input("Wanna play again? (yes, no): ")
            if answer_y.lower() == "no" or answer_y.lower() == "n":
                flag = True
                break
            elif answer_y.lower() == "yes" or answer_y.lower() == "y":
                break
            else:
                continue
        
        if flag:
            break

if __name__ == "__main__":
    main()