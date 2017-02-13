import random as rand
import vim_list

def main():

	print('Welcome to VIM tester!')
	print('What is your name?')

	name=input()

	print('Hello, ' +name)
	print('I am going to ask you a series of questions to test your VIM knowledge')

	flag=1
	right=0
	wrong=0

	the_list = vim_list.commands

	while flag == 1:
		n=rand.randint(0,1)
		print('What command ' +the_list[n][1]+ '?')
		answer=input()
		if answer==the_list[n][0]:
			print('Yes, you are correct!')
			right=right+1
		else:
			print('Not quite.  The answer is ' +the_list[n][0])
			wrong=wrong+1
		print("Enter 1 to continue, or 0 to quit")
		flag=int(input())

	total=right+wrong
	percentage=round(right/total*100,1)
	print(name+ ', you got ' +str(percentage)+ '% correct.')
	if percentage >= 80:
		print(name+ ', you are a VIM master!')
	else:
		print('Keep working on it, ' +name+ '!') 

if __name__ == '__main__':
	main()
