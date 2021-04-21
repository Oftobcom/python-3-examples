py_string = 'Python'
print(py_string)

slice_object = slice(1)
print(py_string[slice_object])

slice_object = slice(-1)
print(py_string[slice_object])

slice_object = slice(1, 6, 2)
print(py_string[slice_object])   

slice_object = slice(0, 6, 2)
print(py_string[slice_object])   


print()

py_string='matematica'
print(py_string)

slice_object=slice(3)
print(py_string[slice_object])

slice_object=slice(-3)
print(py_string[slice_object])

slice_object = slice(0,10,4)
print(py_string[slice_object])

slice_object = slice(1,len(py_string),4)
print(py_string[slice_object])
