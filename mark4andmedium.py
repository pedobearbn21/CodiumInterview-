# Else and Finally in Error Handling
'''
    In Error Handling
    Program will run else  when Try didn't has a error or exception
    And Program will run finally when Process run  try->except->else->finally  so finally will always run in the last.
'''

# Medium
def is_prime(num):
    for j in range(2,(num//2)+1):
        if(num%j==0):
            return False
    return True


if __name__ == '__main__':
    num_list_prime = int(input('Enter Num for Gen list prime number ='))
    list_numbers = [ i for i in range(2,num_list_prime+1) if is_prime(i) ]
    print(f' {num_list_prime} => {list_numbers}')