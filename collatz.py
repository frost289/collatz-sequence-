#if the number is even, divide by 2
# if it odd nultiple by 3 and add 1.. while n is not equal to one

def colla(n):
    
    while n != 1:
        yield n
        n = n / 2 if n %2 == 0 else n * 3 + 1

        
    yield 1






n = pow(10,1000)
print(tuple(colla(n)))