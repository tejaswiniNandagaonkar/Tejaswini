#comprehension
#user defined function

########################################################
#comprehension

# _odd = list()
#
# for i in range(1, 10, 2):
#     _odd.append(i)
# print(_odd)
# print("##################     LIST COMPREHENSION     ######################")
#
# _odd = [i for i in range(1, 10, 2)]
# print(_odd)
#
# print("##################")
#
# for i in range(1, 10):
#     if i % 2 == 1:
#         _odd.append(i)
#
# print("##################     LIST COMPREHENSION     ######################")
#
# _odd = [i for i in range(1, 10) if i % 2 == 1 ]
# print(_odd)
#
# print("########################################")
#
# sq = {}
# number = [2, 3, 4, 5, 6, 7, 8, 9]
# for num in number:
#     sq[num] = num * num
#
# print(sq)
#
# #DIRECTORYCOMPREHENSION
# #ex 1 using dictionary
# _sq = {}
# number = [2, 3, 4, 5, 6, 7, 8, 9]
# _sq = { num * num for num in number}
# print(sq)
#
# #ex 2 using list
labels = ['name', 'age', 'contact no']
user_1 = ['teju', 10, 90775456778]
user_2 = ['vishakha', 12, 823758784]
user_3 = ['chandrakant', 24, 823758784]


# _di = {}
# labels = ['name', 'age', 'contact no']
# _di = { 'user_1',
# 'user_2'
# 'user_3'}
# print({labels[0]:user_1[0],labels[1]:user_1[1],labels[2]:user_1[2]})
# print({labels[0]:user_2[0],labels[1]:user_2[1],labels[2]:user_2[2]})
# print({labels[0]:user_3[0],labels[1]:user_3[1],labels[2]:user_3[2]})
#
#
# print("#####################################################")
#
# op =list()
# for user in [user_1, user_2, user_3]:
#     _user  = dict()
#     for index in range(0, 3):
#         _user[labels[index]]= user[index]
#     op.append(_user)
# print(op)
# print("#####################################################")

output =[
    {
        label: user[index] for index, label in enumerate(labels)
    }
    for user in [user_1, user_2, user_3]
]
print(output)

print("#########################    WITHOUT ENUMRATION   ############################")
output =[
    {
        labels[index]: user[index] for index in range(0, 3)
    }
    for user in [user_1, user_2, user_3]
]
print(output)

print("#########################    user defined function   ############################")
#syntax
'''
def <function_name>():
    """
    function doc string
    """
    <statament 1>
    <statament 2>
    .
    .
    .
    <statement n>
'''

def greetings():
    """
    this is greetings fuction with argument
    :param name:
    :return:
    """
    print("hello world")
greetings()

#greetings()

def arg_greetings(name):
    """
    :param name:
    :return:
    """
    print(F"hello {name}")
arg_greetings("teju")
#arg_greeting

def arg_return_greetings(name):
    """
    This id greetings function with arguments and return greeting message
    :param name:
    :return:
    """
    message = F"hello {name}"
    return message
resp = arg_return_greetings(name="teju")
print(resp)

print("#########################    user defined function with user input  ############################")

def arg_return_greetings(name):
    """
    This id greetings function with arguments and return greeting message
    :param name:
    :return:
    """
    message = F"hello {name}"
    return message

_name = input("enter name")
resp = arg_return_greetings(name=_name)
print(resp)

