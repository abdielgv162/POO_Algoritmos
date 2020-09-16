import time

def factorial(n):
    respuesta = 1

    while n > 1:
        respuesta *= n  
        n -= 1

    return respuesta 

def factorial_r(n):
    if n == 1 :
        return 1
    
    return n * factorial(n-1)

if __name__ == '__main__':
    n = 10000

    comienzo = float(time.time())
    factorial(n)
    final = float(time.time())
    print(float((final - comienzo)))

    comienzo = float(time.time())
    factorial_r(n)
    final = float(time.time())
    print(float((final - comienzo)))
