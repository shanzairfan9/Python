# Strings
str = "Shanza Irfan "
str1 = "Consulting firm"
str3 = "Shanza"

print(str[1])

print(str[0:5])  # substring in python

print(str + str1)  # concatenation

print(str3 in str)  # substring check

var = str.split(".")
print(var)
print(var[0])
str4 = " great "
print(str4.strip())
print(str4.lstrip())

print(str4.rstrip())
# Number, Floats and complex
a = 3
print(a)
f = 10.7
print(a)
b, c, d = 5, 6.4, "Great"

# complex
number = '3'
complex_number = complex(number)
print("Complex number formed: ", complex_number)

# List
values = [1, 2, "Shanza", 4, 5]
print(values[0])
print(values[-1])
print(values[1:3])
values.insert(3, "Irfan")
print(values)
values.append("End")
print(values)

values[2] = "Qureshi"  # Updating

del values[0]

print(values)

# Tuple
val = (1, 2, "Shanza", 4.5)

print(val[1])

# val[2] = "Irfan" #this will through an error because tuples are immutables

print(val)

# Dictionary
dic = {"a": 2, 4: "bcd", "c": "Hello world"}

print(dic[4])
print(dic["c"])

dict = {}

dict["firstname"] = "Shanza"

dict["lastname"] = "Irfan"

dict["gender"] = "Female"

print(dict)
print(dict["lastname"])

# set
# set of letters
s = {'g', 'e', 'k', 's'}

s.add('f')
print("Set after updating:", s)

s.discard('g')
print("Set after updating:", s)

s.remove('e')
print("Set after updating:", s)

print("Popped element", s.pop())
print("Set after updating:", s)

s.clear()
print("Set after updating:", s)

# Frozenset
person = {"name": "Shanza", "age": 27, "gender": "female"}

fSet = frozenset(person)
print("Frozen set is:", fSet)
# Bool
value = [0]
print("Boolean of [0] is: ", bool(value))

value = 0
print("Boolean of 0 is: ", bool(value))

value = 1
print("Boolean of 1 is: ", bool(value))

value = -1
print("Boolean of -1 is: ", bool(value))

# byte
print(bytes('Hello World', 'utf-8'))
nums = [1, 2, 3, 4, 5]
print(bytes(nums))

# byteArray
nums = [1, 2, 3, 4, 5]
print(bytearray(nums))

#None
x = None
print(x)

