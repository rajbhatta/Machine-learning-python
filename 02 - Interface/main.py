
# Press the green button in the gutter to run the script.
from service.IphoneMobileService import IphoneMobileService

if __name__ == '__main__':
   mobileService= IphoneMobileService()

   # Call upgradeSoftware
   mobileService.updgradeSoftware()

   #call upgradeCost
   mobileService.upgradeCost()


