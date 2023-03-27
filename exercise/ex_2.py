import numpy
# square

a_s = 15
perimeter_s = a_s * 4
field_s = a_s ** 2

output_s = f'Perimeter of the square is equal to {perimeter_s} and field is equal to {field_s}.'

#rectangle

a_r = 10
b_r = 8
perimeter_r = 2 * a_r + 2 * b_r
field_r =  a_r * b_r

output_r = f'Perimeter of the rectangle is equal to {perimeter_r} and field is equal to {field_r}.'

#circle

r_c = 7
perimeter_c = 2 * numpy.pi * r_c
field_c = numpy.pi * (r_c ** 2)

output_c = f'Perimeter of the circle is equal to {perimeter_c} and field is equal to {field_c}.'

#trapeze

a_t = 3
b_t = 28
c_t = 10
d_t = 15
h_t = 12

perimeter_t = a_t + b_t + c_t + d_t
field_t = ((a_t + b_t) * h_t)/2

output_t = f'Perimeter of the trapeze is equal to {perimeter_t} and field is equal to {field_t}.'

print(output_s)
print(output_r)
print(output_c)
print(output_t)
