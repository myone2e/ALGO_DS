from sympy import factor


def factorial(n):
    
    if n > 0:
        return n * factorial(n-1) # 이 부분이 recursive call (자기 자신과 똑같은 함수를 호출한다고 생각)
    else:
        return 1
    
if __name__ == '__main__':
    n = int(input())
    print(factorial(n))


# n = 5 => 5*fac(4) => 5*4*fac(3) ...