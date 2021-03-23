# Data collections in Python

- Lists and Tupels
- Dictionary 
- Sets
- What is list?
- Commonly used to store the data
### Lists are MUTABLE
- syntax [ ] used to create a list example:
  `shopping_list = ["bread", "chocolate", "avocados", "milk"]
print(shopping_list[1])`

### To change a value in a list
  `shopping_list[0] = "orange"
print(shopping_list)`

### To add a new value to a list
`shopping_list.insert(1, "ice cream")
shopping_list.append("coke")`

### pop() deletes the last item from the list
``shopping_list.remove("orange")``

###Can we mix fata types in a list? yes
mixed_list = [1, 2, 3, "one", "two", "three"]