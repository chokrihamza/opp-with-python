def fn():
  val = 100

  def printval():
    print(val)  # val is available inside the scope
  return printval


fn()()  # or just retur printval() and call fn()


globalval = "am in the global"


def function():
  print(globalval)  # global val are available in all the script


function()

# python is a very storng language
x = 300


def myfunc():
  x = 200
  print(x)


myfunc()

print(x)  # there is no conflict between the two variables
# global keyword


def c():
  global x
  x = 10


c()
print(x)
