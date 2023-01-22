class DriverObject:

    driver = None

    # getter method
    @classmethod
    def get_driver(cls):
        return cls.driver

    # setter method
    @classmethod
    def set_driver(cls, x):
        cls.driver = x
