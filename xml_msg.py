import xml.etree.ElementTree as ET
import xml.dom.minidom as MD
import io


class XMLMsg:


    def __init__(self, message):
        self.message = message
        self.xpath_root = ET.fromstring(message)
        self.file_root = io.StringIO()
        self.file_root.write(self.message)
        self.file_root.seek(0)

    def get_msg(self):
        dom = MD.parseString(self.message)
        return dom.toprettyxml()

    def get_xpaths(self):
        xpaths = set()
        for  path in self.path_generator():
            if path != 'NewTrade':
                xpaths.add(path.replace('NewTrade','.'))
        return xpaths

    def path_generator(self):
        path = []
        it = ET.iterparse(self.file_root, events=('start', 'end'))
        for evt, el in it:
            if evt == 'start':
                path.append(el.tag)
                yield '/'.join(path)
            else:
                path.pop()

    def get_value_for_xpath(self, xpath):
        return self.xpath_root.find(xpath).text.strip()
