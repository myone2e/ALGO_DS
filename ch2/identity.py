lst1 = [1,2,3,4,5]
lst2 = [1,2,3,4,5]
print(lst1 is lst2)

lst2 = lst1 #lst2가 lst1을 참조
print(lst1 is lst2)

lst1[2] = 9

print(lst1)
print(lst2)