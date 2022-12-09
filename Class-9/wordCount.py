file = open("article.txt", "r")

text = file.read()
#Find the number of France came in the article
cnt = 0
for i in range(0, len(text)-6):
    word = text[i:i+6]
    if word == 'France':
        cnt = cnt + 1
print("The number of times France is in the text :",cnt)
