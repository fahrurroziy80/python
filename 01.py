# tipe data Integer
data_integer = 1
print("data ", data_integer )
print("- bertipe - ", type(data_integer))

# Tipe data float
data_float = 1.2
print("data ", data_float)
print("- bertipe - ", type(data_float))

# tipe data String
data_String = "3"
print("data ", data_String)
print("- bertipe - ", type(data_String))

# tipe data boolen
data_bool = True
print("data ", data_bool)
print("- bertipr - ", type(data_bool))

# tipe data khusus
# bilangan complex
data_complex = complex(8,8)  #j = imaginer
print("data ", data_complex)
print("- bertipe - ", type(data_complex))

# data yang menggunakan bahasa c
from ctypes import c_double

data_c_double = c_double(11.1)
print("data ", data_c_double)
print("- bertipe - ", type(data_c_double))