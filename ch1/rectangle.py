area = int(input("Enter an area: "))

for i in range(1, area + 1):
    if i*i >area:
        break
    if area % i: #나머지가 있다면 스킵 
        continue
    print(f'{i} x {area // i}')