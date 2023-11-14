#factorial by recursion
def fact(n):
    if n==0 or n==1:
        return 1
    else:
        fact(n)=n*fact(n-1)

n=int(input("enter the number:"))
print(fact(n))
