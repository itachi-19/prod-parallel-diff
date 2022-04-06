#! /usr/bin/env python3

import xml.etree.ElementTree as ET
import io
from enum import Enum

class XPathSet(Enum):
    ICAP = 1
    COMMON = 2
    FID = 3

class Iterable:
    def __init__(self,file):
        self.file = file
        self.xpaths = set()
        self.set_xpaths()

    def pathGen(self):
        path = []
        it = ET.iterparse(self.file, events=('start', 'end'))
        for evt, el in it:
            if evt == 'start':
                path.append(el.tag)
                yield '/'.join(path)
            else:
                path.pop()

    def set_xpaths(self):
        for path in self.pathGen():
            if path != 'NewTrade':
                self.xpaths.add(path.replace('NewTrade', '.'))

class XMLParser:
    def __init__(self, icap_msg, fid_msg):
        self.icap_msg = icap_msg
        self.fid_msg = fid_msg
        self.icap_root, self.fid_root = ET.fromstring(self.icap_msg), ET.fromstring(self.fid_msg)
        self.icap, self.fid = io.StringIO(), io.StringIO()
        self.initialize_files()
        self.diffs = []

    def initialize_files(self):
        self.icap.write(self.icap_msg)
        self.fid.write(self.fid_msg)
        self.icap.seek(0)
        self.fid.seek(0)

    def get_xpaths(self):
        it_icap, it_fid = Iterable(self.icap), Iterable(self.fid)
        icap_xpaths, fid_xpaths = it_icap.xpaths, it_fid.xpaths

        common_xpaths = icap_xpaths.intersection(fid_xpaths)
        icap_xpaths = icap_xpaths - common_xpaths
        fid_xpaths = fid_xpaths - common_xpaths

        return icap_xpaths, common_xpaths, fid_xpaths

    def get_diff(self, xpath, xpath_set):
        def get_icap_val(xpath): return self.icap_root.find(xpath).text.strip()
        def get_fid_val(xpath): return self.fid_root.find(xpath).text.strip()
        if xpath_set == XPathSet.ICAP:
            return get_icap_val(xpath), 'Not Found'
        elif xpath_set == XPathSet.COMMON:
            icap_val = get_icap_val(xpath)
            fid_val = get_fid_val(xpath)
            if icap_val == fid_val:
                return None
            else:
                return icap_val, fid_val
        else:
            return 'Not Found', self.fid_root.find(xpath).text.strip()

    def append_to_diff(self, xpaths):
        for xpath in xpaths[0]:
            diff = self.get_diff(xpath, xpaths[1])
            if diff:
                self.diffs.append([xpath, diff])

    def get_diffs(self):
        all_xpaths = self.get_xpaths()
        xpathsets = XPathSet.ICAP, XPathSet.COMMON, XPathSet.FID
        xpaths_with_type = zip(all_xpaths, xpathsets)
        for xpaths in xpaths_with_type:
            self.append_to_diff(xpaths)
        return self.diffs
