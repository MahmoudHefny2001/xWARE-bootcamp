n = int(input("Enter a number to get the summation from 1 to it: "))
sum = i = 0
while i < n+1:
	sum += i
	i += 1
print("The summation is: ", str(sum))