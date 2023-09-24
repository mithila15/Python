# function is a first class object

def double_decker():
    print('hello')
    def inner_fun():
        print('world')
        return 3000
    return inner_fun
#print (double_decker())
#print (double_decker()())

def do_something(work):
    print('Work started')
    #print(work)
    work()
    print('work ended')

def coding():
    print('coding in python')

#do_something(coding)

def sleeping():
    print('Sleeping and dreaming ')
do_something(sleeping)   