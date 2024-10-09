def is_prime(func):
    def wrapper(*args,**kwargs):
        result = func(*args,**kwargs)
        if result < 2:
            print ('простое')
        else:
            for i in range(2,int(result**0.5)+1):
                if result % i == 0:
                    print('составное')
                    break
            else:
                print('простое')
        return result
    return wrapper


@is_prime
def sum_three(*args):
    sums = 0
    for i in args:
        sums += i
    return sums

result = sum_three(2, 3, 6)
print(result)


