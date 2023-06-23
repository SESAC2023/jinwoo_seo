N = int(input())

total_word = N

for i in range(N):
    word = input()
    for j in range(len(word)-1):
        if word[j] == word[j+1]:
            continue
        elif word[j] in word[j+2:]:
            total_word -= 1
            break
print(total_word)
