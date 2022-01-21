print("Compute Summation from 1 to n")
n = int(input("Enter a Postive int: "))
if n < 0:
    print("Enter Positive int!!")
    n = int(input("Enter Again: "))
    
sum = 0 
for i in range(1, n+1): #range is iterable object
    sum += i
print(f'sum of 1 to n is {sum}')