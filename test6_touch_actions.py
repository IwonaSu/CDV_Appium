import os
import unittest
from time import sleep

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class TestowanieAplikacji(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platfomVersion'] = '7.0'
        desired_caps['deviceName'] = 'Gigaset GS170'
        desired_caps['app'] = PATH('ApiDemos-debug.apk')
        desired_caps['appPackage'] = 'io.appium.android.apis'
        desired_caps['appActivity'] = 'io.appium.android.apis.ApiDemos'

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()


    def test_touch(self):
        self.driver.find_element_by_accessibility_id("Views").click()
        self.driver.find_element_by_accessibility_id("Expandable Lists").click()
        self.driver.find_element_by_accessibility_id("1. Custom Adapter").click()

        peopleNames = self.driver.find_element_by_xpath("//android.widget.TextView[@text = \"People Names\"]")
        action = TouchAction(self.driver)
        action.long_press(peopleNames).release().perform()
        sleep(4)
        sampleMenu = self.driver.find_element_by_xpath("//android.widget.TextView[@text = \"Sample menu\"]")
        self.assertIsNotNone(sampleMenu)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestowanieAplikacji)
    unittest.TextTestRunner(verbosity=2).run(suite)