import math
def timer(func):
    def inner(*args):
        print('time started')
       #print(func)
        func(*args)
        print ('time ended')

    return inner

@timer
def get_factorial(n):
    print('factorial starting')
    result = math.factorial(n)
    print(f'factorial of {n} is: {result}')
get_factorial(5)

# timer get_factorial()()

