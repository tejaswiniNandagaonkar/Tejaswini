# '''
# 1) write a code to find maximum number from 5 values
# 2) write a code to find minimum number from 5 values
# 3) write a code to find maximum number from 10 values with only single if statement
# 4) write a code to find minimum number from 10 values with only single if statement
# '''
num1 = 100
num2 = 20
num3 = 60
num4 = 40
num5 = 50

if num1 > num2 and num1 > num3 and num1 > num4 and num1 > num5:
             print("num1 is max")
else:
      if num2 > num3 and num2 > num4 and num2 > num5:
             print("number 2 is max")
      else:
            if num3 > num4 and num3 > num5:
                print("number 3 is max")
            else:
                if num4 > num5:
                          print("number 4 is max")
                else:
                          print("number 5 is max")


if (num1 >= num2) and (num1 >= num3) and (num1 >= num4) and (num1 >= num5):
   largest = num1
elif (num2 >= num1) and (num2 >= num3) and (num2 >= num4) and (num2 >= num5):
   largest = num2
elif (num3 >= num1) and (num3 >= num3) and (num3 >= num4) and (num3 >= num5):
   largest = num3
elif (num4 >= num1) and (num4 >= num3) and (num4 >= num4) and (num4 >= num5):
   largest = num4
else:
   largest = num5

print("The largest is",largest)

if (num1 <= num2) and (num1 <= num3) and (num1 <= num4) and (num1 <= num5):
   smallest = num1
elif (num2 <= num1) and (num2 <= num3) and (num2 <= num4) and (num2 <= num5):
   smallest = num2
elif (num3 <= num1) and (num3 <= num3) and (num3 <= num4) and (num3 <= num5):
   smallest = num3
elif (num4 <= num1) and (num4 <= num3) and (num4 <= num4) and (num4 <= num5):
   smallest = num4
else:
   smallest = num5

print("The smallest is",smallest)


list1 = [20,90,280,500,22,25,89,100,266,1]
list1.sort(reverse= False)
print("the number is max",list1[0])


list1 = [20,90,280,500,22,25,89,100,266,1]
list1.sort(reverse= True)
print("the number is max",list1[0])



list = [20,30,100,1,4,78,9,2,10,8]
i = 0
while i <= 5:
    if i < list[i]:
        max = list[i]
        i += 1
print(list[i])


#For Loop

for i in range(0, 5):
    for j in range(0, i):
        print(j, end=" ")
    print('')
