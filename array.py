
array1=[1]
x=2
while len(array1)<100000:
    array1.append(x)
    x=x+1
print(len(array1))


def searcharray(c):
    print(array1[c])


r=input('enter the location of the array starting from 0 to 99999\n')
r=int(r)

searcharray(r)


#written by Owhondah Okechukwu Samuel
