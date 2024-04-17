from get_input import get_input
from booth import *

# performs the basic Booth's algorithm
def Booth(user_input):
  B = user_input[0]
  Q = user_input[1]
  size = len(B)
  AC = "0" * size
  e = "0"
  second_comp_B = second_comp(B)
  add_sub = 0
  
  for i in range(size):
    if Q[size - 1] == e:
      shift = shift_right(AC, Q)
      AC = shift[0]
      Q = shift[1]
      e = shift[2]
    else:
      if Q[size - 1] == "0" and e == "1":
        AC = addition(B, AC)
      else:
        AC = addition(second_comp_B, AC)
        
      shift = shift_right(AC, Q)
      AC = shift[0]
      Q = shift[1]
      e = shift[2]
      
      add_sub += 1
  
  print("=== Booth's RESULT ===")
  print(f"AC: {AC}, Q: {Q}")
  print(f"Number Iterations: {size}")
  print(f"Number ADD/SUB: {add_sub}")
  print()
  
# performs the modified Booth's algorithm
def Modified_Booth(user_input):
  B = user_input[0]
  Q = user_input[1]
  size = len(B)
  AC = "0" * size
  e = "0"
  second_comp_B = second_comp(B)
  shift_num = 0
  add_sub = 0
  iteration = 0
  
  while shift_num < size:
    if Q[size - 1] == Q[size - 2] and Q[size - 2] == e:
      shift = shift_right(AC, Q)
      shift = shift_right(shift[0], shift[1])
      AC = shift[0]
      Q = shift[1]
      e = shift[2]
    elif Q[size - 2] == "0":
      AC = addition(B, AC)
      
      if Q[size - 1] == e:
        AC = addition(B, AC)
        
      shift = shift_right(AC, Q)
      shift = shift_right(shift[0], shift[1])
      AC = shift[0]
      Q = shift[1]
      e = shift[2]
      
      add_sub += 1
    else:
      AC = addition(second_comp_B, AC)
      
      if Q[size - 1] == e:
        AC = addition(second_comp_B, AC)
        
      shift = shift_right(AC, Q)
      shift = shift_right(shift[0], shift[1])
      AC = shift[0]
      Q = shift[1]
      e = shift[2]
      
      add_sub += 1
    
    shift_num += 2
    iteration += 1
  
  print("=== Modified Booth's RESULT ===")
  print(f"AC: {AC}, Q: {Q}")
  print(f"Number Iterations: {iteration}")
  print(f"Number ADD/SUB: {add_sub}")
  print()

if __name__ == "__main__":
  user_input = get_input()
  Booth(user_input)
  Modified_Booth(user_input)