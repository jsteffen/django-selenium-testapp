from django.core.urlresolvers import reverse
from django_selenium.testcases import SeleniumTestCase

class MyTestCase(SeleniumTestCase):

    def test_home(self):
        self.open_url(reverse('home'))
        self.failUnless(self.is_text_present('Test Page'))
        self.aseertEquals(self.get_title(), 'Home')
