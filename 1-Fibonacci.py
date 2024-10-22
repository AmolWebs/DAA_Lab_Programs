def recursive_fibonacci(n):
    if n<=1:
        return n
    else:
        return recursive_fibonacci(n-1) + recursive_fibonacci(n-2)
    

def non_recursive_fibonacci(n):
    first=0
    second=1
    print(first,end=" ")
    print(second,end=" ")
    while n-2>0:
        third = first + second
        first=second
        second=third
        print(third,end=" ")
        n-=1

if __name__=="__main__":
    print("Name : Amol Subhash Dangat\nRoll No : 09\n")
    fibo_range = int(input("Enter Length for Fibonacci Series : "))
    print("Fibonacci series by recursive approach : ",end=" ")
    for i in range(fibo_range):
        print(recursive_fibonacci(i),end=" ")

    print("\nFibonacci series by iterative approach : ",end=" ")
    non_recursive_fibonacci(fibo_range)