def MultiplesOfNumber(number:int,dividednumber:int)->bool:
    if (number % dividednumber==0):
        return True
    return False

for i in range(1,101):
    if(MultiplesOfNumber(i,3) and MultiplesOfNumber(i,5)):
        print('FizzBuzz')
    elif(MultiplesOfNumber(i,3)):
        print('Fizz')
    elif(MultiplesOfNumber(i,5)):
        print('Buzz')
    else:
        print(i)