
def sum (n):
    sum = 0
    
    for i in range(1,n+1):
        sum+=i
        
    return sum


def product (n) :
    product= 1 
    for i in range(1,n+1):
        product*=i
        
    return product
    
n=int(input('Enter a number : '))

choice= int (input ('Enter 1 to sum, 2 to product : '))

if choice == 1 :
    print(sum(n))
if choice == 2 :
    print (product(n))
