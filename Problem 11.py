def Bitwise_add(a,b):
    while b != 0:
        carry = a&b
        a = a^b
        b = carry<<1

    return a

n = int(input())

m = int(input())

k = int(input())

s = Bitwise_add(n,m)

print(s)

if k == s:
    print("YES")
else:
    print("NO")

