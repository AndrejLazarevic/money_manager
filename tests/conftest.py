import pytest
from driver.driver import form_driver
from driver.driver_object import DriverObject
from utilities.logger import log


@pytest.fixture(scope='function')
def formDriver():
    driver = form_driver()
    DriverObject.set_driver(driver)
    log("Launching app")



