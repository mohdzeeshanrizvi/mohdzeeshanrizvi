# convert two list into dictionary?
# keys=['ten','twenty','thirty']
# values=[10,20,30]
# dict1=dict(zip(keys,values))
# print(dict1)


# merge two python dictionaries into one?
# dict1={'ten':10,'twenty':20,'thirty':30}
# dict2={'thirty':30,'forty':40,'fifty':50}
# dict3={**dict1,**dict2}
# print(dict3)


# print the value of key'history'from the below dict?
# sampleDict={
#     "class":{
#         "student":{
#             "name":"mike",
#             "marks":{
#                 "physics":70,
#                 "history":80
#             }
#         }
#     }
# }
# print(sampleDict['class']['student']['marks']['history'])


# initialize keys with default values?
# employees=['kelly','emma']
# defaults={"designation":'developer',"salary":8000}
# updated=dict.fromkeys(employees,defaults)
# print(updated)



# create a dictionary by extracting the keys from a given dictionary?
# sampledict={
#     "name":"kelly",
#     "age":25,
#     "salary":8000,
#     "city":"new york"}
# keys=["name","salkary"]
# newdict={k.sampledict[k] for k in keys}
# print(newdict)

# def validate_sum(func):
#     def wrapper(*args, **kwargs):
#         if args[0] >= 0 and args[1] >= 0:
#             print("---Before method call----")
#             output = func(*args, **kwargs)
#             print("---After method call----")
#             return output
#         else:
#             return "INVALID DATA"
#     return wrapper
#
# @validate_sum
# def sum(n1, n2):
#     res = n1 + n2
#     return res
#
# print("Sum of 2 numbers : ", sum(10,5)) # sum (10,-5)


import numpy as np
a=np.array([1,2,3])
b=np.array([4,5,6])
c=a*b