# Authors: Joe Chen and Benjamin King

from django.test import TestCase, LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time



class BehaviourTest(TestCase):

   def test_login(self):

      # look up how to remover gecko from path after execution

      driverInst = webdriver.Firefox()
      driverInst.get('http://127.0.0.1:8000/accounts/login/')
      time.sleep(.5)
      driverInst.find_element_by_name("username").send_keys("admin490")
      time.sleep(.5)
      driverInst.find_element_by_name("password").send_keys("Sup3rP@s$wOrd")
      time.sleep(.5)
      driverInst.find_element_by_class_name("btn-secondary").click()
      time.sleep(.5)
      driverInst.find_element_by_name("logout").click()
      time.sleep(.5)
      driverInst.find_element_by_name("login").click()
      time.sleep(.5)
      driverInst.find_element_by_name("username").send_keys("admin490")
      time.sleep(.5)
      driverInst.find_element_by_name("password").send_keys("Sup3rP@s$wOrd")
      time.sleep(.5)
      driverInst.find_element_by_class_name("btn-secondary").click()
      time.sleep(.5)
      driverInst.find_element_by_name("reports").click()
      time.sleep(.5)
      driverInst.find_element_by_name("return").click()
      time.sleep(.5)
      driverInst.find_element_by_name("new").click()
      time.sleep(.5)
      driverInst.find_element_by_name("home").click()
      time.sleep(1)
      driverInst.quit()