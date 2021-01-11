import math
def mysqur(a):
    x=a+1
    while True:

        y = (x + a/x) / 2
        if y == x:
            break
        x = y
    return x

b=1.0
print('a','   ', 'mysqrt(a)  ', '              ','math.sqrt(a)              ', 'diff     ')
while b<=9:
    print(b,' ', mysqur(b),' '*(25 -len(str(mysqur(b)))), math.sqrt(b),' '*(25 -len(str(math.sqrt(b)))), (mysqur(b)-math.sqrt(b)))
    b=b+1



#written by Owhondah Okechukwu Samuel
