import xml.etree.ElementTree as ET
import xml.dom.minidom as MD

class GenericXML:
    def __init__(self, message):
        self.message = message
        self.root = ET.fromstring(message)

    def get_xpaths(self):
        pass

    def get_value_for_xpath(self, xpath):
        return self.root.find(xpath).text.strip()

    def get_msg():
        return self.message
