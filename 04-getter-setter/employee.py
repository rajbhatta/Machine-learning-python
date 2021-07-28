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

    


