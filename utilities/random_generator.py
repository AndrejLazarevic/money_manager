import time
import datetime


class RandomGenerator:

    @staticmethod
    def generate_mail():
        timestamp = time.time()
        return "randommail" + str(timestamp) + "@yopmail.com"

    @staticmethod
    def get_current_date():
        date = datetime.datetime.now()
        return str(date)
