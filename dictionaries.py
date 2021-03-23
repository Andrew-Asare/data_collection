# Dictionaries?
# Dictionaries use KEY VALUE pairs to save the data
# The data can be retrieved by its value or the key
# Syntax dict{} list[] tuple()
# Within the dictionary we can also have a list declared

# Let's create one
dev_ops_student = {
    "key": "value",
    "name": "Andrew",
    "stream": "devops",
    "completed_lessons": 3,
    "completed_lessons_names": ["variables", "data types", "collections"]
    #key                value:  0               1           2
}
# print(dev_ops_student)
# confirm the type
# print(type(dev_ops_student))

# print(dev_ops_student["name"])
# print(dev_ops_student["completed_lessons"])
# print(dev_ops_student["completed_lessons_names"])
# print(dev_ops_student["completed_lessons_names"][1])

#
#
#
# # add "operators" in completed_lesson_names
#
# dev_ops_student["completed_lessons_names"].append("operators")
# print(dev_ops_student)
#
# # change the completed lesson from 3 to 4
#
# dev_ops_student["completed_lessons"] = 4
# print(dev_ops_student)
#
# # remove the "data type from completed_lesson_names
#
# dev_ops_student["completed_lessons_names"].remove("data types")
# print(dev_ops_student)

# Sets? The difference is that sets are unordered
# Syntax {}
# Let's create a set

car_parts ={"wheels", "windows", "doors"}
print(car_parts)
print(type(car_parts))
car_parts.add("seats")
print(car_parts)
car_parts.discard("doors")
print(car_parts)



# Frozen sets
#The frozenset() function returns an unchangeable frozenset object (which is like a set object, only unchangeable).