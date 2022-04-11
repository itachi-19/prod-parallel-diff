from generic_xml import GenericXML
import io


class FileXML(GenericXML):

    def __init__(self, message):
        self.file = io.StringIO() # dummy file
        self.file.write(message)
        self.file.seek(0)
        super().__init__(message)

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
