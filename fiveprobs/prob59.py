alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

ciphertext = open('prob59text.txt','r')
nums = ciphertext.read().split(",")

words = open('prob42text.txt','r')
wordListOld = words.read().split(",")
wordList = [word.strip("\"").lower() for word in wordListOld]

maxkey = ""
maxnumwords = 0

print(ord("a"))

for i in range(26):
    for j in range(26):
        for k in range(26):
            key = alphabet[i]+alphabet[j]+alphabet[k]
            #print(key)
            decryptedUsingKey = ""
            for num in range(len(nums)):
                #print(key[num%3])
                decryptedUsingKey += chr((ord(key[num%3]) and not nums[num]) or (not ord(key[num%3]) and nums[num]))
                print(decryptedUsingKey)
            wordsInDecr = decryptedUsingKey.split(" ")
            numwords = 0
            for word in wordsInDecr:
                word = word.lower()
                newWord = ""
                for char in word:
                    if char in alphabet:
                        newWord += char
                if newWord in wordList:
                    numwords += 1
            if numwords >= maxnumwords:
                #print("numwords: " + str(numwords))
                maxnumwords = numwords
                #print("old maxkey: " + maxkey)
                #print("new maxkey: " + key)
                maxkey = key

decryptedUsingKeyFinal = ""
print(maxkey)
for num in range(len(nums)):
    decryptedUsingKeyFinal += chr((ord(maxkey[num%3]) and not nums[num]) or (not ord(maxkey[num%3]) and nums[num]))

print(decryptedUsingKeyFinal)