
def add_binaries(foo, bar):
  
  return bin(int(foo, 2 ) + int(bar, 2 ))
  

def add_zeros(foo):
  # adds preceeding zeros
  bar = foo[2:].zfill(8) # [2:] removes '0b' at the start. zfill usefully fills 8 chars with zeros
  
  return bar

def digify(row, col):
  
  foo = bin(row*3+col) # ineficient
  
  return foo#bar

# Examples:
print(digify(0, 1))  # Returns 00011111
print(digify(0, 2))  # Returns 00100000
print(digify(0, 3))  # Returns 00100001

print(digify(1, 1))  # Returns 00001011
print(digify(1, 2))  # Returns 00001100
print(digify(1, 0))  # Returns 00001101

print(digify(2, 0))  # Returns 00010111
print(digify(2, 1))  # Returns 00010101
print(digify(2, 2))  # Returns 00010110


# how to add to binary numbers (which python stores as strings)
#c = bin(int(a,2) + int(b,2))

x = digify(3, 3)  # Returns 00100001
y = digify(2, 3)  # Returns 00100001

total = add_binaries(x, y)

z = digify(3, 2)  # Returns 00100001

total = add_binaries(total, z)

print(total)

print(add_zeros(total))


