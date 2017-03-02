#Recursive Functions, a function that calls itself

#A recursive function that prints a triangle pattern

def main():
    makeTriangle(10)

#Print a triangle with a given length

def makeTriangle(sideLength):
    if sideLength < 1: return
    makeTriangle(sideLength-1)
    #Print the row at the bottom
    print("[]"*sideLength)
#Print the function
main()


def main2(n):
    if n >= 4:
        main2(n/2)
    print(n)
main2(4)


def triArea(h,b):
    area = h*b / 2
    return area
print(triArea(4,52))

def tempconvert(f):
    cel = (f - 32) / 1.8
    return cel
temp1 = tempconvert(32)
temp2 = tempconvert(95)

print(temp1)
print(temp2)

def sqarea(sideLength):
    square = sideLength ** 2
    return square
print(sqarea(5))

