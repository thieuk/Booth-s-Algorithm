# arithmetic shift right
def shift_right(A, Q):
  result = []
  AQ = A + Q
  left_bit = A[0]
  AQe = left_bit + AQ
  
  result.append(AQe[0:len(A)]) # AC
  result.append(AQe[len(A):len(AQe) - 1]) # Q
  result.append(AQe[len(AQe) - 1]) # Extended bit
  
  return result

# add two binary numbers 
def addition(num1, num2):
  sum = [0] * len(num1)
  c = 0
  
  for i in range(len(num1)):
    index = len(num1) - i - 1
    
    if num1[index] == num2[index]: 
      if num1[index] == "0": 
        if c == 1:
          sum[index] = 1
          c = 0
      else:
        if c == 0:
          c = 1
        else:
          sum[index] = 1
          c = 1
    else:
      if c == 0: 
        sum[index] = 1
      else:
        c = 1
  
  for i in range(len(sum)):
    sum[i] = str(sum[i])
  
  return "".join(sum)

# converts binary number to its second complement 
def second_comp(num):
  result = ["0"] * len(num)
  one = ["0"] * (len(num) - 1)
  one.append("1")
  
  # converts to 1's complement
  for i in range(len(num)):
    if num[i] == "0":
      result[i] = "1"
    else:
      result[i] = "0"

  return addition("".join(result), "".join(one))