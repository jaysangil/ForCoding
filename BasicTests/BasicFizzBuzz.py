# function to initiate fizz_buzz game

def fizz_buzz(n):
    
    # loop from i to n+1 
    for i in range(1, n +1):
        # if number both divisible by 3 and 5
        if i % 2 == 0 and i % 5 == 0:
            print("FizzBuzz")
        # check if i is divisible by 2     
        elif i % 2 == 0: 
            print("Fizz")
            
        # check if i is divisible by 5    
        elif i % 5 == 0:
            print("Buzz")
          
        # if above condition doesn't satisfy, print number itself   
        else:
            print(i)
# execute fizz buzz game from numbers 1 to n         
fizz_buzz(150)