
from employee import Employee

def runMe():

    # invocation with paramterized constructor
    emp1 = Employee('Niraj', 'Bhatta')
    print(emp1.getLastName())
    print(emp1.getFirstName())



if __name__ == "__main__":
    runMe()
