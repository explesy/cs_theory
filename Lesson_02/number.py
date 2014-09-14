#!/usr/bin/python3

from itertools import zip_longest

def to_dec(y, numeral):
  ''' Return decimal represntation of the digit in given numeral system '''

  dec = 0 
  power = len(y) - 1

  for digit in y:
    if digit.isdigit():
      dec += int(digit) * (numeral ** power)
    else:
      dec += int(chr_to_num(digit)) * (numeral ** power)

    power -= 1

  return dec


class Number:

  def __init__(self, registers, numeral):
    if numeral >= 2 and numeral <= 256:
      self.numeral = numeral
    else:
      raise ValueError("Numeral system must be from this interval: [2, 256]")
    self.registers = []
    for x in registers:
      if x > (numeral -1): raise ValueError("Register value more than ", numeral-1)
      self.registers.append(x)

  def __add__(self, other):
    if self != other:
      raise ValueError("Different numeral systems")

    numeral = self.numeral

    overflow = False
    result = []
    for x, y in zip_longest(self.registers, other.registers, fillvalue = 0):
      r = x + y
      # print(x, y, r)
      if overflow:
        r += 1
        overflow = False
      if r > (numeral - 1):
        r -= numeral
        overflow = True
      result.append(r)
    if overflow: result.append(1)
    return Number(result, numeral)


  def __sub__(self, other):
    if self != other:
      raise ValueError("Different numeral systems")

    # Nice but not working in systems with numeral nore than 10
    # if int(''.join(map(str, self.registers[::-1]))) < int(''.join(map(str, other.registers[::-1]))):
    #   raise ValueError("First number lesser than second: {} < {}".format(self, other))

    for x, y in zip_longest(reversed(self.registers), reversed(other.registers), fillvalue = 0):
      if x >= y:
        break
      else:
        raise ValueError("First number lesser than second: {} < {}".format(self, other))

    numeral = self.numeral

    overflow = False

    result = []

    for x, y in zip_longest(self.registers, other.registers, fillvalue = 0):
      if x >= y and not overflow:
        r = x - y
      elif x > y and overflow:
        r = x - y - 1
        overflow = False
      elif x < y and not overflow:
        x += numeral
        r = x - y
        overflow = True
      elif x < y and overflow:
        x += numeral
        r = x - y - 1
        overflow = False

      # print(x, y, r)      

      result.append(r)

    return Number(result, numeral)

  def __str__(self):
    return str(self.registers)

  def __ne__ (self, other):
    if self.numeral != other.numeral:
      return True
    else:
      return False

  def __mul__(self, other):
    if self != other:
      raise ValueError("Different numeral systems")

    numeral = self.numeral
    result = []

    factor = ''.join(map(str, other.registers[::-1]))
    factor = to_dec(factor, numeral)

    sum = Number((0, 0), numeral)

    for i in range(0, factor):
      sum += self

    return sum


''' I'm trying but fuck it for now!
  def __mul__(self, other):
    if self != other:
      raise ValueError("Different numeral systems")

    numeral = self.numeral
    result = []
    r1 = []
    iter = 0 
    r2 = []
    overflow = False

    # Multiply numbers and collect them into a list
    for x in self.registers:
      for y in other.registers:
        r = y * x
        # print(x, y, r)
        if r >= numeral:
          r = str(r)
          for digit in r:
            r1.append(int(digit))
          r2.insert(iter, r1)
        else:
          r1.append(r)
          r2.insert(iter, r1)
        r1 = []
        iter +=1

    print(r2)

    step = 1

    # Add some zeroes and reverse numbers
    for digits in r2:
      # print(len(digits), step)
      while len(digits) < step:
        digits.append(0)
      # digits = digits.reverse()
      print(digits)
      step += 1

    # print(r2)
    
    step = 0

    sum = Number((0, 0), self.numeral)
    
    # Sum up the numbers
    for numbers in r2:
      sum += Number(r2[step], self.numeral)
      step += 1

    # print(sum)
        
    return sum
'''


def main():

  test_list = [
                [Number((3, 255), 256), Number((2, 3), 256)],
                [Number((1, 9), 10), Number((2, 7), 10)],
                [Number((9, 9), 10), Number((9, 9), 10)],
                [Number((0, 1), 2), Number((1, 0), 2)],
                [Number((2, 7), 8), Number((3, 5), 8)]
              ]

  for x, y in test_list:
    sum = x + y
    diff = x - y
    mult = x * y 

    print("NS: {}   \t {} + {} = {}".format(x.numeral, x, y, sum))
    print("NS: {}   \t {} - {} = {}".format(x.numeral, x, y, diff))
    print("NS: {}   \t {} * {} = {}".format(x.numeral, x, y, mult))

if __name__ == '__main__':
  main()