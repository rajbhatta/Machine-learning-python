# How to work with classmethod in python #
```python
class ClassMethodDemo:

    def __init__(self, parameters):
        pass

    @classmethod
    def callForClassMethodDemo(cls, parameters):
        pass

```

```python
from classmethoddemo import ClassMethodDemo


def runMeForClassMethod():
    classMthd=ClassMethodDemo()
    classMthd.callForClassMethodDemo()

if __name__ == '__main__':
    runMeForClassMethod()

```

# How to work with staticmethod #
```python
class staticmethoddemo:
    def __init__(self):
        pass

    @staticmethod
    def static_method(args):
        pass
```

```python
from staticmethoddemo import StaticMethodDemo

def runMeForClassMethod():
    """
    classMthd=ClassMethodDemo()
    classMthd.callForClassMethodDemo()
    :return:
    """
    staticCall=StaticMethodDemo.static_method('eeee')

if __name__ == '__main__':
    runMeForClassMethod()
```