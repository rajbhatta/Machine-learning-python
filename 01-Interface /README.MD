# 1. What is interface in  Python ? #
- In Python, there is no interface similar to other programming language such as Java.
- In Python, interface is an abstract class which contains only the abstract method not concrete method.

# 2. How to create an interface (AbstractClass) ? #
```python

Interface MobileService

from abc import ABC, abstractmethod

class MobileService(ABC):

    @abstractmethod
    def updgradeSoftware(self):
        pass

    @abstractmethod
    def upgradeCost(self):
        pass

```

# 3. How to implement interface ? #
```python
from service.MobileService import MobileService


class IphoneMobileService(MobileService):
    def updgradeSoftware(self):
        print('This method will upgrade the software')

    def upgradeCost(self):
        print('This method will downgrade the software')
```

# 4. Invoke from main method ? #
```python

# Press the green button in the gutter to run the script.
from service.IphoneMobileService import IphoneMobileService

if __name__ == '__main__':
   mobileService= IphoneMobileService()

   # Call upgradeSoftware
   mobileService.updgradeSoftware()

   #call upgradeCost
   mobileService.upgradeCost()
```