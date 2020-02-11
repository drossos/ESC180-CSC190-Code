def main():
        for i in range(0,10,1):
                print(str(fib(i)))

def fib(n):
        if (n == 1 or n == 0):
                return 1
        else:
                return fib(n-1) + fib(n-2)
main()
