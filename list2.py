thislist = ["apple", "banana", "cherry"]
print(thislist)

#Daftar dengan string, bilangan bulat, dan nilai boolean:
list1 = ["abc", 34, True, 40, "male"]

#Periksa apakah Item Ada
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

#Remove Specified Index
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)


#if else
a = 33
b = 200
if b > a:
  print("b is greater than a")

number = 15
if number > 0:
  print("The number is positive")

#Nested If Statements
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")
