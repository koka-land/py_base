a = 3 * 2187**2020 + 3 * 729**2021 - 2 * 81**2022 + 27**2023 - 4 * 3**2024 - 2029

otvet = 0

while a > 0:
    if a % 27 > 9:
        otvet += 1
    a //= 27

print(otvet)
