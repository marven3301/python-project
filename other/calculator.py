def calculator():
    while True:
        print("\nВведите 'q' в любой момент, чтобы выйти.")

        a_input = input("Введите первое число: ")
        if a_input.lower() == 'q':
            break

        b_input = input("Введите второе число: ")
        if b_input.lower() == 'q':
            break

        operation = input("Введите операцию (+, -, *, /): ")
        if operation.lower() == 'q':
            break

        try:
            a = float(a_input)
            b = float(b_input)

            if operation == '+':
                result = a + b
            elif operation == '-':
                result = a - b
            elif operation == '*':
                result = a * b
            elif operation == '/':
                if b != 0:
                    result = a / b
                else:
                    print("Ошибка: деление на ноль")
                    continue
            else:
                print("Ошибка: неизвестная операция")
                continue

            print(f"Результат: {result}")

        except ValueError:
            print("Ошибка: введите корректные числа.")
