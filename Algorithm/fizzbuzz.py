#1-100
#3-Fizz
#5-Buzz
#3 & 5 - FizzBuzz
#i

def FizzBuzz(num):
	if not num % 15:
		return "fizzbuzz"
	elif not num % 3:
		return "fizz"
	elif not num % 5:
		return "buzz"
	return num
    
print(FizzBuzz(1))
print(FizzBuzz(15))   
print(FizzBuzz(3))
print(FizzBuzz(42))
print(FizzBuzz(223230))
print(FizzBuzz(17))
