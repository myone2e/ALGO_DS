def card_conv(x, r):
    
    d = ''
    dchar = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    n = len(str(x))
    
    print(f'{r:2} | {x:{n}d}')
    while x > 0:
        print('    +' + (n+2)*'-')
        if x // r:
            print(f'{r:2} | {x//r:{n}d} ... {x%r}')
        else:
            print(f'      {x//r:{n}d} ... {x%r}')
        d += dchar[x%r]
        x //= r
        
    return d[::-1]

if __name__ == '__main__':
    print('Decimal to n cardinal')

    while True:
        while True: #non-negative int
            no = int(input("Enter a Target number : "))
            if no > 0:
                break #다음 루프로 넘어가도록
        
        while True :
            cd = int(input('Which scale do you want to convert ? : '))
            if 2 <= cd <= 36:
                break
        
        print(f'{cd} cardinal, {card_conv(no, cd)}')
        
        retry = input("Want to do once more? (Y or N) : ")
        if retry in {'N', 'n'}:
            break
