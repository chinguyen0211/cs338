import hashlib


# ============  PART 1  ============
pwDict1 = {}

words1 = [line.strip().lower() for line in open('words.txt')]
for line in open('passwords1.txt'):
    pw = line.split(':')
    pwDict1[pw[1]] = pw[0]

f = open('cracked1.txt', 'a')
computedH1 = 0
crackedPw1 = 0
for word in words1:
    hPw = hashlib.sha256(word.encode('ascii')).hexdigest()
    computedH1 += 1
    if pwDict1.get(hPw) is not None:
        f.write(pwDict1.get(hPw) + ":" + word + "\n")
        crackedPw1 += 1
f.close()

print("# hashes computed = ", computedH1)
print("# of passwords cracked = ", crackedPw1)

# ============  PART 2  ============

pwDict2 = {}

words2 = [line.strip().lower() for line in open('words.txt')]
print(len(words2))
for line in open('passwords2.txt'):
    pw = line.split(':')
    pwDict2[pw[1]] = pw[0]

f = open('cracked2.txt', 'a')
computedH2 = 0
crackedPw2 = 0
for word in words2:
    for secondWord in words2:
        newWord = word + secondWord
        hPw = hashlib.sha256(newWord.encode('ascii')).hexdigest()
        computedH2 += 1
        if pwDict2.get(hPw) is not None:
            f.write(pwDict2.get(hPw) + ":" + word + "\n")
            crackedPw2 += 1
f.close()

print("# hashes computed = ", computedH2)
print("# of passwords cracked = ", crackedPw2)
