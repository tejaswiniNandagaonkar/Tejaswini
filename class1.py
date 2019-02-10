# '''
# 1) write a code to find maximum number from 5 values
# 2) write a code to find minimum number from 5 values
# 3) write a code to find maximum number from 10 values with only single if statement
# 4) write a code to find minimum number from 10 values with only single if statement
# '''
# num1 = 100
# num2 = 20
# num3 = 60
# num4 = 40
# num5 = 50
#
# if num1 > num2 and num1 > num3 and num1 > num4 and num1 > num5:
#              print("num1 is max")
# else:
#       if num2 > num3 and num2 > num4 and num2 > num5:
#              print("number 2 is max")
#       else:
#             if num3 > num4 and num3 > num5:
#                 print("number 3 is max")
#             else:
#                 if num4 > num5:
#                           print("number 4 is max")
#                 else:
#                           print("number 5 is max")
#
#
# if (num1 >= num2) and (num1 >= num3) and (num1 >= num4) and (num1 >= num5):
#    largest = num1
# elif (num2 >= num1) and (num2 >= num3) and (num2 >= num4) and (num2 >= num5):
#    largest = num2
# elif (num3 >= num1) and (num3 >= num3) and (num3 >= num4) and (num3 >= num5):
#    largest = num3
# elif (num4 >= num1) and (num4 >= num3) and (num4 >= num4) and (num4 >= num5):
#    largest = num4
# else:
#    largest = num5
#
# print("The largest is",largest)
#
# if (num1 <= num2) and (num1 <= num3) and (num1 <= num4) and (num1 <= num5):
#    smallest = num1
# elif (num2 <= num1) and (num2 <= num3) and (num2 <= num4) and (num2 <= num5):
#    smallest = num2
# elif (num3 <= num1) and (num3 <= num3) and (num3 <= num4) and (num3 <= num5):
#    smallest = num3
# elif (num4 <= num1) and (num4 <= num3) and (num4 <= num4) and (num4 <= num5):
#    smallest = num4
# else:
#    smallest = num5
#
# print("The smallest is",smallest)
#
#
# list1 = [20,90,280,500,22,25,89,100,266,1]
# list1.sort(reverse= False)
# print("the number is max",list1[0])
#
#
# list1 = [20,90,280,500,22,25,89,100,266,1]
# list1.sort(reverse= True)
# print("the number is max",list1[0])
#
#
#
# list = [20,30,100,1,4,78,9,2,10,8]
# i = 0
# while i <= 5:
#     if i < list[i]:
#         max = list[i]
#         i += 1
# print(list[i])
#
#
# #For Loop
#
# for i in range(0, 5):
#     for j in range(0, i):
#         print(j, end=" ")
#

for i in range(0, 5):
    for j in range(0, 5):
        print(i % 2, end=" ")
    print(" ")

print("###########################################")

for i in range(1, 6):
    for j in range(1, 6):
        print(j, end=" ")
    print(" ")

print("###########################################")

for i in range(0,6):
    for j in range(0, i+1):
        print(2**(j+1), end= " ")
    print(" ")


print("###########################################")

k = 2*(6-2)
for i in range(1, 6):
    for j in range(1,k):
        print(end=" ")
    k = k -2
    for j in range(1, i+1):
        print("1", end=" ")
    print(" ")
print("###########################################")
n=1
for i in range(1,6):
    for j in range(1,6):
        print(n, end=' ')
        n+=1
    print("")
print("###########################################")

num = 0
for i in range (1, 7):
    if(i%2 == 1):
        start = 1
        end = 6
        inc = 1
        num += 1
    else:
        start = 5
        end = 0
        inc = -1
    for j in range(start,end,inc):
        print("%02d"%(j*num)   , end=" ")
    print(" ")


print("###########################################")

s=" "
for i in range(1, 6):
    for