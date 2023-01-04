words = open('prob42text.txt','r')

trianglewords = []
triangles = []
for i in range(40):
    triangles.append((i*(i+1))//2)

wordList = words.read().split(",")
wordList.sort()

def get_char_score(letter):
    #print(letter)
    return ord(letter) - 64

def score_without_order(name):
    score = 0
    for char in name:
        #print(char)
        score += get_char_score(char)
    return score

for word in wordList:
    #print(word)
    if score_without_order(word.strip("\"")) in triangles:
        trianglewords.append(word)
        print(word)

print(len(trianglewords))
#print(nameList[937])

words.close()