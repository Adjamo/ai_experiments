
def add_binaries(foo, bar):
  
  return bin(int(foo, 2 ) + int(bar, 2 ))
  

def add_zeros(foo):
  # adds preceeding zeros
  bar = foo[2:].zfill(8) # [2:] removes '0b' at the start. zfill usefully fills 8 chars with zeros
  
  return bar

def digify(row, col):
  
  foo = bin(row*13+col) # ineficient
  
  return foo#bar

# Examples:
print(digify(1, 1))  # Returns 00011111 # 1 is ace
print(digify(1, 2))  # Returns 00100000
print(digify(1, 3))  # Returns 00100001
print(digify(1, 4))  # Returns 00100001
print(digify(1, 5))  # Returns 00100001
print(digify(1, 6))  # Returns 00100001
print(digify(1, 7))  # Returns 00100001
print(digify(1, 8))  # Returns 00100001
print(digify(1, 9))  # Returns 00100001
print(digify(1, 10))  # Returns 00100001
print(digify(1, 11))  # Returns 00100001 # 11 is jack
print(digify(1, 12))  # Returns 00100001 # 12 is queen
print(digify(1, 13))  # Returns 00100001 # 13 is king

print(digify(5, 6))  # Returns 00001011
print(digify(6, 5))  # Returns 00001100


# how to add to binary numbers (which python stores as strings)
#c = bin(int(a,2) + int(b,2))

x = digify(3, 3)  # Returns 00100001
y = digify(2, 3)  # Returns 00100001

total = add_binaries(x, y)

z = digify(3, 2)  # Returns 00100001

total = add_binaries(total, z)

print(total)

print(add_zeros(total))


