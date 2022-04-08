#! /usr/bin/env python3

# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 itachi <itachi@DESKTOP-SIH2KFG>
#
# Distributed under terms of the MIT license.

"""
"""
import unittest
import sys
from diff import Diff
from writer import Writer
from reader import Reader
from trade import Trade
from pprint import pprint

class DiffTool:
    def __init__(self, icap_file, fid_file, report_file):
        self.icap_file = icap_file
        self.fid_file = fid_file
        self.report_file = report_file
        self.writer = Writer(report_file)

    def generate_diffs(self):
        reader = Reader(icap_file, fid_file)
        data = reader.data
        not_found = []
        for trade_id in data:
            icap_msg = data[trade_id]['icap_msg']
            if 'fid_msg' not in data[trade_d]:
                self.writer.write_not_found(trade_id)
            else:
                fid_msg = data[trade_id]['fid_msg']
                trade = Trade(trade_id, icap_msg, fid_msg)
                self.writer.write_diff(trade)
        self.writer.generate_report()
    
class Tests(unittest.TestCase):
    def test_Diff(self):
        pass

if __name__ == '__main__':
    try:
        icap_file = sys.argv[1]
        fid_file = sys.argv[2]
        diff_tool = DiffTool(icap_file, fid_file, 'report.html')
    except Exception as e:
        print()
        print( '[X] ERROR: Invalid Files -', e)
    diff_tool.generate_diffs()


