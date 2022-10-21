def array():
    N = int(input('Введите желаемый размер массива - '))
    a=int(input('Как вы хотите вести значения массива?(1-с клавиатуры; 2-рандомно) - '))
    from random import randint
    B = [0] * N
    if a==1:
        for i in range(N):
            print('Введите значение массива с индексом', i, '- ', end='')
            B[i] = float(input())
    else:
        for i in range(N):
            B[i] = randint(0, 100)
    print('Исходный массив: ',end='')
    return (B)
def max_e():
    A=array()
    print(A)
    max=A[0]
    for i in range(len(A)):
        if (A[i]>=max):
            i1=i
    for i in range(len(A)):
        if i>i1:
            A[i]=0
    print('Изменённый массив: ',end='')
    return(A)
print(max_e())



