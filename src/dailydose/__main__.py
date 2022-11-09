from datetime import date
from dailydose import hang
from dailydose import fact


def main():
    run = True

    while run:
        today = date.today()
        print(f"{'*' * 20}")
        print(
            f"Today is {today.strftime('%Y-%m-%d')}. Feeling bored? How about...")

        print(f"\t 1. See a fun fact")
        print(f"\t 2. See a news")
        print(f"\t 3. Play hangman")
        print(f"\t 4. Play battleship")
        print(f"\t 5. <Quit>")

        user_selection = input("Choose a number 1-5...\n> ")
        while user_selection not in ["1", "2", "3", "4", "5"]:
            print("Wrong number...")
            user_selection = input("Choose a number 1-5...\n> ")

        if user_selection == "1":
            random_fact = fact.get()
            print(random_fact[0]['heading'])
            print("\n"+random_fact[0]['content'])

        elif user_selection == "2":
            print("DO YOUR MAGIC news...")

        elif user_selection == "3":
            number_of_letters = input("Choose the length of word 4-10:\n> ")
            hang.hangman(num_letter=number_of_letters)

        elif user_selection == "4":
            print("DO YOUR MAGIC battleship...")

        else:
            print("Bye!")
            run = False


if __name__ == '__main__':
    main()
