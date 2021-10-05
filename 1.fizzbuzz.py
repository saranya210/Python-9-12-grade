
   
#Enter a number using custom input
a = int(input("Enter a number: "))

# if number is divisible by both 3 and 5 it returns fizzbuzz
if (a%5 == 0 and a%3 == 0):
    print("FizzBuzz")

# if number is divisible by 3 it returns fizz
elif(a%3 == 0 ):
    print("Fizz")

# if number is divisible by 5 it returns buzz
elif (a%5 == 0):
    print("Buzz")

# if none then simply return the number
else:
    print(a)