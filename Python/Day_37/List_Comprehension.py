x = [1,2,3,4,5,6,7,8,9,10]
x2 = [i+2 for i in x]
x_even = [i for i in x if i%2==0]
x_square = [i**2 for i in x]
x_even_cube = [i**3 for i in x if i%2==0]
print(x)
print(x2)
print(x_even)
print(x_square)
print(x_even_cube)
