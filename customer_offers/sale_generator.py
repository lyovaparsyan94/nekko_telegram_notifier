import random
from config.constants import CONFIG_FILE
from config.config_loader import ConfigLoader


class CustomerOfferGenerate:

    def __init__(self):
        self.config_loader = ConfigLoader.config_loader(config_file=CONFIG_FILE)

    def set_random_sale(self):
        min_discount = int(self.config_loader['min_discount'])
        max_discount = int(self.config_loader['max_discount'])
        return random.randint(min_discount, max_discount)


discount = CustomerOfferGenerate().set_random_sale()
