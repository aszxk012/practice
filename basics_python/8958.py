test = int(input())

for i in range(test):
    score = 0
    final_score = 0
    quiz = input()

    for j in quiz:
        if j == "O":
            score += 1

        elif j == "X":
            score = 0


        final_score += score

    print(final_score)