class DriverObject:

    driver = None

    # getter
    @classmethod
    def get_driver(cls):
        return cls.driver

    # setter
    @classmethod
    def set_driver(cls, x):
        cls.driver = x
