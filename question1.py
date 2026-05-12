# Timed True/False Math Check
# A.I Disclaimer: Some, I used A.I to fix syntax errors
import random
import time


def generate_problem():
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)

    operator = random.choice(["+", "-", "*"])
    if operator == "+":
        actual_answer = num1 + num2
    elif operator == "-":
        actual_answer = num1 - num2
    else:
        actual_answer = num1 * num2

    if random.choice([True, False]):
        proposed_answer = actual_answer
    else:
        proposed_answer = actual_answer + random.choice(
            [i for i in range(-10, 11) if i != 0]
        )

    return num1, num2, operator, actual_answer, proposed_answer


def check_answer(user_input, actual_answer, proposed_answer):
    statement_is_true = (actual_answer == proposed_answer)

    if user_input == "t" and statement_is_true:
        return True
    elif user_input == "f" and not statement_is_true:
        return True
    else:
        return False


def main():
    total_attempted = 0
    correct_answers = 0
    too_slow_answers = 0

    while True:
        num1, num2, operator, actual_answer, proposed_answer = generate_problem()

        print("\nIs this true or false?")
        print(f"{num1} {operator} {num2} = {proposed_answer}")

        start_time = time.time()
        user_input = input("Type t, f, or done: ").lower()
        end_time = time.time()

        elapsed_time = end_time - start_time
        print(f"You took {elapsed_time:.1f} seconds.")

        if user_input == "done":
            break

        if user_input not in ["t", "f"]:
            print("Invalid input. Please type t, f, or done.")
            continue

        total_attempted += 1

        if elapsed_time > 3:
            too_slow_answers += 1
            print("Too slow!")
            continue

        if check_answer(user_input, actual_answer, proposed_answer):
            correct_answers += 1
            print("Correct!")
        else:
            print("Incorrect.")

            if actual_answer == proposed_answer:
                print(
                    f"{num1} {operator} {num2} is actually {actual_answer}, so the statement was true."
                )
            else:
                print(
                    f"{num1} {operator} {num2} is actually {actual_answer}, so the statement was false."
                )

    print("\nTotal attempted:", total_attempted)
    print("Correct:", correct_answers)
    print("Too slow:", too_slow_answers)

    if total_attempted > 0:
        percentage = (correct_answers / total_attempted) * 100
    else:
        percentage = 0

    print(f"Percentage correct: {percentage:.1f}%")


if __name__ == "__main__":
    main()