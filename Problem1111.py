num1 = int(input())
num2 = int(input())
xor = num1 ^ num2
adad = 0
while xor != 0 :
    if (xor & 1) == 1:
        adad += 1
    xor >>= 1

print(adad)