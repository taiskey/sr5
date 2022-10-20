
a = float(input("ВВедите любое число: "))
a = int(a)
k = ''
k = a
c=''
b = int(input("Введите целевую систему счисления(2 или 8): "))
if b==2:
    while a > 0:
        c = str(a%2)+c
        a = a//2
if b==8:
    while a >0:
        c = str(a%8)+c
        a= a//8
print(k, "-->", c)



