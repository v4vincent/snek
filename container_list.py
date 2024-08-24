
class FirstObject:
   print("This is from the FirstObject object")

object1 = FirstObject()

list_a = ['abc', 123, False, 1.5, 'a', object1]

print(list_a)

for i in list_a:
   print(i)

list_a.append("Add")
print(list_a)

list_a.pop(5)

list_b = [1,2,3,4]

combined_list = list_a + list_b

print(combined_list.index(False))



