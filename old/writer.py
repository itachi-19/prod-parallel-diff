#! /usr/bin/env python3
from string import Template

class StringBuilder:
    def __init__(self,diff_, missing):
        self.top = Template(open("input/top.html").read())
        self.diff = Template(open("input/diffs.html").read())
        self.not_found = Template(open("input/not_found.html").read())
        self.html = [ self.top, '', '' ]
        self.diffs = []
        self.not_found = ''

    def build_diffs():
        pass

    def append_diff(trade):
        trade_id = trade.trade_id

        self.diffs.append(self.diff.substitute(trade_id))

        

class Writer:
    def __init__(self, report_file):
        self.report = open('output/report2.html', 'w')
        self.not_found_trades = []
        self.diff_trades = []

    def write_diff(self, trade_id, diffs):
        print(trade_id, diffs)

    def write_not_found(self, trade_id):
        self.not_found

    def generate_report():
        output = self.top.read()
        pass

    def close():
        for file in self.top, self.diffs, self.not_found:
            file.close()

def 
