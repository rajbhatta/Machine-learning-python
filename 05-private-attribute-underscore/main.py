
from employee import Employee

def runMe():

    # invocation with paramterized constructor
    emp1 = Employee('Niraj', 'Bhatta')
    print(emp1.getLastName())
    print(emp1.getFirstName())

    # printing private property
    print(emp1.__firstName)



if __name__ == "__main__":
    runMe()
