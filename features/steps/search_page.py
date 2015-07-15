from features.browser import Browser
import re


class SearchPage(Browser):

    URL = 'http://www.google.com'
    FIELD_NAME = 'q'
    LINK = '.r > a'

    def open(self):
        self.visit(self.URL)

    def search_for(self, text):
        search_field = self.find_by_name(self.FIELD_NAME)
        self.fill_in(search_field, text)
        self.wait_for_title(text)
        self.wait_for_element(self.LINK)

    def expect(self, link, num):
        script = "return document.querySelectorAll('"+self.LINK+"')["+str(int(num)-1)+"].innerHTML"
        value = self.driver.execute_script(script)
        print(value)
        print(link)
        return re.search(link.lower(), value.lower())