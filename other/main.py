from calculator import calculator
import cards
import time
import random
import text_tools
import sorter
from faker import Faker


def randname(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        fake_name = Faker.name().split()[0]
        fake_city = Faker.city()
        print(f"name {fake_name}, city {fake_city}")

    return wrapper


while True:
    print("Welcome to my program\n"
          " 1. Calculator\n"
          "2. Card game\n"
          "3. Polindrome check\n"
          "4. Bubble sort\n"
          "5. Fake name and city")
    num = input(">>> ")

    # calculator
    if num == "1":
        print(calculator())

    # card game
    elif num == "2":
        print("Waiting till the program launches...")
        time.sleep(1)
        print("Launch was successful")

        # Главное меню
        while True:
            select = input("Enter parameter: \n 1. 56 cards\n 2. 36 cards\n 3. Results\n Q. Quit\n>>> ")

            if select == "1":
                game_deck = cards.get_full_deck()
                random.shuffle(game_deck)
                print("The deck is shuffled")

                player1_cards, game_deck = cards.get_deck(6, game_deck)
                player2_cards, game_deck = cards.get_deck(6, game_deck)

                time.sleep(0.6)

                print("player 1 cards: ", player1_cards)
                print("player 2 cards: ", player2_cards)

                p1_points = cards.get_points(player1_cards)
                p2_points = cards.get_points(player2_cards)

                print(f"player 1 points: {p1_points}")
                print(f"player 2 points: {p2_points}")

                winner, points = cards.difference_in_points(player1_cards, player2_cards)
                print(f"{winner} wins with {points} points" if winner != "Draw" else "It's a draw!")

                cards.save_result(winner, points)

                input("Press Enter to return to the menu...")

            elif select == "2":
                game_deck = cards.get_deck_36()
                random.shuffle(game_deck)
                print("The deck is shuffled")

                player1_cards, game_deck = cards.get_cards_36(6, game_deck)
                player2_cards, game_deck = cards.get_cards_36(6, game_deck)

                time.sleep(0.6)

                print("player 1 cards: ", player1_cards)
                print("player 2 cards: ", player2_cards)

                p1_points = cards.get_points(player1_cards)
                p2_points = cards.get_points(player2_cards)

                print(f"player 1 points: {p1_points}")
                print(f"player 2 points: {p2_points}")

                winner, points = cards.difference_in_points(player1_cards, player2_cards)
                print(f"{winner} wins with {points} points" if winner != "Draw" else "It's a draw!")

                cards.save_result(winner, points)

                input("Press Enter to return to the menu...")

            elif select == "3":
                print("Saved results:")
                for line in cards.get_save():
                    print(line)

                input("Press Enter to return to the menu...")

            elif select.upper() == "Q":
                print("Exiting the game. Goodbye!")
                break

            # palindrome test
    elif num == "3":
        text = input("Enter text to check for palindrome: ")
        print(text_tools.palindrome_message(text))

        input("Press Enter to return to the main menu...")

    elif num.upper() == "Q":
        print("Goodbye!")
        break

    # bubble sort
    elif num == "4":
        print(sorter.sort_from_input())
        input("Press Enter to return to the main menu...")

    # Fake name and city
    elif num == "5":
        @randname
        def say_hello():
            print("Hello")
        say_hello()

    # Quit the program
    elif num.lower() == "q":
        print("Exiting the program...")
        time.sleep(1)
        break

    # Wrong number check
    else:
        print("Wrong number")


