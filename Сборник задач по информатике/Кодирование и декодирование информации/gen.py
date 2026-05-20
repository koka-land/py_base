import random

# Русские буквы
letters_pool = list("АБВГДЕЖЗИКЛМНОПРСТУФХ")

# -----------------------------
# Генерация случайной таблицы кодов
# -----------------------------

def generate_codes(num_letters=6):

    # Случайные буквы
    letters = random.sample(letters_pool, num_letters)

    codes = {}

    used_codes = set()

    while len(codes) < num_letters:

        # случайная длина кода
        length = random.randint(2, 4)

        # случайный бинарный код
        code = ''.join(random.choice('01') for _ in range(length))

        # без повторов
        if code not in used_codes:
            letter = letters[len(codes)]

            codes[letter] = code
            used_codes.add(code)

    return codes


# -----------------------------
# Все расшифровки строки
# -----------------------------

def find_decodings(binary_string, decode_dict):

    results = []

    def dfs(position, current):

        if position == len(binary_string):
            results.append(current)
            return

        for code, letter in decode_dict.items():

            if binary_string.startswith(code, position):

                dfs(
                    position + len(code),
                    current + letter
                )

    dfs(0, "")

    return results


# -----------------------------
# Генерация цепочки
# -----------------------------

def generate_chain(codes, length=8):

    all_codes = list(codes.values())

    chain = ""

    while len(chain) < length:
        chain += random.choice(all_codes)

    return chain[:length]


# -----------------------------
# Генерация задания
# -----------------------------

while True:

    codes = generate_codes()

    decode_dict = {v: k for k, v in codes.items()}

    ambiguous = []
    unique = None

    attempts = 0

    while attempts < 1000:

        chain = generate_chain(codes)

        decodings = find_decodings(chain, decode_dict)

        unique_decodings = set(decodings)

        # несколько расшифровок
        if len(unique_decodings) > 1:

            if chain not in ambiguous:
                ambiguous.append(chain)

        # одна расшифровка
        elif len(unique_decodings) == 1:

            if unique is None:
                unique = chain

        attempts += 1

        # нашли всё необходимое
        if len(ambiguous) >= 3 and unique is not None:
            break

    if len(ambiguous) >= 3 and unique is not None:
        break


# -----------------------------
# Вывод
# -----------------------------

print("Таблица кодов:\n")

for letter, code in codes.items():
    print(f"{letter} = {code}")

print("\nЦепочки:\n")

all_chains = ambiguous[:3] + [unique]

random.shuffle(all_chains)

for i, chain in enumerate(all_chains, 1):

    decodings = find_decodings(chain, decode_dict)

    print(f"{i}) {chain}")

    for d in set(decodings):
        print("   ", d)

    print()

print("Однозначно декодируется:")
print(unique)