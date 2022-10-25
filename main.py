#from art import logo
from replit import clear
#print(logo)

#Add
def add(n1, n2):
  return n1 + n2

#Substract
def substract(n1, n2):
  return n1 - n2

#Multiply
def multiply(n1, n2):
  return n1 * n2

#Divide
def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": substract,
  "*": multiply,
  "/": divide
}

def start_over():
  num1 = float(input("What's the first number?:\n")) 
  
  for key in operations:
    print(key)
  
  operation_symbol = input("Pick and operation from the line above: ")
  
  num2 = float(input("What's the second number?:\n"))
  
  def calculate(num1, num2, operation_symbol):
    calc = operations[operation_symbol](num1, num2)
    return calc
  
  answer = calculate(num1, num2, operation_symbol)
  print(f"{num1} {operation_symbol} {num2} = {answer}")
  
  is_continue = True
  while is_continue:
    continue_question = input('Type "y" to continue calculating or "n" to start over again:\n').lower()
    if continue_question == "y":
      clear()
      num1 = answer
      print(f'Your first number is {num1}.')
      for key in operations:
        print(key)
      operation_symbol = input("Pick and operation from the line above: ")
      num2 = float(input("What's the next number?:\n"))
      answer = calculate(num1, num2, operation_symbol)
      print(f"{num1} {operation_symbol} {num2} = {answer}")
    elif continue_question == "n":
      clear()
      print(f"{num1} {operation_symbol} {num2} = {answer}")
      is_continue = False
      start_over()
    else:
      clear()
      print('Wrong input. Try again.')

start_over()
    
    

