#basics


#variables

a = 1 #integer
b = "b" #string
c = True #boolean
d = None #none
e = a #assignment 
f = 2.3 #float
g = [a, "a", 12, True, [a, b, c], {"x": 123, "y": 321}, 123.123] #list
h = (a, "a", 12, True, [a, b, c], {"x": 123, "y": 321}, 123.123) #tuple
i = {
  "name": "Baitemir",
  "age": 17,
  "occation": "developer",
  "isMarried": False
} #dictionary


#functions

#function declaration
def func(arg):
  print("hello " + arg)

#function call
func("baitemir")

#if else statement

if(1 > 2):
  print("1 is greater than two")
elif(1 == 2):
  print("1 is equal to 2")
else:
  print("i'm not stupid")


#while loops
i = 1
while(i < 3):
  print("loop № " + str(i))
  i+= 1

#for loops
for i in range(5):
  print(i)