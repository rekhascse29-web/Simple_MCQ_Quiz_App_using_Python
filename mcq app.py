def run_quiz():
    score = 0

    print("----- Welcome to the Math Quiz -----")

    for i in range(1, 21):

        if i == 1:
            question = "5 + 7 ="
            print("A. 10  B. 11  C. 12  D. 13")
            correct = "C"

        elif i == 2:
            question = "9 × 6 ="
            print("A. 54  B. 56  C. 64  D. 52")
            correct = "A"

        elif i == 3:
            question = "Square root of 144 ="
            print("A. 10  B. 11  C. 12  D. 14")
            correct = "C"

        elif i == 4:
            question = "25 ÷ 5 ="
            print("A. 4  B. 5  C. 6  D. 7")
            correct = "B"

        elif i == 5:
            question = "15 - 8 ="
            print("A. 6  B. 7  C. 8  D. 9")
            correct = "B"

        elif i == 6:
            question = "7 × 8 ="
            print("A. 54  B. 56  C. 64  D. 58")
            correct = "B"

        elif i == 7:
            question = "Square of 9 ="
            print("A. 81  B. 72  C. 91  D. 99")
            correct = "A"

        elif i == 8:
            question = "36 ÷ 6 ="
            print("A. 5  B. 6  C. 7  D. 8")
            correct = "B"

        elif i == 9:
            question = "12 + 15 ="
            print("A. 25  B. 26  C. 27  D. 28")
            correct = "C"

        elif i == 10:
            question = "18 - 9 ="
            print("A. 7  B. 8  C. 9  D. 10")
            correct = "C"

        elif i == 11:
            question = "11 × 11 ="
            print("A. 111  B. 121  C. 131  D. 141")
            correct = "B"

        elif i == 12:
            question = "Square root of 81 ="
            print("A. 7  B. 8  C. 9  D. 10")
            correct = "C"

        elif i == 13:
            question = "50 ÷ 10 ="
            print("A. 4  B. 5  C. 6  D. 7")
            correct = "B"

        elif i == 14:
            question = "20 + 15 ="
            print("A. 35  B. 34  C. 36  D. 37")
            correct = "A"

        elif i == 15:
            question = "14 - 6 ="
            print("A. 7  B. 8  C. 9  D. 10")
            correct = "B"

        elif i == 16:
            question = "6 × 9 ="
            print("A. 52  B. 53  C. 54  D. 55")
            correct = "C"

        elif i == 17:
            question = "Square of 7 ="
            print("A. 47  B. 48  C. 49  D. 50")
            correct = "C"

        elif i == 18:
            question = "81 ÷ 9 ="
            print("A. 8  B. 9  C. 10  D. 11")
            correct = "B"

        elif i == 19:
            question = "17 + 13 ="
            print("A. 29  B. 30  C. 31  D. 32")
            correct = "C"

        elif i == 20:
            question = "30 - 12 ="
            print("A. 17  B. 18  C. 19  D. 20")
            correct = "B"

        print("\nQuestion", i, ":", question)
        answer = input("Enter your answer (A/B/C/D): ").upper()

        if answer == correct:
            print("Correct!\n")
            score += 1
        else:
            print("Wrong! Correct answer is", correct, "\n")

    print("----- Quiz Finished -----")
    print("Your Score:", score, "/ 20")

    if score == 20:
        print("Excellent!")
    elif score >= 15:
        print("Great Job!")
    elif score >= 10:
        print("Good effort!")
    else:
        print("Keep practicing!")

run_quiz()
