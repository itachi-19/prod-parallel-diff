#! /usr/bin/env python3

class Diff:
    def __init__(self, xpath='/NewTrade/rate', icap_val=0.33, fid_val=234):
        self.xpath = xpath
        self.diff = 0.33, 5.3423

    def __str__(self):
        return f'{self.xpath} -> (f{self.diff})'

    def __repr__(self):
        return f'{self.xpath} -> (f{self.diff})'
