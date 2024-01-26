import math
import functools

action = input()

if action not in ['sum', 'average', 'min', 'max', 'gcd', 'lcd']:
    print('Invalid command')
else:
    adada = []
    adad = ''
    while adad != 'end':
        adad = input()
        if adad != 'end':
            adada.append(int(adad))

    if action == 'sum':
         jam = sum(adada)
         print(jam)
    elif action == 'average':
        jam = sum(adada)
        tedad = len(adada)
        javab = (jam/tedad)
        print(round(javab,2))
    elif action == 'min':
        kochik = min(adada)
        print(kochik)
    elif action == 'max':
        bozorg = max(adada)
        print(bozorg)
    elif action == 'gcd':
        gcd_result = functools.reduce(math.gcd, adada)
        print(gcd_result)
    elif action == 'lcd':
        def lcm(a, b):
            return abs(a*b) // math.gcd(a, b)

        lcm_result = functools.reduce(lcm, adada)
        print(lcm_result)