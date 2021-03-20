"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".
Replace this with more appropriate tests for your application.
"""

import time
from django.test import TestCase
from django.test import LiveServerTestCase
#from selenium.webdriver.firefox.webdriver import WebDriver
#from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium import webdriver




#binary = FirefoxBinary("C:\'Program Files (x86)'\'Mozilla Firefox'\firefox.exe") 
#browser = WebDriver.Firefox(firefox_binary=binary) 


class CreateContactIntegrationTest(LiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        #cls.selenium = WebDriver()
        cls.driver = webdriver.Chrome(r'C:\Project\chromedriver.exe')
        cls.driver.get('http://127.0.0.1:8000/')
        super(CreateContactIntegrationTest,cls).setUpClass()
        
    @classmethod
    def tearDownClass(cls):
        #cls.selenium.quit()
        super(CreateContactIntegrationTest,cls).tearDownClass()
            
    def test_login(self):
                
        #self.selenium.get('%s/login' % (self.live_server_url,))
        #self.driver.get('http://127.0.0.1:8000/')
                
        #self.selenium.find_element_by_id('id_username').send_keys("admin")
        time.sleep(5) # Let the user actually see something!
        search_box = self.driver.find_element_by_name('username')
        search_box.send_keys('admin')
        #self.selenium.find_element_by_id('id_password').send_keys("adminadmin")
        search_box = self.driver.find_element_by_id('id_password').send_keys("adminadmin")
        #search_box.submit() 
                
        #self.selenium.find_element_by_xpath("//input[@type='submit']").click()
        self.driver.find_element_by_xpath("//input[@type='submit']").click()
                
        #self.assertEqual(Contact.objects.all()[0].login_form, 'admin')
        
    def test_create_project(self):
        search_box = self.driver.find_element_by_name('username').click() 
        search_box = self.driver.find_element_by_id('project_name')
        search_box.send_keys('project test')
        search_box = self.driver.find_element_by_id('tinymce')
        search_box.send_keys('project test')
        search_box = self.driver.find_element_by_id('id_password').send_keys("adminadmin")
        self.driver.find_element_by_xpath("//input[@type='submit']").click()
                
class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)