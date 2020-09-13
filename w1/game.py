import random

number = random.randint(0, 101)

while True:

    answer = input("Guess the number: ")
    if not answer or answer == "exit":
        break

    if not answer.isdigit():
        print("Enter digits!")
        continue

    user_answer = int(answer)

    if user_answer > number:
        print("The proper number is less")
    elif user_answer < number:
        print("The proper number is greater")
    else:
        print("Correct!")
        break
