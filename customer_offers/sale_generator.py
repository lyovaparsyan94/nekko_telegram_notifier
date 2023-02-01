import random
from config.constants import CONFIG_FILE
from config.config_loader import ConfigLoader


class CustomerOfferGenerate:

    def __init__(self):
        self.config_loader = ConfigLoader.config_loader(config_file=CONFIG_FILE)

    def set_random_sale(self):
        min_discount = int(self.config_loader['min_discount'])
        max_discount = int(self.config_loader['max_discount'])
        pers_disc_text = self._personal_discount_text()
        random_sale = random.randint(min_discount, max_discount)
        return f'{pers_disc_text} {random_sale} %'

    def custom_greeting_message(self):
        if self.config_loader['arm_version'] is True:
            return self.config_loader['arm_start_text']
        else:
            return self.config_loader['rus_start_text']

    def _define_arm_version(self):
        if self.config_loader['arm_version'] is True:
            return True
        else:
            return False

    def _personal_discount_text(self):
        if self._define_arm_version() is True:
            return self.config_loader['arm_personal_sale_text']
        else:
            return self.config_loader['rus_personal_sale_text']


discount = CustomerOfferGenerate().set_random_sale()
start_text = CustomerOfferGenerate().custom_greeting_message()
# sale_text = CustomerOfferGenerate()._personal_discount_text()
