n = int(input("Enter a number to get the summation from 1 to it: "))
sum = i = 0
while i < n:
	sum += i
	i += i
print("The summation is: ", str(sum))
