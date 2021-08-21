try:
  print(x)
except:
  print("there is no value of x")

try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")

try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")

try:
  f = open("demofile.txt", 'w')
  f.write("Hello there")
except:
  print("Something went wrong when writing to the file")
finally:
  f.close()
x = "hello"

if not type(x) is int:
  raise TypeError("Only integers are allowed")
