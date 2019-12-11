num=int(input("enter the number"))
c=num
rev=0
while(num>0):
    rem=num%10
    rev=(rev*10)+(rem)
    num=num//10
print("the reversed num:",rev)
if(c==rev):
	print("its a palindrome")
else:
	print("its not a palindrome")