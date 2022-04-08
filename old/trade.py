#! /usr/bin/env python3

from diff import Diff
from xml_parser import XMLParser

class Trade:
    def __init__(self, trade_id, icap_msg, fid_msg):
        self.trade_id = trade_id
        xmlparser = XMLParser(icap_msg, fid_msg)
        self.diffs = xmlparser.get_diffs()
