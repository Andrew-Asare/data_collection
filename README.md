# Data collections in Python

- Lists and Tupels
- Dictionary 
- Sets
- What is list?  
-What is Tuples? 
-What is a Dictionary?
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

###Dictionaries 
-Dictionaries use KEY VALUE pairs to save the data
-The data can be retrieved by its value or the key
- An examle of a dictionary is this:
```python
dev_ops_student = {
    "key": "value",
    "name": "Andrew",
    "stream": "devops",
    "completed_lessons": 3,
    "completed_lessons_names": ["variables", "data types", "collections"]
```
-add "operators" in completed_lesson_names

```python
dev_ops_student["completed_lessons_names"].append("operators")
print(dev_ops_student)
```

- change the completed lesson from 3 to 4

```python
dev_ops_student["completed_lessons"] = 4
print(dev_ops_student)
```

-remove the "data type from completed_lesson_names

```python
dev_ops_student["completed_lessons_names"].remove("data types")
print(dev_ops_student)
```
