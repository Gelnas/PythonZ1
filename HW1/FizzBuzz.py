for i in range(100):
    a=i+1
    if a % 15 == 0:
            print('FizzBuzz')
    elif a % 3 == 0:
            print('Fizz')
    elif i+1 % 5 == 0:
	    print('Buzz')
    else:
	    print(i+1)
input()
