# Проверка на палиндром
def is_palindrome(line: str) -> bool:
    return line.lower() == line.lower()[::-1]


def palindrome_message(line: str) -> str:
    return f"{line} is a palindrome" if is_palindrome(line) else f"{line} is not a palindrome"


# Преобразование строки в заглавные слова
def title_case(text: str) -> str:
    return text.title()
