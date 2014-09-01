#!/usr/bin/python3

from itertools import zip_longest

class Number:
  def __init__(self, registers, numeral):
    self.numeral = numeral
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
      if x > y and not overflow:
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

  def __mul__(self, other):
    if self != other:
      raise ValueError("Different numeral systems")

    numeral = self.numeral
    result = []
    r1 = []
    r2 = []
    overflow = False

    for x in self.registers:
      for y in other.registers:
        r = y * x
        print(x, y, r)
        if r >= numeral:
          r = str(r)
          # print(r, r[-1], r[0:-1], "*")
          r2.append(r[-1])
          overflow = True
        result.append(r)
      r1 = result
        # print(r1)

    # return Number(result, numeral)

# def __floordiv__(self, other):

  def __str__(self):
    return str(self.registers)

  def __ne__ (self, other):
    if self.numeral != other.numeral:
      return True
    else:
      return False



def test():

  test_list = [
                [Number((3, 255), 256), Number((2, 3), 256)],
                [Number((1, 9), 10), Number((2, 7), 10)],
                [Number((0, 1), 2), Number((1, 0), 2)],
                [Number((2, 7), 8), Number((3, 5), 8)]
              ]

  for x, y in test_list:
    sum = x + y
    diff = x - y
    # mult = x * y 

    print("NS: {}   \t {} + {} = {}".format(x.numeral, x, y, sum))
    print("NS: {}   \t {} - {} = {}".format(x.numeral, x, y, diff))
    # print("NS:   {} \t {} * {} = {}".format(x.numeral, x, y, mult))

test()