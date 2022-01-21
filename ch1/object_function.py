n = 1
def put_id():
    x = 1 #local
    print(f'id(x) = {id(x)}')

print(f'id(1) = {id(1)}' )
print(f'id(n) = {id(n)}')
put_id()
#n과 x는 모두 int형 객체 1을 참조하는 이름일 뿐
#정수 객체는 함수와 무관하게 존재