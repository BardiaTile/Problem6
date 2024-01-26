num1 = int(input())
num2 = int(input())
tedad = int(input())
mehmoona = []

while tedad:
    test1 = int(input())
    if test1 < 32:
        if num1 & (1 << test1):
            mehmoona.append('yes')
        else:
            mehmoona.append('no')
    else:
        if num2 & (1 << (test1 - 32)):
            mehmoona.append('yes')
        else:
            mehmoona.append('no')
    tedad -= 1

for a in range(len(mehmoona)):
    print(mehmoona[a])