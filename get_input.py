# check if input contain anything other than 0 and 1
def contains_other_characters(user_input):
  for char in user_input:
    if char not in ['0', '1']:
      return True
    
  return False

# ensure the input binary numbers are valid
def validate_input(numbers, user_input):
  valid = False
  
  if len(user_input) < 4 or len(user_input) > 12: # check length
    print("\nINVALID INPUT! - Input must have a length of (4 ≤ length ≤ 12)\n")
  elif contains_other_characters(user_input): # make sure input is binary
    print("\nINVALID INPUT! - Input can only contain 0 and 1\n")
  elif len(numbers) == 1 and len(numbers[0]) != len(user_input): # make sure length of Multiplicand and Multiplier are equal
    print("\nINVALID INPUT! - Multiplicand and Multiplier must be the same length\n")
  else:
    valid = True
  
  return valid

# get 2 input binary numbers from user
def get_input():
  numbers = []
  
  while len(numbers) < 2:
    user_input = input("Enter the first number (Multiplicand): ") if len(numbers) == 0 else input("Enter the second number (Multiplier): ")
    
    if validate_input(numbers, user_input):
      numbers.append(user_input)
      
  print()
    
  return numbers