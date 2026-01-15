import random

def higher_lower():
    score = 0

    print("Higher / Lower o‘yini boshlandi!")
    print("Qaysi son kattaroq? '1' yoki '2' deb javob bering.\n")

    while True:
        a = random.randint(1, 100)
        b = random.randint(1, 100)

        print(f"1-son: {a}")
        print(f"2-son: {b}")

        answer = input("Qaysi biri katta? (1/2): ")

        if (answer == "1" and a > b) or (answer == "2" and b > a):
            score += 1
            print("To‘g‘ri! Ball:", score)
        else:
            print("Xato!")
            print("O‘yin tugadi. Yakuniy ball:", score)
            break

higher_lower()
