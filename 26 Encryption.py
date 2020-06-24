code = str(input("What would you like encrypted: "))
hello = False
num = 0
count = 0
letterCount = 0
for i in range(len(code)):
    num += (ord(code[i]) - 64) * (26 ** (len(code) - i - 1))
print(num)
decrypt = num
while not hello:
    decrypt = decrypt - (26 ** (count + 1))
    count = count + 1
    if decrypt < 0:
        hello = True
print(count)
