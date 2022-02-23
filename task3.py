def my_func(arg_x, arg_y, arg_z):
    sum_arg = arg_x + arg_y + arg_z
    return sum_arg - min(arg_x, arg_y, arg_z)


x = int(input('x: '))
y = int(input('y: '))
z = int(input('z: '))
print(my_func(x, y, z))

