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
        desired_caps['app'] = PATH('ContactManager.apk')
        desired_caps['appPackage'] = 'com.example.android.contactmanager'
        desired_caps['appActivity'] = 'com.example.android.contactmanager.ContactManager'
        desired_caps['unicodeKeyboard'] = True
        desired_caps['resetKeyboard'] = True


        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()


    def test_add_contact(self):
        nameInput = "Test"
        phoneInput = "0123456789"
        emailInput = "test@gmail.com"
        self.driver.find_element_by_accessibility_id("Add Contact").click()
        self.driver.find_elements_by_class_name("android.widget.EditText")[0].send_keys(nameInput)
        nameCurrent = self.driver.find_elements_by_class_name("android.widget.EditText")[0].get_attribute("text")
        self.assertEqual(nameCurrent, nameInput)
        self.driver.find_elements_by_class_name("android.widget.EditText")[1].send_keys(phoneInput)
        phoneCurrent = self.driver.find_elements_by_class_name("android.widget.EditText")[1].get_attribute("text")
        self.assertEqual(phoneCurrent, phoneInput)
        self.driver.find_elements_by_class_name("android.widget.EditText")[2].send_keys(emailInput)
        emailCurrent = self.driver.find_elements_by_class_name("android.widget.EditText")[2].get_attribute("text")
        self.assertEqual(emailCurrent, emailInput)

        sleep(3)
        self.driver.find_element_by_accessibility_id("Save").click()



 #       self.assertTrue(self.driver.is_app_installed('com.example.android.contactmanager'))


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestowanieAplikacji)
    unittest.TextTestRunner(verbosity=2).run(suite)
