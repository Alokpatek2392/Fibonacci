def F(n):
    a=0
    b=1
    print(a)
    print(b)
    for i in range(1,n):
        c=a+b
        a=b
        b=c
        if(c%3==0 and c%5!=0):
            print('Buzz')
        elif(c%5==0 and c%3!=0):
            print('Fizz')
        elif(is_prime_number(c)):
            print('BuzzFizz')
        else:
            print(c)

def is_prime_number(x):
    if x >= 2:
        for y in range(2,x):
            if not ( x % y ):
                return False
    else:
        return False
    return True

