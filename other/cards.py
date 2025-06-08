import random

# Сохраняем результаты
save = list()

# Колоды
suits = ["♥️", "♦️", "♠️", "♣️"]
models = ["A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2"]
models36 = ["A", "K", "Q", "J", "10", "9", "8", "7", "6"]

deck = [f"{suit} | {model}" for suit in suits for model in models]
deck36 = [f"{suit} | {model}" for suit in suits for model in models36]


def get_deck(count: int, current_deck: list) -> tuple:
    result = current_deck[:count]
    for el in result:
        current_deck.remove(el)
    return result, current_deck


def get_cards_36(count: int, current_deck: list) -> tuple:
    result = current_deck[:count]
    for el in result:
        current_deck.remove(el)
    return result, current_deck


def get_points(player_cards: list) -> int:
    result = 0
    for el in player_cards:
        el = el.split(" | ")[-1]
        if el.isdigit():
            result += int(el)
        elif el == "A":
            result += 1
        elif el in ["K", "Q", "J"]:
            result += 10
    return result


def difference_in_points(player1_cards: list, player2_cards: list) -> tuple:
    p1_points = get_points(player1_cards)
    p2_points = get_points(player2_cards)
    if p1_points > p2_points:
        return "Player 1", p1_points
    elif p1_points < p2_points:
        return "Player 2", p2_points
    else:
        return "Draw", p1_points


def save_result(winner, points):
    save.append(f"Winner: {winner} with points {points}")


def get_save():
    return save.copy()


def get_full_deck():
    return deck.copy()


def get_deck_36():
    return deck36.copy()
