# Author: Benjamin King
from django.test import TestCase, LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from reservation.models import ReviseReservationModel

# django.test's TestCase is the unit test recommended by django docs
# Create your tests here.


class ReviseReservationTestCase(TestCase):

   # method to create an instance of the ReviseReservationModel
   def create_ReviseReservationModel(self):

      # returns the objects of the instance of the form
      return ReviseReservationModel.objects.all().create()


   def test_ReviseReservationModel(self):

      # attempts to create an instance of the form and assign to variable
      modelVar = self.create_ReviseReservationModel()

	  
      # returns true if an instance of ReviseReservationForm is created
      # successfully
      self.assertTrue(isinstance(modelVar, ReviseReservationModel))
	  
      self.assertEqual(modelVar.district, None)

      self.assertNotEqual(modelVar.schoolName, None)


      # right now, forms are not returning anything, but this
      # test is meant to make sure that the return and the defined
      # value it is meant to return are equal
      #self.assertEqual(modelVar.__str__(), modelVar.schoolName)
	  
