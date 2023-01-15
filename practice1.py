# reverse method on an existing list updates the list in its place - does not return/create a new list
# str.reverse() updates list `str`

# reversed method - create a reversed copy of an existing list in Python, then you can use reversed()
#reversed(list)

#########
def reverse_string(str):
    str_list = (list(str))

    new_str_list = list(reversed(str_list))

    #print(new_str_list)
    str1 = ""
    return print(''.join(new_str_list))
   #return print(str1.join(new_str_list))


reverse_string("Hello!")

#########
#list is equivalent to array, resizable and can have different data types
# def stringReverse(str):
#     strList = list(str)
#     #print(strList)
#
#     for item in reversed(strList):
#         print(item)
#
# stringReverse("Pilot")


