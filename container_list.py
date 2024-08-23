
class FirstObject:
   print("This is from the FirstObject object")

object1 = FirstObject()

list_a = ['abc', 123, False, 1.5, 'a', object1]

print(list_a)

for i in list_a:
   print(i)