names = open('prob22text.txt', 'r')

nameList = names.read().split(",")
nameList.sort()

def get_char_score(letter):
    return ord(letter) - 64

def score_without_order(name):
    score = 0
    for char in name:
        score += get_char_score(char)
    return score

totalscore = 0

for i in range(len(nameList)):
    totalscore += ((i+1)*(score_without_order(nameList[i].strip('\"'))))

print(totalscore)
#print(nameList[937])

names.close()