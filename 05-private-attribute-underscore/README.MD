# Working with private property in python #
- In Python, there is no existence of “Private” instance variables that cannot be accessed except inside an object. However, a convention is being followed by most Python code and coders i.e., a name prefixed with an underscore, For e.g. _geek should be treated as a non-public part of the API or any Python code
- <b>Private property can be defined with two underscores.</b>

## Example ##
```python
 self.__firstName=firstName
```
- If we try to print then we will get error

```python
from employee import Employee

def runMe():
    # printing private property
    print(emp1.__firstName)

if __name__ == "__main__":
    runMe()
```

# Using double underscore #
## Using double underscore for method name ##
```python
class SimpleClass:

    def __datacamp(self):
        return "datacamp"

    def call_datacamp(self):
        return self.__datacamp()

obj = SimpleClass()
print(obj.call_datacamp()) ## same as above it returns the Dobule pre underscore method
print(obj.__datacamp())    ## we get an error here
```

## Using double underscore for variable name ##
```python
class SimpleClass:

    def __init__(self):
        self.__datacamp = "Excellent"

    def get_datacamp(self):
        return self.__datacamp

obj = SimpleClass()
print(obj.get_datacamp()) ## it prints the "Excellent" which is a __var
print(obj.__datacamp)     ## here, we get an error as mentioned before. It changes the name of the variable
```