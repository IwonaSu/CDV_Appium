import os
import unittest
from time import sleep

from appium import webdriver

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


    # def test_arcs(self):
    #     self.driver.find_element_by_accessibility_id("Graphics").click()
    #     self.driver.find_element_by_accessibility_id("Arcs").click()
    #     sleep(5)
    #     currentHeader = self.driver.find_elements_by_class_name("android.widget.TextView")[0].get_attribute("text")
    #     self.assertIsNotNone(currentHeader)
    #     self.assertEqual(currentHeader, "Graphics/Arcs")
    #     sleep(5)
    #     self.driver.back()

    def test_app(self):
        #self.driver.find_element_by_accessibility_id("Graphics").click()
        options = self.driver.find_elements_by_class_name("android.widget.TextView")
        for el in options:
            if el == "App":
                print("App is here!")

        amountOptions = 0
        for el2 in options:
            amountOptions = amountOptions + 1

        print("There are " + str(amountOptions) + " options.")
        if amountOptions >= 10:
            print("There are at least 10 options.")
        else:
            print("There are less than 10 options.")


        clickableOptions = self.driver.find_elements_by_android_uiautomator('new UiSelector().clickable(true)')
        amountClickableOptions = len(clickableOptions)
        if amountOptions == amountClickableOptions:
            print("All of them are clickable!")
        else:
            print("Not all of them are clickable!")

        self.assertGreaterEqual(amountOptions, 10)

        sleep(5)
        self.driver.back()

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestowanieAplikacji)
    unittest.TextTestRunner(verbosity=2).run(suite)
