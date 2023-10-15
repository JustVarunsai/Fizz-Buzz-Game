# FizzBuzz
print('''
 ___   __ __     __       __ __ 
|__  |  /  /    |__) |  |  /  / 
|    | /_ /_    |__) \__/ /_ /_ 
''')

print(f"Hi Welcome to Fizz Buzz Game a math game \nRULES:\nIf a number is divided by 3 then Its FIZZ\nIf it's divided by 5 it's BUZZ\nIf both then it's FIZZBUZZ ")
n=int(input("Let's Start\nEnter n number to get till n number of numbers of Fizz Buzz numbers\n"))
for i in range(1,n+1):
  if i%3==0 and i%5==0:
    print('FizzBuzz')
  elif i%3==0:
    print('Fizz')
  elif i%5==0:
    print('Buzz')
  else:
    print(i)