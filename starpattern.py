
# 3.1
def star_one(number:int):
    for i in range(1,number+1):
        print('*' * i)

# 3.2
def star_two(number:int):
    for i in range(1,number+1):
        for j in range(number-i):
            print(' ',end='')
        print('*'*i)

# 3.3
def star_three(number:int):
    center_blank = 1
    for i in range(1,number+1):
        if(n == 1):
            print('*')
        else:
            for j in range(1,number-i+1):
                print(' ',end='')
            print('*',end='')
            if i>1:
                for k in range(1,center_blank+1):
                    print(' ',end='')
                center_blank = center_blank + 2
                print('*',end='')
        print()

# 3.4
def star_four(number:int):
    k=number-2
    half_roud = (number+1)//2
    for i in range(half_roud):
        print(' '*i,end='')
        print('*',end='')
        print(' '*k,end='')
        if (i+1 != ((number+1)//2)) or number%2==0:
            print('*',end='')
        k-=2
        print()
    for i in range(n-half_roud,0,-1):
        print(' '*(i-1),end='')
        print('*',end='')
        print(' '*(number-i-i),end='')
        if (i-1 != ((number-half_roud)) or (i == 1)):
            print('*',end='')
        print()
# 3.5
def star_five(number:int):
    k=1
    for i in range((number+1)//2):
        for blank in range(1,((number+1)//2)-i):
            print(' ',end='')
        print('*'*k,end='')
        k+=2
        print()
    if(number%2==0):
        print('*'*(k-2),end='')
        print()
        k=n-1
    else:
        k=n
    for i in range(1,((number)//2+1)):
        for blank in range(i):
            print(' ',end='')
        k-=2
        print('*'*k,end='')
        print()

# 3.6
def star_six(number:int):
    k=number
    p=1
    if(number == 1):
        print('*')
    else:
        for i in range(1,number):
            for a in range(1,k):
                print('A',end='')
            if i == 1 :
                print('+',end='')
            else:
                print('+',end='')
                for e in range(p):
                    print('E',end='')
                p+=2
                print('+',end='')
            for b in range(1,k):
                print('B',end='')
            k-=1
            print()
        print('+',end='')
        for centerE in range(p):
            print('E',end='')
        print('+',end='')
        print()
        for i in range(1,number):
            for c in range(k):
                print('C',end='')
            if i == number-1:
                print('+',end='')
            else:
                p-=2
                print('+',end='')
                for e in range(p):
                    print('E',end='')
                print('+',end='')
            for c in range(k):
                print('D',end='')
            k+=1
            print()


# !Issue = Case Number4 is_prime fix it

if __name__ == '__main__':
    n = int(input('n = '))
    print('--------------------- 1. Star One ---------------------')
    star_one(n)
    print('--------------------- 2. Star Two ---------------------')
    star_two(n)
    print('--------------------- 3. Star Three ---------------------')
    star_three(n)
    print('--------------------- 4. Star Four ---------------------')
    star_four(n)
    print('--------------------- 5. Star Five ---------------------')
    star_five(n)
    print('--------------------- 6. Star Six ---------------------')
    star_six(n)
    print('--------------------- Prime Number ---------------------')
