def perfect(n):
    sum_divisiors=0
    for i in range(1,n):
        if n%i==0:
            sum_divisiors+=i
            
    if sum_divisiors==n:
        return f"{n} is a perfect number"
    else:
        return f"{n} is a not perfect number"
number=int(input("enter a number"))
print(perfect(number))