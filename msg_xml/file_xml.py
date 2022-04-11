from msg_xml.generic_xml import GenericXML
import xml.etree.ElementTree as ET
import io


class FileXML(GenericXML):

    def __init__(self, message):
        self.file = FileXML.get_dummy_file(message) # dummy file
        super().__init__(message)
    
    @staticmethod
    def get_dummy_file(message):
        file = io.StringIO()
        file.write(message)
        file.seek(0)
        return file

    def path_generator(self):
        path = []
        it = ET.iterparse(self.file, events=('start', 'end'))
        for evt, el in it:
            if evt == 'start':
                path.append(el.tag)
                yield '/'.join(path)
            else:
                path.pop()

    def get_xpaths(self):
        xpaths = set()
        for  path in self.path_generator():
            if path != 'NewTrade':
                xpaths.add(path.replace('NewTrade','.'))
        return xpaths
