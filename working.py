#workspace for experimenting

print('Welcome!')

# in python there is no difference between single quotes and double quotes
# triple quotes can be used to create multi line strings
# strings are objects so we can call methods on them

# f strings
# a = 8
# b = 9
# x = f'seven is {a} {b}'

# {a:<09} this will left align with total size 9 and fill rest with zeros

x = 'seven "{1:<09}" "{0:>09}"'.format(8, 9)
print('x is {}'.format(x))
print(type(x))

# bitwise operators & , | , ^ , << , >>

x = 0x0a
y = 0x01
z = x >> y

print(f'(hex) x is {x:02x}, y is {y:02x}, z is {z:02x}')
print(f'(bin) x is {x:08b}, y is {y:08b}, z is {z:08b}')
