word = list(input())
answer = 1
word_len = len(word)
for i in range((word_len // 2) + 1): # 4인 경우,
    if word[i] != word[-i - 1]:
        answer = 0

print(answer)

# if word == list(reversed(word)):
#     print(1)
# else:
#     print(0)