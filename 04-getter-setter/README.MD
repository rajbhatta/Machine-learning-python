# Working with getter/setter in python #
## Getter setter with default constructor ##
```python

    1. Employee.py

class Employee:

    # Default constructor
    def __init__(self):
        ## Private variable in python
        self.__firstName
        self.__lastName

    # getter method to get property 
    def getFirstName(self):
        return self.__firstName

    # setter method in python
    def setFirstName(self, firstName):
        self.__firstName = firstName

    # getter method to get property 
    def getLastName(self):
        return self.__lastName

    # setter method in python
    def setLastName(self, lastName):
        self.__lastName = lastName
```

```python

2. main.py

from employee import Employee

def runMe():
    # invocation with default constructor
    emp = Employee()
    emp.setFirstName('Raj')
    emp.setLastName('Bhatta')

    print("===================")
    print(emp.getFirstName)
    print(emp.getLastName)

if __name__ == "__main__":
    runMe()

```
# Getter/Setter with Parameterized constructor #
```python

    1. Employee.py

class Employee:

    #Parameterized constructor
    def __init__(self,firstName,lastName):
        self.__firstName=firstName
        self.__lastName=lastName
        
    # getter method to get property 
    def getFirstName(self):
        return self.__firstName

    # setter method in python
    def setFirstName(self, firstName):
        self.__firstName = firstName

    # getter method to get property 
    def getLastName(self):
        return self.__lastName

    # setter method in python
    def setLastName(self, lastName):
        self.__lastName = lastName
```

```python
    
    2. main.py

from employee import Employee

def runMe():

    # invocation with paramterized constructor
    emp1 = Employee('Niraj', 'Bhatta')
    print(emp1.getLastName())
    print(emp1.getFirstName())



if __name__ == "__main__":
    runMe()
```