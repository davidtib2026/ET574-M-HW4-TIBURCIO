# Name: David Tiburcio
# QCC ID: 23699348
# ET574 HW4 Slot Machine Simulator

import random


class Reel:
    def __init__(self, max_value=9):
        self.max_value = max_value

    def spin(self):
        return random.randint(0, self.max_value)


class SlotMachine:
    def __init__(self):
        self.reel1 = Reel()
        self.reel2 = Reel()
        self.reel3 = Reel()

    def evaluate_spin(self, r1, r2, r3):
        if r1 == r2 == r3:
            return "Win"
        elif r1 == 0 or r2 == 0 or r3 == 0:
            return "Lose"
        else:
            return "Spin Again"

    def play_round(self):
        r1 = self.reel1.spin()
        r2 = self.reel2.spin()
        r3 = self.reel3.spin()
        total = r1 + r2 + r3
        result = self.evaluate_spin(r1, r2, r3)
        return r1, r2, r3, total, result


def main():
    machine = SlotMachine()

    while True:
        print("\n--- Slot Machine Menu ---")
        print("1. Play a round")
        print("2. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            r1, r2, r3, total, result = machine.play_round()
            print(f"Reels: {r1} {r2} {r3}")
            print(f"Total: {total}")
            print(f"Result: {result}")
        elif choice == "2":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")


if __name__ == "__main__":
    main()

# Slot machine completed and tested