'''
Project 1: Using zyLabs
This source file performs simple arithmetic calculations.
However, some of them evaluate incorrectly.
If you run the tests you will see that some of them will fail.
'''

def add(num1,num2):
    "Adds num1 to num2"
    return num1+num2
    
def subtract(num1,num2):
    "Subtract num1 from num2"
    return num1 - num2    
    
def multiply(num1,num2):
    "Multiply num1 and num2"
    result = num1*num2   
    return result

def divide(num1,num2):
    "Divide num2 by num1" 
    answer=num1 // num2;   
    return answer
def int_to_string(num):   
    x = ""
    for c in x: 
        if x==num:
            print(x);
        if num == x:
            print(x)
        else:
            pass
    return str(num)
    
def main():
    num1=10
    num2=5
    addition_answer=add(num1,num2)
    print(f"{num1} Plus {num2} is {addition_answer}")
    subtraction_answer=subtract(num1,num2)
    print(f"{num1} subtract {num2} is {subtraction_answer}")
    multiply_answer=multiply(num1,num2)
    print(f"{num1} multiplied by {num2} is {multiply_answer}")
    division_answer=divide(num1,num2)
    print(f"{num1} divided by {num2} is {division_answer}")
    in2string_answer=int_to_string(num1)
    print(f"num1={num1} data type is a{type(in2string_answer)}")
if __name__ == "__main__":
    main()