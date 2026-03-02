n = int(input("Введіть кількість секунд (0 ≤ n < 8640000): "))

if 0 <= n < 8640000:

    days, remainder = divmod(n, 86400)
    hours, remainder = divmod(remainder, 3600)
    minutes, seconds = divmod(remainder, 60)

    # Підбір правильного слова "день"
    if days % 10 == 1 and days % 100 != 11:
        day_word = "день"
    elif 2 <= days % 10 <= 4 and not (12 <= days % 100 <= 14):
        day_word = "дні"
    else:
        day_word = "днів"

    print(f"{days} {day_word}, "
          f"{str(hours).zfill(2)}:"
          f"{str(minutes).zfill(2)}:"
          f"{str(seconds).zfill(2)}")

else:
    print("Число повинно бути в діапазоні від 0 до 8639999.")