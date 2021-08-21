# there is  awesome methods in
# iterator like : __next__()
tuple1 = (1, 2, 3, 4, 5)
tuple_iter = tuple1.__iter__()
print(tuple_iter.__next__())
print(tuple_iter.__next__())
print(tuple_iter.__next__())
print(tuple_iter.__next__())
print(tuple_iter.__next__())
# you can also use iter() and next()

tuple2 = ('h', 'j', 'ok', 'kpk', 'nkjkpk')

tuple2_iter = iter(tuple2)
print(tuple2_iter)
print(next(tuple2_iter))
print(next(tuple2_iter))
print(next(tuple2_iter))
print(next(tuple2_iter))
print(next(tuple2_iter))
# application of iterrator in class


class Increment:
  def __iter__(this):  # u can use any name you want
    this.increment_number = 1
    return this  # we going to chain the class

  def __next__(this):
    if this.increment_number <= 20:
     x = this.increment_number
     this.increment_number += 1
     return x
    else:
      raise StopIteration


increment = Increment()
print(increment)
increment_iter = iter(increment)
for val in range(0, 10):
 print(next(increment_iter))

#if we loop oo we will get a problem
for val in increment_iter:
  # infinet loop to stop it we have to add thar StopIteration
  print(next(increment_iter))
