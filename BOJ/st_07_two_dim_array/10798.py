x = [[0] * 15 for i in range(5)]

for i in range(5):
    word = list(input())
    w_len = len(word)

    for j in range(w_len):
        x[i][j] = word[j]

for i in range(15):
    for j in range(5):

        if x[j][i] == 0:
            continue;

        else:
            print(x[j][i], end='')
