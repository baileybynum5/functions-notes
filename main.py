#Functions Notes!

#custom block in snap! is a function in python
#functions have arguments or inputs (inputs to the custom blocks in Snap!)
#lines included in a function must be indented
#to create a function we use "def" which stands for define
#a function must have 2 things EX: def name(): -parenthesis and the colon. arguments or inputs go inside the parenthesis

#a function can also have a return value. this gives the function that value when you call it.
#this makes the function act like a variable

def function_test(input1, input2):
  ans = input1 + input2
  return ans

result = function_test(15, -25)
#on line 16... 15 gets assigned to input1 and -25 gets assigned to input2. that makes the return value -10.
print(result)

num1 = int(input("Enter a number\n\t>"))
num2 = int(input("Enter a second number\n\t>"))
#int() makes whatever is in the parenthesis into an integer

result2 = function_test(num1, num2)
print(result2)
#adding\n\t> at the end of a a prompt creates a nice looking, easy to read prompt.
#end notes