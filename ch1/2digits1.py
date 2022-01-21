print("Enter a 2 digit int: ")

while True:
    no = int(input("Enter a value: "))
    if no >= 10 and no <= 99: #10 <= no <= 99와 같고 no<10 or no > 99와도 같음 (드모르간)
        break
print(f'Entered number is {no}')