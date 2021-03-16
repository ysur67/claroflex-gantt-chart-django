"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.test import LiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver


class CreateContactIntegrationTest(LiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        cls.selenium = WebDriver()
        super(CreateContactIntegrationTest,cls).setUpClass()
        
        @classmethod
        def tearDownClass(cls):
            cls.selenium.quit()
            super(CreateContactIntegrationTest,cls).tearDownClass()
            
            def test_add_contact(self):
                
                self.selenium.get('%s/new' % (self.live_server_url,))
                
                self.selenium.find_element_by_id('id_first_name').send_keys("Joey")
                self.selenium.find_element_by_id('id_last_name').send_keys("Smith")
                self.selenium.find_element_by_id('id_email').send_keys("Joey@joeysmith.com")
                
                self.selenium.find_element_by_xpath("//input[@type='submit']").click()
                
                self.assertEqual(Contact.objects.all()[0].first_name, 'Joey')
                
class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)
