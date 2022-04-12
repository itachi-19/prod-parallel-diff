from msg_xml.file_xml import FileXML

class XMLDiffer:

    def __init__(self, msg1, msg2):
        self.xml1 = FileXML(msg1)
        self.xml2 = FileXML(msg2)
        
    def get_diff_between_xpaths(self):
        xpaths1 = set(self.xml1.get_xpaths())
        xpaths2 = set(self.xml2.get_xpaths())

        all_xpaths = xpaths1.union(xpaths2)

        diffs = []

        for xpath in all_xpaths:
            val1 = self.xml1.get_value_for_xpath(xpath)
            val2 = self.xml2.get_value_for_xpath(xpath)
            if val1 != val2:
                diffs.append([xpath, (val1, val2)])

        return diffs

