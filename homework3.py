# Tab width must be 4 spaces
# assining variables should look like this example:
#     count1 = 0
#     count2 = 0

# rewrite your home work withot "while loop" operator using
# use only "string" object methods

def func():
	count1=0
	count2=0
	i=0
	string=str(input())
	while (string[i]=="("): 
		count1+=1
		i+=1
	i=len(string)-1
	while (string[i]==")"):
		count2+=1
		i-=1
	if count1==count2:
		print("all is correct")
	if count1>count2:
		string=string+")"*(count1-count2)
	else:
		string="("*(count2-count1)+string
	print(string)
func()

