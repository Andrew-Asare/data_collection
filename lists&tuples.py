# What is a list?

# Lists are commonly used to store data
# Lists are Mutable
#Syntax [] used to create a list

shopping_list = ["bread", "chocolate", "avacados", "milk"]
#                   0       1           2            3
#
# print(shopping_list)
# print(type(shopping_list))
# print(shopping_list[0:2])
# print(shopping_list[-2])
# change the value of 0 index from bread to orange

shopping_list[0] = "orange"
print(shopping_list)

shopping_list.append("ice cream")

print(shopping_list)

shopping_list.remove("orange")
print(shopping_list)


shopping_list.pop() # deletes the last item from the list or chosen index
print(shopping_list)

#can we mix fata types in a list? yes
mixed_list = [1, 2, 3, "one", "two", "three"]

print(mixed_list[1:3])



