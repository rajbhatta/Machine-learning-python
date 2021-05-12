from service.MobileService import MobileService


class IphoneMobileService(MobileService):
    def updgradeSoftware(self):
        print('This method will upgrade the software')

    def upgradeCost(self):
        print('This method will downgrade the software')