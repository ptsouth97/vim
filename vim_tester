import random as rand

vim_list=[
['h', 'moves one character to the left'],
['l', 'moves one character to the right']
]

print('Welcome to VIM tester!')
print('What is your name?')

name=input()

print('Hello, ' +name)
print('I am going to ask you a series of questions to test your VIM knowledge')

flag=1
right=0
wrong=0

while flag == 1:
	n=rand.randint(0,1)
	print('What command ' +vim_list[n][1]+ '?')
	answer=input()
	if answer==vim_list[n][0]:
		print('Yes, you are correct!')
		right=right+1
	else:
		print('Not quite.  The answer is ' +vim_list[n][0])
		wrong=wrong+1
	print("Enter 1 to continue")
	flag=int(input())

total=right+wrong
percentage=right/total*100
print(name+ ' you got ' +str(percentage)+ '% correct.')
if percentage >= 80:
	print('You are a VIM master!')
else:
	print('Keep working on it!')
