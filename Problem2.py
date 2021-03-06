"""
	Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

	1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

	By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
"""

#create the fibonacci sequence
num1=1
num2=2
numNext=0;
evensTotal=2
counter=0;

#while loop to create the answer
while(num1<4000000 or num2<4000000):

	#add together the two numbers
	numNext=num2+num1

	if(numNext%2==0): evensTotal+=numNext

	#reassign the values to continue the sequence
	num1=num2
	num2=numNext

	#iterate the counter and reset the numNext value
	counter+=1
	numNext=0

print "The value of the number of evens between one and four million in the Fibonacci sequence is: ", evensTotal