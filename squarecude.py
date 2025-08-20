# square and cube finder

#print('square')
#number1 = input()
#num1 = int(number1)

#print('cube')
#number2 = input()
#num2 = int(number2)

#print('number of square and cube: ')
#number3 = input()
#num3 = int(number3)

#print("square : " + str(num3 ** 2), "cube : " + str(num3 ** 3))

square = int(2) #global variable
cube = int(3)  #global variable

def result(number1): #define function
    return(f"square is :  {number1 ** square} , cube is : {number1 ** cube}")

user_input = input("Enter the number : \n") #print output on screen
user_input_int = int(user_input) #int convert string to integer

value_output = result(user_input_int) #takes input from keyboard and got funtion line
print(value_output) #prints output value


