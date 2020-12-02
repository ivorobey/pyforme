def fib(n):
    if not isinstance(n, int):
        raise TypeError("Fibonacchi func can work with only <int> type")

    if n < 0:
        raise ValueError("Fibonacchi cant work with negative numbers")

    if n >= 10000:
        raise ValueError("Fibonacchi cant work with larger than 9999")\


    # F=[0,1]+[0]*(n-1)
    # for i in range(2,n+1):
    #     F[i]=F[i-1]+F[i-2]
    # return F[n]


    if n==0:
        return 0
    f_2=0
    f_1=1
    for i in range (2,n+1):
        f_1,f_2=(f_1+f_2),f_1
    return f_1


    
