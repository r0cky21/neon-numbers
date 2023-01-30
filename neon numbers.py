#neon-------

n=int(input("enter number"))
n1=n

sq=n*n
sm=0

while(n!=0):
    rem=n%10
    sm=(sm*10)+rem
    n = n//10

if(sm==n1):
    print(f"{n1} is neon")

else:
    print(f"{n1} is not neon")
