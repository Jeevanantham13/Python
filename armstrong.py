num=int(input("enter a number:"))
c=num
rev=0
while(num>0):
	rem=num%10
	rev=rev+(rem*rem*rem)
	num=num//10
print("the reversed number is:",rev)
if(c==rev):
	print("its an armstrong")
else:
	print("its not an armstrong")
	