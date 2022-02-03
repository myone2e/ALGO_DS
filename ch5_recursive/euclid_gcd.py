# math.gcd 존재
def gcd(x, y):
    
    if y == 0:
        return x
    
    else:
        return gcd(y, x%y)

if __name__ == '__main__':
    print("Enter two positive ints")
    x, y = map(int, input().split())
    print(gcd(x,y))